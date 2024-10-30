""" test module: {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}_stack.py"""
import aws_cdk as core
from aws_cdk import assertions
import pytest
from {{cookiecutter.project_slug}}.{{cookiecutter.project_slug}}_stack import ExampleStack


@pytest.mark.deployment
def test_sqs_queue_created():
    """meaningless test to verify pytest"""
    app = core.App()
    stack = ExampleStack(app, "deleteme-cdk")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties(
        "AWS::SQS::Queue", {"VisibilityTimeout": 300}
    )


@pytest.mark.deployment
def test_sns_topic_created():
    """meaningless test to verify pytest"""
    app = core.App()
    stack = ExampleStack(app, "deleteme-cdk")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
