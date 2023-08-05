"""
------------------------------------
Network Hardening: DNS Configuration
------------------------------------

While the Domain Name Service (DNS) underlies all network communication, it is
not a secure protocol. Failing to secure a device's use of DNS can allow
malicious actors to arbitrarily spoof websites and will leak sensitive metadata
about websites visited.
"""

import ipaddress
import re
import subprocess
from typing import List

import pytest


def _run_resolvectl(*params: str) -> str:
    try:
        result = subprocess.run(
            ["resolvectl", *params], text=True, stdout=subprocess.PIPE, check=True
        )
    except (OSError, subprocess.CalledProcessError):
        pytest.fail(
            "systemd-resolved is not installed or not running to provide secure DNS."
        )

    return result.stdout


@pytest.fixture(scope="session")
def links_with_dns() -> List[str]:
    # This is not parametrized so we can better handle errors with resolvectl
    # or features not enabled at compile time. Otherwise we'd have a ton of
    # repeated "feature not supported" messages.
    links = []

    key_match = re.compile(r".*? \(([^)]+)\):")
    try:
        data = _run_resolvectl("dns")
    except (OSError, subprocess.CalledProcessError):
        pytest.fail("Cannot run resolvectl. Is resolved running?")

    for line in data.splitlines():
        m = key_match.match(line)
        if not m:
            continue
        name = m.group(1)
        servers = line[m.end() :].strip()
        if not servers:
            continue

        links.append(name)
    return links


def check_links_for_feature(name: str, feature: str, links: List[str]) -> None:
    missing = []

    for link in links:
        try:
            data = _run_resolvectl(feature, link)
            _, value = data.rsplit(":", 1)
        except IndexError:
            pytest.fail("Malformed output from resolvectl")
        except subprocess.CalledProcessError:
            pytest.fail(f"{name} is not enabled in ``resolved``")

        value = value.strip().lower()
        if value != "yes":
            missing.append(link)

    missing = ", ".join(missing)
    assert not missing, f"{name} should be enabled on interface(s): {missing}"


def test_dnssec_is_enabled(links_with_dns: List[str]) -> None:
    """
    DNSSEC enforcement should be enabled
    ====================================

    DNSSEC is a standard that protects DNS lookups from spoofing or cache
    poisoning attacks. Without DNSSEC, there is no guarantee that the IP
    address the DNS server returned has not been maliciously altered. DNSSEC
    must be enabled on the DNS server, but it does no good if the client is not
    set up to verify it. When possible, the DNS client should *require* DNSSEC.

    See :kevlar-code:`600`.
    """

    check_links_for_feature("DNSSEC", "dnssec", links_with_dns)


def test_dns_over_tls_is_enabled(links_with_dns: List[str]) -> None:
    """
    DNS-over-TLS should be enabled
    ==============================

    DNS is vulnerable to eavesdropping and traffic modification. This is a
    serious side channel that can reveal to third parties what sites were
    visited, even if the connections are encrypted. By encrypting DNS using
    standard TLS, third parties cannot view or alter domain name lookups.

    See :kevlar-code:`600`.
    """

    check_links_for_feature("DNS-over-TLS", "dnsovertls", links_with_dns)


def test_resolv_conf_uses_loopback() -> None:
    """
    ``/etc/resolv.conf`` should not query DNS servers directly
    ==========================================================

    When ``/etc/resolv.conf`` has remote DNS server listed, most applications
    will use the system libc's rudimentary DNS client functionality to query
    them directly. There are no libc DNS implementations that implement any
    sort of security, such as DNS-over-TLS or DNSSEC. Instead,
    ``/etc/resolv.conf`` should be configured to query a more sophisticated
    resolver via a loopback address.

    See :kevlar-code:`600`.
    """

    try:
        with open("/etc/resolv.conf") as fp:
            for line in fp:
                fields = line.split()
                if len(fields) == 2 and fields[0] == "nameserver":
                    try:
                        addr = ipaddress.ip_address(fields[1])
                    except ValueError:
                        continue

                    assert (
                        addr.is_loopback
                    ), f"/etc/resolv.conf is configured to query {addr} directly. "
    except OSError as e:
        pytest.fail(f"Could not check /etc/resolv.conf for errors: {e}")
        return
