# Call modules, potentially with low level commands

import subprocess
import shutil
from typing import List, Any

from . import PathLike


def _run_kmod(
    cmdline: List[PathLike], **kwargs: Any
) -> "subprocess.CompletedProcess[Any]":
    utility = cmdline[0]

    exe = shutil.which(utility) or "kmod"
    try:
        return subprocess.run(cmdline, executable=exe, **kwargs)
    except FileNotFoundError:
        # Mimic shell return code for not found
        return subprocess.CompletedProcess(cmdline, 127)
    except OSError:
        # Is a directory, permission denied
        return subprocess.CompletedProcess(cmdline, 126)


def run_kmod(
    cmdline: List[PathLike], **kwargs: Any
) -> "subprocess.CompletedProcess[Any]":
    check = kwargs.pop("check", False)
    result = _run_kmod(cmdline, **kwargs)
    if check:
        result.check_returncode()
    return result
