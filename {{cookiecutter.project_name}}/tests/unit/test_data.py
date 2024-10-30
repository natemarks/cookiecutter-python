""" test module: {{cookiecutter.project_slug}}/data.py"""
import pytest


from {{cookiecutter.project_slug}}.data import RDSSecret


@pytest.mark.unit
def test_data():
    """meaningless test to verify pytest"""
    result = RDSSecret(
        username="my_user",
        password="my_password",
        dbInstanceIdentifier="cts-cts-staging",
        host="cts-cts-staging.cwi3fcl24jgg.us-east-1.rds.amazonaws.com",
    )
    assert result.engine == "postgres"
