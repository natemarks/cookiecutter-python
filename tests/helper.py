#!/usr/bin/env python3
"""Helper functions for pytest

Case is used to manage godlen files

the input and output dataclasses are used to drive tests
input:  input for a cookiecutter test run stored for a case as input.json
output: result object from the test helper function

"""
from dataclasses import dataclass
from glob import glob
import json
import logging
import os
from pathlib import Path
import sys
import pytest


def remove_suffix(value: str, suffix: str) -> str:
    """use slicing to be compatible with python before 3.8"""
    if value.endswith(suffix):
        return value[: -len(suffix)]
    return value


def strip_parent_path(value: str, parent_path: str) -> str:
    """remove parent path (prefix) from path
    given:
    /tmp/pytest-of-nmarks/pytest-24/test_cookiecutter_orange_0/cdk-my-project-name
    get:
    /cdk-my-project-name

    """
    return value[len(parent_path) :]


def get_logger(module_name: str) -> logging.Logger:
    """return standard logger
    usage:
    MODULE_LOGGER = get_logger(str(__name__))
    """
    my_logger = logging.getLogger(module_name)
    my_logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler(sys.stdout)

    formatter = logging.Formatter(
        "%(asctime)s - {%(name)s} - {%(filename)s:%(funcName)s:%(lineno)d} - "
        "%(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)

    my_logger.addHandler(console_handler)
    return my_logger


module_logger = get_logger(str(__name__))


class Case:
    """A test case

    This class is used by pytests to access the input and expected data
    files for a particular test case. The tests/data direcotry tree mirrors the tests/
    modules directory tree

    For parametrize (table) tests, a test module: tests/unit/policy/test_inline.py
    containing a test function: test_red_policy
    having a test case id: 111

    would have its input file:
    tests/data/tests/unit/policy/test_inline/test_red_policy/111/input.json
    and expected file:
    tests/data/tests/unit/policy/test_inline/test_red_policy/111/expected.json

    For tests that have a single test case (not table tests)
    would have its input file:
    tests/data/tests/unit/policy/test_inline/test_red_policy/input.json
    and expected file:
    tests/data/tests/unit/policy/test_inline/test_red_policy/expected.json

    """

    def __init__(self, request: pytest.FixtureRequest):
        self.request = request  # type: pytest.FixtureRequest
        self.test_dir = self.get_test_dir()
        self.data_dir = os.path.join(self.test_dir, "data")
        self.module_dir = remove_suffix(self.request.node.location[0], ".py")
        self.function_name = request.node.originalname
        try:
            self.case_name = request.node.callspec.id
        except AttributeError:
            self.case_name = ""

    def get_test_dir(self) -> str:
        """return the project tests directory path"""

        wrds = self.request.fspath.dirname.split(os.path.sep)
        while wrds[-1] != "tests":
            wrds.pop()
        return os.path.sep.join(wrds)

    def case_dir(self):
        """return the file path to the current case input file"""
        return os.path.join(
            self.data_dir, self.module_dir, self.function_name, self.case_name
        )

    def update_expected(self, data: str, file_name="expected.json"):
        """save expected/golden file"""
        os.makedirs(self.case_dir(), mode=0o755, exist_ok=True)
        file_path = os.path.join(self.case_dir(), file_name)
        with open(file_path, "w", encoding="utf-8") as outfile:
            outfile.write(json.dumps(data, indent=4))

    def input(self):
        """assuming the input file is JSON, return the data"""
        file_path = os.path.join(self.case_dir(), "input.json")
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def expected(self):
        """assuming the expected file is JSON, return the data"""
        file_path = os.path.join(self.case_dir(), "expected.json")
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data


@dataclass
class Input:
    """test input object used to drive test runs"""

    project_name: str


@dataclass
class Output:
    """test output object used to compare actual and expected output"""

    project_dir: str


# pylint: disable=too-few-public-methods
class Result:
    """test result"""

    def __init__(self, output_dir: Path):
        self.actual = {}
        self.output_dir = str(output_dir)
        self.set_project_dir()

    def set_project_dir(self):
        """set the project dir from the output dir"""
        res = glob(f"{self.output_dir}/*", recursive=False)
        if len(res) != 1:
            module_logger.error("expected one project dir. got: %i", len(res))
            return
        # strip the random temp dir parent path from the project dir

        self.actual["project_dir"] = strip_parent_path(
            str(res[0]), self.output_dir
        )
