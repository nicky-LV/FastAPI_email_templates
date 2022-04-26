import os
import smtplib

import pytest
import json
from jinja2 import Environment, PackageLoader, select_autoescape
from fastapi_email_templates import Mail
from typing import List


# Fixtures for env variables, as pytest does not have access to our os env variables.
@pytest.fixture
def smtp_host():
    return os.environ['SMTP_HOST']


@pytest.fixture
def email_username():
    return os.environ['EMAIL_USERNAME']


@pytest.fixture
def email_password():
    return os.environ['EMAIL_PASSWORD']


@pytest.fixture
def smtp_port():
    return int(os.environ['SMTP_PORT'])


@pytest.fixture
def email_engine(email_username, email_password, smtp_host):
    engine: Mail = Mail(username=email_username, password=email_password,
                             smtp_host=smtp_host)
    return engine


def test_template_discovery():
    """ Create a test template within the templates directory and load it. """
    if not os.path.exists("templates/test.html"):
        os.mknod("templates/test.html")

    # Setup jinja2 environment
    env = Environment(
        loader=PackageLoader("main"),
        autoescape=select_autoescape()
    )

    template = env.get_template("test.html")

    if not template:
        raise FileNotFoundError("Template could not be found.")


def test_context_population():
    context = {
        "title": "Test",
        "body": "Test"
    }

    if not os.path.exists("templates/test.html"):
        os.mknod("templates/test.html")

    # Setup jinja2 environment
    env = Environment(
        loader=PackageLoader("main"),
        autoescape=select_autoescape()
    )

    template = env.get_template("test.html")
    populated_template = template.render(**context)

    assert populated_template is not template

    if not template:
        raise FileNotFoundError("Template could not be found.")


def test_smtp_server_connection(smtp_host, smtp_port):
    """ Connect to SMTP server. SMTP_HOST and SMTP_PORT must be provided as environment variables. """
    server = smtplib.SMTP(host=smtp_host, port=int(smtp_port))
    assert server is not None


def test_send_email_with_context(email_engine, email_username, email_password, smtp_host):
    """ Test sending populated email template"""
    receiver_email: List[str] = ["nickysitnikovs18@gmail.com"]
    context = {
        "title": "Test",
        "body": "Body"
    }

    email_engine.send_email_template(recipients=receiver_email, subject="Test", email_path="test.html",
                                    context=context)


def test_send_email(email_engine, email_username, email_password, smtp_host):
    """ Test sending populated email template"""
    receiver_email: List[str] = ["nickysitnikovs18@gmail.com"]

    email_engine.send_email_template(recipients=receiver_email, subject="Test", email_path="test_no_context.html")


def test_send_carbon_copy(email_engine, email_username, email_password, smtp_host):
    """ Test sending email template with CCs and BCCs"""
    receiver_email: List[str] = ["randomemailaddress@randomdomain.com"]
    cc: List[str] = ["nickysitnikovs18@gmail.com"]
    bcc: List[str] = ["nickysitnikovs18@gmail.com"]

    context: dict = {
        "title": "Test",
        "cc": cc,
        "bcc": bcc
    }

    email_engine.send_email_template(recipients=receiver_email, cc=cc, bcc=bcc, email_path="cc_test.html",
                                     context=context, subject="test_cc")