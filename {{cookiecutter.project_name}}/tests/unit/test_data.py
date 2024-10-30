#!/usr/bin/env python3
"""data classes for stack/iam_xray.py

There is one App_Vpc per environment


"""
# pylint: disable=duplicate-code
import pytest
from tests.helper import Case
from {{cookiecutter.project_slug}}.data import return_data



@pytest.mark.unit
@pytest.mark.parametrize(
    "contents",
    [
        pytest.param("some data", id="some_data"),
        pytest.param("some data", id="some_other_data"),
    ],
)
def test_return_data(request, contents, update_golden):
    """test app_vpc stack"""

    case = Case(request)

    if update_golden:
        case.update_expected(return_data(contents))
    assert return_data(contents) == case.expected()
