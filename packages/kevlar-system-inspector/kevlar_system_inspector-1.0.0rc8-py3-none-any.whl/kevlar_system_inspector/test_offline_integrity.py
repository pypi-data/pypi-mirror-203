"""
---------------------
Application Integrity
---------------------

It is often a simple matter to alter files while the computer is turned off,
allowing an attacker to alter data and executables without needing to bypass
enforcement that happens while the system is live. It is critical to secure the
system from offline tampering, or none of the data on the device can really be
trusted. This is a prerequisite to secure boot.
"""

from typing import Dict
from dataclasses import dataclass
import subprocess
import os
import re

import pytest


@dataclass(frozen=True)
class BlockDevInfo:
    has_encryption: bool
    has_integrity: bool


def get_str_device(dev: int) -> str:
    major = os.major(dev)
    minor = os.minor(dev)
    return f"{major}:{minor}"


def get_mapper_devices() -> Dict[str, str]:
    root = "/dev/mapper"
    mapper_devices = {}
    for name in os.listdir(root):
        path = os.path.join(root, name)
        info = os.stat(path)
        dev = get_str_device(info.st_rdev)
        mapper_devices[dev] = name
    return mapper_devices


def inspect_mountpoint(path: str) -> BlockDevInfo:
    has_encryption = False
    has_integrity = False

    info = os.stat(path)
    mapper_devs = get_mapper_devices()
    devices = [get_str_device(info.st_dev)]

    while devices:
        device = devices.pop()
        if device not in mapper_devs:
            continue

        name = mapper_devs[device]

        try:
            table = subprocess.run(
                ["dmsetup", "table", name],
                check=True,
                text=True,
                stdout=subprocess.PIPE,
            ).stdout
        except (OSError, subprocess.CalledProcessError):
            pytest.fail(f"Cannot run dmsetup to inspect device {name}")

        _start, _end, kind, *fields = table.split()
        if kind in ("verity", "integrity"):
            has_integrity = True
        elif kind == "crypt":
            has_encryption = True

        # Rather than try to understand all of the various tables, like raid or
        # dm-crypt, we will just scan for things that look like devices.
        for field in fields:
            if re.fullmatch(r"\d{1,3}:\d{1,3}", field):
                devices.append(field)

    return BlockDevInfo(has_encryption=has_encryption, has_integrity=has_integrity)


def test_root_filesystem_has_integrity() -> None:
    """
    The root filesystem should be protected at the block level from offline modification
    ====================================================================================

    The root filesystem holds system binaries and configuration and should be
    protected from offline modification. We recommend block-based schemes such
    as dm-verity, because they are higher performance and present fewer
    configuration challenges than file-based schemes.

    See :kevlar-code:`500`
    """

    info = inspect_mountpoint("/")
    assert info.has_integrity, "Root file system is unprotected."
