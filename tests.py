import os
from jinja2 import Environment, PackageLoader, select_autoescape
import smtplib


def test_template_discovery():
    """ Create a test template within the templates directory and load it. """
    if not os.path.exists("./templates/test.html"):
        os.mknod("./templates/test.html")

    # Setup jinja2 environment
    env = Environment(
        loader=PackageLoader("main"),
        autoescape=select_autoescape()
    )

    template = env.get_template("test.html")

    if not template:
        raise FileNotFoundError("Template could not be found.")


def test_smtp_server_connection():
    """ Connect to SMTP server. SMTP_HOST and SMTP_PORT must be provided as environment variables. """
    server = smtplib.SMTP(host=os.environ['SMTP_HOST'], port=int(os.environ['SMTP_PORT']))