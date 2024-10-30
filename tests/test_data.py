""" test module: {{cookiecutter.project_slug}}/data.py"""
import pathlib
import pytest

from cookiecutter.main import cookiecutter
from tests.helper import Case, Result, remove_suffix, strip_parent_path

TEMPLATE_DIRECTORY = str(pathlib.Path(__file__).parent.parent)


def test_remove_suffix():
    """test remove_suffix"""
    assert remove_suffix("ggg.py", ".py") == "ggg"


def test_strip_parent_path():
    """test strip_parent_path"""
    tmp = "/tmp/pytest-of-nmarks/pytest-24/test_cookiecutter_orange_0/cdk-my-project-name"
    assert (
        strip_parent_path(
            tmp, "/tmp/pytest-of-nmarks/pytest-24/test_cookiecutter_orange_0"
        )
        == "/cdk-my-project-name"
    )


@pytest.mark.unit
@pytest.mark.parametrize(
    "",
    [
        pytest.param(id="orange"),
    ],
)
def test_cookiecutter(tmp_path, request, update_golden):
    """test cookiecutter template"""
    case = Case(request)

    cookiecutter(
        TEMPLATE_DIRECTORY,
        output_dir=str(tmp_path),
        no_input=True,
        extra_context=case.input(),
    )
    res = Result(output_dir=tmp_path)

    if update_golden:
        case.update_expected(res.actual)
    assert res.actual == case.expected()
