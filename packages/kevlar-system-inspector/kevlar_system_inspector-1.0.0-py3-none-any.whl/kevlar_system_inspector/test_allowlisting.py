"""
--------------------------------------------------------------
Application Allowlisting: Prevent the introduction of new code
--------------------------------------------------------------

An immutable system should not allow the introduction of new code, even by a
root user. The technique of denying the execution of code that was not
originally part of the system is called application allowlisting.

For more information, see :kevlar-code:`200`.
"""

import warnings
import tempfile
import shutil
import os
import subprocess
from pathlib import Path
import errno
import glob
import re
import stat
from typing import Optional

import pytest

from .utils.elf import ELF, ELFError
from .utils import raises
from .decorators import full_version_only


def _copy_elf(src: Path, dst: Path) -> Path:
    shutil.copy2(src, dst, follow_symlinks=True)
    ELF(dst)  # raise ELFError if it's not an ELF
    return Path(dst)


def _resolve_system_lib(lib_name: str) -> Optional[Path]:
    paths = ["/lib", "/lib64", "/lib/*", "/usr/lib", "/usr/lib64", "/usr/lib/*"]
    for path in paths:
        pattern = os.path.join(path, lib_name)
        files = glob.glob(pattern)
        for file in files:
            # On a development machine, we might find both
            # /usr/lib/x86_64-linux-gnu/<lib> and
            # /usr/lib/aarch64-linux-gnu/<lib>, where the latter is for cross
            # compiling.
            try:
                elf = ELF(file)
                if elf.is_native():
                    return Path(file)
            except ELFError:
                pass
    return None


@pytest.fixture
def cat(workdir: Path) -> Path:
    """A cat-like non-system binary"""
    exename = "cat"
    exepath = shutil.which(exename)
    if not exepath:
        warnings.warn(f"Could not find ``{exename}`` on this system for testing.")
        pytest.skip()

    src = Path(exepath)
    dst = workdir / exename

    try:
        return _copy_elf(src, dst)
        if not (os.stat(dst).st_mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)):
            raise PermissionError(errno.EPERM, "Copy has wrong DAC permissions")
    except (OSError, ELFError) as e:
        warnings.warn("Could not copy suitable ELF binary for testing.")
        pytest.skip(str(e))


@pytest.fixture
def dynamic_cat(cat: Path) -> Path:
    """Ensure that 'cat' is dynamically linked."""
    elf = ELF(cat)
    if not elf.libraries():
        warnings.warn("Could not find suitable dynamically-lined binary for testing")
        pytest.skip()
    return cat


@pytest.fixture
def libc(workdir: Path, cat: Path) -> Path:
    """A copy of libc in a non-system location"""

    # find it by examining the binary
    elf = ELF(cat)
    libs = elf.libraries()
    for lib in libs:
        if re.match(r"libc(\..*)?\.so(\..*)?$", lib):
            libc_name = lib
            break
    else:
        warnings.warn(
            f"Could not determine suitable library for testing. (Is {cat} statically linked?)"
        )
        pytest.skip()

    libc_src = _resolve_system_lib(libc_name)
    if libc_src is None:
        warnings.warn(f"Could not resovle {libc_name} for testing on this system.")
        pytest.skip()

    libc_dst = workdir / libc_name
    try:
        return _copy_elf(libc_src, libc_dst)
    except (OSError, ELFError) as e:
        warnings.warn("Could not copy suitable ELF library for testing.")
        pytest.skip(str(e))

    return libc_dst


def test_attempt_to_run_unauthorized_binary(cat: Path) -> None:
    """
    A copied binary should not work
    ===============================

    Only official binaries should be runnable, no matter how benign. This check
    simply copies a binary such as /bin/true to a temporary directory and
    executes it.

    See :kevlar-code:`200`.
    """

    with raises(PermissionError, "Was able to run an unauthorized binary"):
        subprocess.run([cat], stdin=subprocess.DEVNULL)


def test_attempt_to_preload_unauthorized_library(dynamic_cat: Path, libc: Path) -> None:
    """
    Users should not be able to inject into binaries using ``LD_PRELOAD``
    =====================================================================

    ``LD_PRELOAD`` allows injection of arbitrary code into a process.

    See :kevlar-code:`200`.
    """
    # Doesn't prevent running, just preloading the library.
    process = subprocess.Popen(
        ["cat"], env={"LD_PRELOAD": libc}, stdin=subprocess.PIPE, stdout=subprocess.PIPE
    )

    with process:
        # It's possible (and even likely) that on a single core VM we read
        # /proc/<pid>/maps before the linker/loader has had time to run! Do
        # basic interaction with 'cat' to ensure that it is up and running.
        assert process.stdin and process.stdout
        process.stdin.write(b"x")
        process.stdin.flush()
        process.stdout.read(1)

        with open(f"/proc/{process.pid}/maps", "r") as mapfile:
            maps = mapfile.read()

    libc = re.escape(str(libc))

    # When allowlisting or other LSM is enabled, the linker is often partially
    # successful at loading the .so into the address space. It isn't until it
    # tries to make the page executable that it fails, and that's all we really
    # care about. So look for executable permissions specifically, and not just
    # presence of the library name.
    assert not re.search(
        rf"r.xp\s.*{libc}$", maps, re.MULTILINE
    ), "Successfully injected non-authorized libc into ``cat``."


def test_attempt_to_intercept_system_library(dynamic_cat: Path, libc: Path) -> None:
    """
    Users should not be able to hijack authorized shared libraries
    ==============================================================

    ``LD_LIBRARY_PATH`` allows injecting arbitrary code into a process by
    impersonating a legitimate library.

    See :kevlar-code:`200`.
    """

    # Quick tests show this won't work with musl, since the loader and libc are
    # the same binary. We would need to choose another library/binary combo, which
    # comes with its own portability issues. So for now this is a TODO. The combo
    # LD_PRELOAD/LD_LIBRARY_PATH below should do it though.

    result = subprocess.run(
        ["cat"],
        env={"LD_LIBRARY_PATH": libc.parent},
        stderr=subprocess.PIPE,
        stdin=subprocess.DEVNULL,
    )
    # Return code comes from ld.so itself
    assert result.returncode == 127, "Able to run test binary with hijacked libc."


def test_attempt_to_use_env_var_combo(
    dynamic_cat: Path, libc: Path, workdir: Path
) -> None:
    """
    Users should not be able to inject code with environment variables
    ==================================================================

    ``LD_LIBRARY_PATH`` and ``LD_PRELOAD`` allow injecting arbitrary code into
    a process. This test uses them together.

    See :kevlar-code:`200`.
    """

    libz_name = "libz.so.1"
    libz_src = _resolve_system_lib(libz_name)
    if not libz_src:
        warnings.warn("Unable to find libz for testing.")
        pytest.skip()

    libz_dst = workdir / libz_name
    _copy_elf(libz_src, libz_dst)

    assert libc.parent == workdir
    result = subprocess.run(
        ["cat"],
        env={"LD_LIBRARY_PATH": str(workdir), "LD_PRELOAD": libz_name},
        stderr=subprocess.PIPE,
        stdin=subprocess.DEVNULL,
    )
    # Return code comes from ld.so itself
    assert result.returncode == 127, "Able to run test binary with hijacked libc."


def _atomic_overwrite(src: str, dst: str) -> None:
    dst_dir = os.path.dirname(dst)
    fd, staged_src = tempfile.mkstemp(dir=dst_dir)
    os.close(fd)
    shutil.copy2(src, staged_src)
    try:
        os.rename(staged_src, dst)
    except BaseException:
        try:
            os.unlink(staged_src)
        except OSError:
            pass
        raise


@pytest.mark.requires_root
def test_attempt_to_overwrite_system_binary() -> None:
    """
    Users should not be able to modify protected locations
    ======================================================

    See :kevlar-code:`200`.
    """
    # Can get different errors depending on what other defenses are enabled
    # (i.e., dm-verity)

    # Don't trust shutil.copy for two reasons:
    #   1) It does not guarantee an atomic operation, and we don't want to
    #   brick the system if we can't complete the write.
    #   2) On a busybox system (like Poky's core-image-minimal) attempting to
    #   naively copy to /bin/cat will produce "text file busy", because cat is
    #   the entire busybox binary.
    # Instead we will carefully do an atomic overwrite.

    cat_dst = shutil.which("cat")
    assert cat_dst

    try:
        _atomic_overwrite(cat_dst, cat_dst)
    except OSError as e:
        if e.errno in (errno.EPERM, errno.EACCES, errno.EROFS):
            # What we expect to see.
            return
        elif e.errno == errno.ENOSPC:
            msg = f"Could not safely/benignly overwrite {cat_dst}: {e}"
            warnings.warn(msg)
            pytest.skip(msg)
        else:
            raise  # An internal error we should try to fix.
    else:
        pytest.fail(f"Able to (benignly) overwrite {cat_dst}")


@full_version_only
def test_attempt_to_run_new_binary() -> None:
    """
    Users should not be able to drop and execute a crafted binary
    =============================================================

    See :kevlar-code:`200`.
    """
    ...
