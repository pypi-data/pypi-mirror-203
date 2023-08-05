"""
-------------------------------
Application Sandboxing: Systemd
-------------------------------

Systemd can restrict what operations services can perform using per-service
system call filtering. This can mitigate what an exploitable program can be
made to do and can mitigate follow-on exploits such as local privilege
escalations.
"""

import subprocess
from typing import Dict

import pytest

from .utils.systemd import (
    does_service_exist,
    get_service_properties,
    is_system_using_systemd,
)

# Skip on non-systemd systems
pytestmark = pytest.mark.skipif(
    not is_system_using_systemd(), reason="Not using systemd on this system"
)


def test_systemd_has_seccomp_enabled() -> None:
    """
    Systemd should be built with system call filtering support
    ==========================================================

    Systemd system call filtering is a compile-time option that should be
    enabled.

    See :kevlar-code:`700`.
    """

    result = subprocess.run(
        ["systemctl", "--version"], text=True, stdout=subprocess.PIPE
    )
    assert "+SECCOMP" in result.stdout, "Systemd was not compiled with seccomp support"


BASIC_SERVICE_LIST = [
    "systemd-resolved",
    "systemd-resolved2",
]


@pytest.fixture(scope="session", params=BASIC_SERVICE_LIST)
def basic_service(request: pytest.FixtureRequest) -> Dict[str, str]:
    service = request.param

    if not does_service_exist(service):
        pytest.skip("Service not installed")
    return get_service_properties(service)


def test_has_filter_installed(basic_service: Dict[str, str]) -> None:
    """
    {{fixture_names["basic_service"]}} should have a system call filter installed
    =============================================================================

    This service has a system call filter available. It should be activated.

    See :kevlar-code:`700`.
    """

    # Empty and ~ are equivalent.
    assert (
        basic_service.get("SystemCallFilter", "~") != "~"
    ), "No system call filter installed"


def test_native_only(basic_service: Dict[str, str]) -> None:
    """
    {{fixture_names["basic_service"]}} should only allow native system calls
    ========================================================================

    Some architectures support multiple types of system calls. Most commonly,
    64-bit systems will support a secondary set of system calls for 32-bit
    processes. Allowing these alternate system calls can reduce the
    effectiveness of a system call filter and should be prohibited for programs
    that have system call filtering enabled.

    See :kevlar-code:`700`.
    """

    assert (
        basic_service.get("SystemCallArchitectures") == "native"
    ), "System call filter allows non-native architectures"
