"""
----------------------------------
Kernel Hardening: Loadable Modules
----------------------------------

Kernel modules allow runtime modification of the kernel. To prevent their use
as a malware vector, only vetted, signed modules should be loadable.
"""

import gzip
import lzma
import platform
import os
from typing import Generator, Any, Tuple
import warnings
import re

import pytest

from .decorators import merge_tests, full_version_only
from .utils.kconfig import KconfigSet


def _modules_disabled() -> bool:
    modules_file = "/proc/sys/kernel/modules_disabled"
    try:
        with open(modules_file, "r") as fp:
            return bool(int(fp.read()))
    except FileNotFoundError:
        return True  # Not enabled in the kernel
    except OSError as e:
        warnings.warn(
            f"Could not open {modules_file} to determine module loading status: {e}"
        )
        return False  # Probably not enabled
    except ValueError as e:
        # Should be 0 or 1 only...but take "0" to be the only 'off' value
        warnings.warn(
            f"Could not parse {modules_file} to determine module loading status: {e}"
        )
        return True


pytestmark = pytest.mark.skipif(
    _modules_disabled(), reason="Module loading disabled. All tests pass."
)


KVER = platform.release()


def iter_modules() -> Generator[Tuple[str, Any], None, None]:
    extension = re.compile(r"(?:\.ko|\.ko\.gz|\.ko\.xz|\.ko\.zstd)$")
    module_dir = f"/lib/modules/{KVER}"
    assert os.path.exists(module_dir), "Could not find Linux kernel modules"

    valid_exts = {
        ".ko": open,
        ".ko.gz": gzip.open,
        ".ko.xz": lzma.open,
        ".ko.zstd": None,
    }

    for root, dirs, files in os.walk(module_dir):
        for fname in files:
            if fname.startswith("."):
                continue
            match_ext = extension.search(fname)
            if not match_ext:
                continue

            ext = match_ext.group(0)
            opener = valid_exts[ext]
            if opener is None:
                warnings.warn(f"Module type {ext} not supported")

            kmod = os.path.join(root, fname)
            yield kmod, opener
        dirs[:] = [d for d in dirs if not d.startswith(".")]


def test_has_module_signing(kconfig: KconfigSet) -> None:
    """
    Kernel module signatures should be enabled
    ==========================================

    The Linux kernel can check the integrity of loaded modules to guard against
    corruption and malware.

    See :kevlar-code:`400`.
    """
    assert "CONFIG_MODULE_SIG=y" in kconfig, "Kernel module signing is disabled."


def test_has_strict_module_signing(kconfig: KconfigSet) -> None:
    """
    Kernel module signatures should be mandatory
    ============================================

    Unsigned modules should not be loadable, to guard against malware and
    corruption.

    See :kevlar-code:`400`.
    """
    try:
        with open("/sys/kernel/security/lockdown", "r") as fp:
            is_locked_down = "[none]" not in fp.read()
    except OSError:
        is_locked_down = False

    is_forced = "CONFIG_MODULE_SIG_FORCE=y" in kconfig

    assert is_locked_down or is_forced, "Unsigned kernel modules may be loaded."


@pytest.mark.parametrize("hash", ["sha1", "sha224"])
@merge_tests
def test_has_strong_module_signing_hash(hash: str, kconfig: KconfigSet) -> None:
    """
    Kernel module signatures should use strong hash functions
    =========================================================

    The kernel can be configured to check module integrity using weak or
    deprecated hash functions. These hash functions should be disabled.

    See :kevlar-code:`400`.
    """
    assert (
        f'CONFIG_MODULE_SIG_HASH="{hash}"' not in kconfig
    ), f"Weak hash {hash} used for signing modules."


def test_any_modules_unsigned() -> None:
    """
    All kernel modules should be signed
    ===================================

    All kernel modules that come with the Linux system should have signatures.

    .. note::

       This test looks for the presence of a signature, but it does not
       validate the signatures themselves.

    See :kevlar-code:`400`.
    """
    any_unsupported = False

    marker = b"~Module signature appended~\n"
    for module, opener in iter_modules():
        if opener is None:
            any_unsupported = True
            continue
        with opener(module, "rb") as fp:
            fp.seek(-len(marker), os.SEEK_END)
            end_data = fp.read(len(marker))
            assert end_data == marker, f"Module {module} is not signed!"

    assert (
        not any_unsupported
    ), "Unsupported module compression formats. Not all modules could be checked."


@full_version_only
def test_validate_module_signatures() -> None:
    """
    All kernel modules should be validly signed
    ===========================================

    All kernel modules that come with the Linux system should have valid
    signatures.

    See :kevlar-code:`400`.
    """
    ...


@full_version_only
def test_kernel_refuses_to_load_unsigned() -> None:
    """
    The kernel should not load unsigned modules
    ===========================================

    This test attempts to inject a benign, unsigned module into the kernel.

    See :kevlar-code:`400`.
    """
    ...


@full_version_only
def test_kernel_refuses_to_load_corrupted_data() -> None:
    """
    The kernel should not load modules with corrupted data
    ======================================================

    This test attempts to inject a benign kernel module with data that does not
    match its signature.

    See :kevlar-code:`400`.
    """
    ...


@full_version_only
def test_kernel_refuses_to_load_corrupted_sig() -> None:
    """
    The kernel should not load modules with corrupted signature
    ===========================================================

    This test attempts to inject a benign kernel module with a slightly altered
    signature.

    See :kevlar-code:`400`.
    """
    ...
