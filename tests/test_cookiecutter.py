""" test module: {{cookiecutter.project_slug}}/data.py"""
from dataclasses import dataclass, asdict
from pathlib import Path
import pytest

from cookiecutter.main import cookiecutter

TEMPLATE_DIRECTORY = str(Path(__file__).parent.parent)


@dataclass
class CaseInput:
    """case input data"""

    full_name: str
    email: str
    github_username: str
    project_name: str
    project_short_description: str


DEFAULT_INPUT = CaseInput(
    full_name="Nate Marks",
    email="npmarks@gmail.com",
    github_username="natemarks",
    project_name="default dino",
    project_short_description="default desc",
)


@pytest.mark.unit
@pytest.mark.parametrize(
    "case_input",
    [
        pytest.param(DEFAULT_INPUT, id="default"),
    ],
)
def test_run_cookiecutter(tmpdir, case_input):
    """test cookiecutter"""
    # Convert tmpdir to a string path to use with cookiecutter output_dir
    output_dir = str(tmpdir)
    result_path = cookiecutter(
        template=TEMPLATE_DIRECTORY,
        output_dir=str(tmpdir),
        extra_context=asdict(case_input),
        no_input=True,
    )

    # Validate that the result path exists in the temporary directory
    generated_project_path = Path(result_path)
    assert generated_project_path.exists()
    assert generated_project_path.parent == Path(output_dir)
