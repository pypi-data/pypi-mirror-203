"""
Plugin to print progress as we go
"""

import textwrap
from typing import List, Dict, Generator, Iterable, Optional, Tuple
from types import ModuleType
import warnings
from dataclasses import dataclass

import docutils.core
import docutils.nodes
import docutils.utils
from docutils.parsers.rst import roles, states
from jinja2 import Environment, PackageLoader, select_autoescape

# Below, we do type annotations for pytest things in quotes, because some of
# them aren't publicly exposed until version 7.0. That only matters for mypy
# checking, so putting them in quotes means Python won't care about them at
# runtime.
import pytest

from .version import is_full_version
from .sysinfo import get_system_info
from .version import VERSION


JINJA_ENV = Environment(
    loader=PackageLoader(__package__),
    autoescape=select_autoescape(),
)
JINJA_ENV.filters["dedent"] = textwrap.dedent


# Code to register a custom role for our test documentation:
#
#   :kevlar-code:`300` which generates a link to our webpage and inserts
#   metadata into the document.
def kevlar_code_ref_role(
    role: str,
    rawtext: str,
    text: str,
    lineno: int,
    inliner: states.Inliner,
    options: Optional[Dict[str, str]] = None,
    content: Optional[List[str]] = None,
) -> Tuple[List[docutils.nodes.Node], List[str]]:
    text = docutils.utils.unescape(text)
    code = f"SL-{text}"
    uri = f"https://starlab.io/sl-{text}"

    try:
        options = roles.normalized_role_options(options)
    except AttributeError:
        # Old Yocto versions.
        options = {} if options is None else options

    ref = docutils.nodes.reference(rawtext, code, refuri=uri, **options)
    nodes = [ref]

    # Metadata is largely so we can have a QA check that all tests are tagged
    # with at least one code.
    try:
        meta = docutils.nodes.meta()
        meta["name"] = "kevlar-code"
        meta["content"] = code
        meta["uri"] = uri
        nodes.append(meta)
    except AttributeError:
        # Old Yocto versions. We won't run unit tests from there.
        pass

    return nodes, []


roles.register_local_role("kevlar-code", kevlar_code_ref_role)


@dataclass(frozen=True)
class FailureCause:
    is_internal: bool
    message: str

    @classmethod
    def from_pytest(cls, pytest_report: "pytest.TestReport") -> "FailureCause":
        try:
            message = str(pytest_report.longrepr.reprcrash.message)  # type: ignore
        except AttributeError:
            message = str(pytest_report.longrepr)
            is_internal = True
        else:
            if message.startswith("AssertionError"):
                is_internal = False
                message = message.split(":", 1)[1].strip()
                lines = message.splitlines()
                while len(lines) > 1:
                    last_line = lines.pop()
                    if last_line.startswith("assert "):
                        break
                first = lines[0]
                bulk = textwrap.dedent("\n".join(lines[1:]))
                message = "\n".join([first, bulk])
            elif message.startswith("Failed: "):
                is_internal = False
                message = message.split(":", 1)[1].strip()
            else:
                is_internal = True
                message = str(pytest_report.longrepr)  # full crash, if available
        return cls(message=message, is_internal=is_internal)


class TestFailure:
    def __init__(self, item: "pytest.Function"):
        self.item = item
        self.documentation = item.function.__doc__
        self.tags = {mark.name for mark in item.iter_markers()}
        if self.documentation:
            vars = item.function.__globals__.copy()
            try:
                vars["fixture_names"] = item.callspec.params
                vars.update(item.callspec.params)
            except AttributeError:
                pass
            vars.update(item.funcargs)
            template = JINJA_ENV.from_string(textwrap.dedent(self.documentation))
            self.documentation = template.render(vars)
        self.causes: Dict[
            FailureCause, int
        ] = {}  # set-like, to preserve insertion order

    def add_report(self, pytest_report: "pytest.TestReport") -> None:
        self.causes[FailureCause.from_pytest(pytest_report)] = 1


class TestModule:
    """
    Holds the module documentation, and lets us group in a dict by module.
    """

    def __init__(self, item: "pytest.Function"):
        self.module = item.module
        self.documentation = item.module.__doc__
        self.tags = {mark.name for mark in item.iter_markers()}
        if self.documentation:
            template = JINJA_ENV.from_string(textwrap.dedent(self.documentation))
            self.documentation = template.render(item.module.__dict__)

        # Failures, grouped by base (non-parametrized) nodeid
        self.failures: Dict[str, TestFailure] = {}


class TestReport:
    """
    The final test report. Contains the human-readable document parsed from
    restructuredtext, suitable for display in any other format.
    """

    def __init__(self) -> None:
        # Failures, grouped by module, then by base (non-parametrized) nodeid
        self.modules: Dict[ModuleType, TestModule] = {}

        # A set, but use a dict to preserve insertion order
        # Only the first warning, when there are duplicates.
        self._warnings: Dict[object, warnings.WarningMessage] = {}

        # Will be filled out at the end
        self.document = docutils.utils.new_document("<pending>")

    @property
    def any_failures(self) -> bool:
        return any(m.failures for m in self.modules.values())

    @property
    def failure_count(self) -> int:
        return sum(len(m.failures) for m in self.modules.values())

    def add_item(
        self,
        item: "pytest.Function",
        pytest_report: Optional["pytest.TestReport"] = None,
    ) -> None:
        if getattr(item.function, "merge_tests", False):
            base_nodeid = item.nodeid.rsplit("[", 1)[0]
        else:
            base_nodeid = item.nodeid
        module_failures = self.modules.setdefault(item.module, TestModule(item))
        failure = module_failures.failures.setdefault(base_nodeid, TestFailure(item))
        if pytest_report is not None:
            failure.add_report(pytest_report)

    def add_warning(self, warning: warnings.WarningMessage) -> None:
        key = (str(warning.message), warning.category, warning.filename, warning.lineno)
        self._warnings.setdefault(key, warning)  # only keep the first

    @property
    def warnings(self) -> Iterable[warnings.WarningMessage]:
        return self._warnings.values()

    def finish(self) -> None:
        self._make_document()

    def _make_document(self) -> None:
        report_template = JINJA_ENV.get_template("report.rst")
        src = report_template.render(
            report=self,
            is_full_version=is_full_version(),
            system_info=get_system_info(),
            inspector_version=VERSION,
        )
        self.document_source = src
        self.document = docutils.core.publish_doctree(src)


class KevlarHooks:
    @pytest.hookspec()
    def pytest_kevlar_report(self, report: TestReport) -> None:
        pass


class KevlarReporter:
    """Collect pytest output into a report object"""

    def __init__(self) -> None:
        self.report = TestReport()

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(
        self, item: "pytest.Function", call: "pytest.CallInfo[None]"
    ) -> Generator[None, "pytest.TestReport", None]:
        outcome = yield
        pytest_report = outcome.get_result()

        if not pytest_report.failed:
            return

        self.report.add_item(item, pytest_report)

    def pytest_addhooks(self, pluginmanager: "pytest.PytestPluginManager") -> None:
        pluginmanager.add_hookspecs(KevlarHooks)

    def pytest_sessionfinish(self, session: "pytest.Session") -> None:
        self.report.finish()
        session.config.hook.pytest_kevlar_report(report=self.report)

    def pytest_warning_recorded(self, warning_message: warnings.WarningMessage) -> None:
        self.report.add_warning(warning_message)
