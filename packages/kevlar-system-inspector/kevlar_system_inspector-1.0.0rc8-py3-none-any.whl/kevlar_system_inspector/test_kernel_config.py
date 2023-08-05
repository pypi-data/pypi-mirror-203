"""
--------------------------------------
Kernel Hardening: Kernel Configuration
--------------------------------------

The Linux kernel should be configured to minimize the potential attack surface
and provide exploit mitigations where possible.

"""

from collections import defaultdict
import errno
import subprocess
import warnings
import os
import stat
from typing import Optional, List, Tuple, Dict
import typing
from pathlib import Path

import pytest

from .decorators import merge_tests
from .utils.kconfig import KconfigSet, KernelVersion
from .utils.modules import run_kmod


KconfigCheckRow = Tuple[str, Optional[str], List[str], str]

KCONFIG_SIMPLE_CHECKS: List[KconfigCheckRow] = [
    # Each row:
    #   1. Config name
    #   1. String value, or NOT_PRESENT
    #   2. Dependencies. If they aren't all satisfied, this check is skipped.
    #   3. Description.
    #
    # The config to check can appear multiple times. This is useful if there
    # are OR conditions in the dependencies like (X86_64 || X86_PAE).
    (
        "CONFIG_BUG_ON_DATA_CORRUPTION",
        "y",
        [],
        "The parameter prevents data corruption from passing silently.",
    ),
    (
        "CONFIG_SLUB_DEBUG",
        "y",
        [],
        "This parameter enables kernel heap consistency checking.",
    ),
    (
        "CONFIG_DEBUG_WX",
        "y",
        [],
        "This parameter warns about insecure memory configuration.",
    ),
    (
        "CONFIG_SHUFFLE_PAGE_ALLOCATOR",
        "y",
        [],
        "This parameter mitigates heap spray attacks.",
    ),
    (
        "CONFIG_PAGE_POISONING",
        "y",
        [],
        "This parameter detects and mitigates use-after-free attacks.",
    ),
    typing.cast(
        KconfigCheckRow,
        pytest.param(
            "CONFIG_PAGE_POISONING_ZERO",
            "y",
            ["CONFIG_PAGE_POISONING=y"],
            """
        This parameter is a pragmatic option. CONFIG_PAGE_POISONING alone can
        cause noticeable performance degradation. While this option makes
        use-after-free conditions slightly more likely to go undetected
        compared to using CONFIG_PAGE_POISONING alone, the performance impact
        is not as great.
        """,
            marks=pytest.mark.skipif(
                KernelVersion.current() >= "5.11", reason="N/A on this kernel"
            ),
        ),
    ),
    (
        "CONFIG_HARDENED_USERCOPY",
        "y",
        [],
        """
        This parameter mitigates exploit techniques that trick the kernel into writing
        into incorrect memory regions.
        """,
    ),
    (
        "CONFIG_FORTIFY_SOURCE",
        "y",
        [],
        "This parameter hardens the kernel against buffer overflows.",
    ),
    (
        "CONFIG_SLAB_FREELIST_RANDOM",
        "y",
        [],
        "This parameter mitigates heap spray attacks",
    ),
    (
        "CONFIG_SLAB_FREELIST_HARDENED",
        "y",
        [],
        "This parameter mitigates heap corruption attacks",
    ),
    (
        "CONFIG_STACKPROTECTOR",
        "y",
        [],
        "This parameter hardens the kernel against stack-based buffer overflows.",
    ),
    (
        "CONFIG_STACKPROTECTOR_STRONG",
        "y",
        [],
        "This parameter hardens the kernel against stack-based buffer overflows.",
    ),
    ("CONFIG_COMPAT_BRK", None, [], "This parameter reduces kernel attack surface."),
    (
        "CONFIG_PROC_KCORE",
        None,
        [],
        "This parameter exposes kernel internal memory to userspace.",
    ),
    (
        "CONFIG_KPROBES",
        None,
        [],
        """
        This parameter exposes kernel internal memory to userspace. Allow
        modification of kernel execution by userspace.
        """,
    ),
    (
        "CONFIG_LEGACY_VSYSCALL_EMULATE",
        None,
        ["CONFIG_X86_64=y"],
        "This parameter reduces kernel attack surface.",
    ),
    (
        "CONFIG_LEGACY_VSYSCALL_XONLY",
        None,
        ["CONFIG_X86_64=y"],
        "This parameter reduces kernel attack surface.",
    ),
    (
        "CONFIG_LEGACY_VSYSCALL_NONE",
        "y",
        ["CONFIG_X86_64=y"],
        "This parameter reduces kernel attack surface.",
    ),
    (
        "CONFIG_MODIFY_LDT_SYSCALL",
        None,
        ["CONFIG_X86=y"],
        "This parameter reduces kernel attack surface.",
    ),
    # TODO: Track down how CONFIG_INET_DIAG got into our reccomended set.
    # There was a DoS CVE in 2.6...is it a rootkit thing?
    ("CONFIG_INET_DIAG", None, [], "Reduce kernel attack surface."),
    (
        "CONFIG_DEVMEM",
        None,
        [],
        """
        This disables /dev/mem, a serious attack surface that can provide userspace
        with raw access to memory if misconfigured.
        """,
    ),
    (
        "CONFIG_DEBUG_KERNEL",
        "y",
        [],
        "This parameter provides consistency checks that can detect and mitigate attacks.",
    ),
    (
        "CONFIG_SCHED_STACK_END_CHECK",
        "y",
        ["CONFIG_DEBUG_KERNEL=y"],
        "This parameter hardends the kernel against stack-based buffer overflows.",
    ),
    (
        "CONFIG_DEBUG_LIST",
        "y",
        ["CONFIG_DEBUG_KERNEL=y", "CONFIG_BUG_ON_DATA_CORRUPTION=y"],
        "This parameter hardens the kernel against buffer overruns.",
    ),
    (
        "CONFIG_DEBUG_SG",
        "y",
        ["CONFIG_DEBUG_KERNEL=y"],
        "This parameter hardens the kernel against driver data corruption.",
    ),
    (
        # TODO: This seems like a rootkit check. Verify.
        "CONFIG_DEBUG_NOTIFIERS",
        "y",
        ["CONFIG_DEBUG_KERNEL=y"],
        "This parameter can mitigate some rootkit hiding techniques.",
    ),
    (
        "CONFIG_DEBUG_CREDENTIALS",
        "y",
        ["CONFIG_DEBUG_KERNEL=y"],
        "This parameter mitigates privilege escalation attacks",
    ),
    ("CONFIG_RANDOMIZE_BASE", "y", [], "ASLR mitigates many attack vectors."),
    (
        "CONFIG_RANDOMIZE_MEMORY",
        "y",
        ["CONFIG_RANDOMIZE_BASE=y", "CONFIG_X86_64=y"],
        "ASLR mitigates many attack vectors.",
    ),
    (
        "CONFIG_STRICT_KERNEL_RWX",
        "y",
        [],
        "This parameter is a standard security practice to prevent read-write-execute memory.",
    ),
    (
        "CONFIG_STRICT_MODULE_RWX",
        "y",
        [],
        "This parameter is a standard security practice to prevent read-write-execute memory.",
    ),
    (
        "CONFIG_PAGE_TABLE_ISOLATION",
        "y",
        ["CONFIG_X86_64=y"],
        "This parameter mitigates hardware side channels",
    ),
    (
        "CONFIG_PAGE_TABLE_ISOLATION",
        "y",
        ["CONFIG_X86_PAE=y"],
        "This parameter mitigates hardware side channels",
    ),
    (
        "CONFIG_RETPOLINE",
        "y",
        ["CONFIG_X86=y"],
        "This parameter mitigates speculative execution attacks (Spectre/Meltdown).",
    ),
]


def _make_kconfig_ids() -> List[str]:
    seen: Dict[str, int] = defaultdict(int)
    ids = []
    for row in KCONFIG_SIMPLE_CHECKS:
        row = getattr(row, "values", row)  # normalize pytest.param entries
        name = row[0]
        id_val = name
        suffix = seen[name]
        if suffix:
            id_val = f"{id_val}-{suffix}"
        seen[name] += 1
        ids.append(id_val)
    return ids


KCONFIG_SIMPLE_IDS = _make_kconfig_ids()


@pytest.mark.parametrize(
    ["name", "value", "dependencies", "description"],
    KCONFIG_SIMPLE_CHECKS,
    ids=KCONFIG_SIMPLE_IDS,
)
def test_configuration_items(
    kconfig: KconfigSet,
    name: str,
    value: Optional[str],
    dependencies: List[str],
    description: Optional[str],
) -> None:
    """
    Kernel config: {{ name }}
    =============================================

    There are many knobs to turn when configuring the Linux kernel for your
    needs. Many of these knobs provide extra security or have subtle security
    implications.

    {{description | dedent}}

    See :kevlar-code:`300`.
    """

    if not value:
        config = f"# {name} is not set"
        message = f"{name} should not be configured"
    else:
        config = f"{name}={value}"
        message = f"{name} should be set"

    for dep in dependencies:
        if dep not in kconfig:
            pytest.skip(f"Dependency {dep} not met for {config}")

    assert config in kconfig, message


@pytest.mark.parametrize(
    ["flag", "reason"],
    [("F", "SLAB sanity checks"), ("Z", "SLAB red zoning")],
    ids=["F", "Z"],
)
@merge_tests
def test_slub_debug_params(
    flag: str, reason: str, kernel_cmdline: List[str], kconfig: KconfigSet
) -> None:
    """
    Enable kernel heap checks
    =========================

    Kernel heap checking must be enabled both via config and via command line.

    See :kevlar-code:`300`.
    """

    if "CONFIG_SLUB_DEBUG=y" not in kconfig:
        pytest.skip("Prerequisites not met")

    for arg in kernel_cmdline:
        if arg.startswith("slub_debug="):
            val = arg.split("=", 1)[1]
            assert (
                flag in val
            ), f"Kernel parameter ``slub_debug=`` missing parameter {flag}: {reason}"
            break
    else:
        pytest.fail("Kernel parameter ``slub_debug=`` missing")


def test_proc_kcore_is_not_present() -> None:
    """
    ``/proc/kcore`` should not be present
    =====================================

    Linux provides a core file of the running system, which allows a user with
    root access to view all kernel pointers and secrets, paving the way for
    further kernel exploits.

    See :kevlar-code:`300`.
    """

    assert not os.path.exists("/proc/kcore"), "/proc/kcore attack surface detected"


DeviceVals = Tuple[int, int, int]

DEVICE_TESTS: List[Tuple[str, DeviceVals, Optional[str]]] = [
    # 1. Device cannonical path
    # 2. Device number (type, maj, min)
    # 3. Module to load if any
    ("/dev/mem", (stat.S_IFCHR, 1, 1), None),
    ("/dev/kmem", (stat.S_IFCHR, 1, 2), None),
]

DEVICE_TEST_IDS: List[str] = [row[0] for row in DEVICE_TESTS]


@pytest.mark.parametrize(
    ["device_path", "device", "module"], DEVICE_TESTS, ids=DEVICE_TEST_IDS
)
def test_devices_not_enabled_via_standard_path(
    device_path: str, device: DeviceVals, module: Optional[str]
) -> None:
    """
    Device path ``{{device_path}}`` should not be present
    ==============================================================

    Device files, such as ``{{device_path}}`` are an unnecessary attack surface
    that can be disabled.

    See :kevlar-code:`300`.
    """

    try:
        info = os.stat(device_path)
    except FileNotFoundError:
        return

    xlate = {stat.S_IFBLK: "b", stat.S_IFCHR: "c"}

    found_type = xlate.get(stat.S_IFMT(info.st_mode), "")
    if found_type not in ("c", "b"):
        warnings.warn(f"Path ``{device_path}`` is not a device file.")
        return

    found_devnum = (found_type, os.major(info.st_rdev), os.minor(info.st_rdev))
    expected_devnum = (xlate[device[0]], device[1], device[2])
    if found_devnum != expected_devnum:
        warnings.warn(
            f"Path ``{device_path}`` points to an unexpected device "
            f"{found_devnum} instead of {expected_devnum}"
        )
        return

    pytest.fail(f"Device ``{device_path}`` present on this system")


@pytest.mark.parametrize(
    ["device_path", "device", "module"], DEVICE_TESTS, ids=DEVICE_TEST_IDS
)
def test_devices_via_nonstandard_path(
    device_path: str, device: Tuple[int, int, int], module: Optional[str], workdir: Path
) -> None:
    """
    ``{{device_path}}`` should be inaccessible even through indirect means
    ============================================================================

    Deleting a device file path is not enough to render a device inaccessible.
    It needs to be removed from the kernel entirely. This test attempts to use
    ``mknod()`` to access a device without using it's standard file path.

    See :kevlar-code:`300`.
    """

    new_path = workdir / "device"

    if module:
        result = run_kmod(["modprobe", module], stderr=subprocess.DEVNULL)
        assert result.returncode == 0, f"Could not load module {module}"

    devtype, major, minor = device
    devnum = os.makedev(major, minor)

    try:
        os.mknod(new_path, devtype | 0o600, devnum)
    except OSError as e:
        pytest.fail(f"Could not create device file for further testing: {e}")

    try:
        try:
            with open(new_path, "rb"):
                pass
        except OSError as e:
            assert e.errno == errno.ENXIO, (
                f"Expected ENXIO, got {e}. Note that this should be completely absent,"
                " not merely restricted."
            )
        else:
            pytest.fail(f"{device_path} present via mknod")
    finally:
        try:
            os.unlink(new_path)
        except OSError:
            pass
