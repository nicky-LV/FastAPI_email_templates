import smtplib

from jinja2 import Environment, PackageLoader, select_autoescape

from typing import List, Optional
from pydantic import BaseModel

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailModel(BaseModel):
    recipients: List[str]


class Mail:
    def __init__(self, username: str, password: str, smtp_host: str, smtp_port: int = 433, tls: bool = True):
        # SMTP details
        self.username = username
        self.password = password
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.tls = tls

        # Load Jinja2 environment for discovering templates
        self.env = Environment(
            loader=PackageLoader("yourapp"),
            autoescape=select_autoescape()
        )

    def send_email_template(self, recipients: List[str], subject, email_path: str, context: dict):
        """
        Sends email jinja2 template
        :param recipients: List[str] of recipient email addresses.
        :param subject: str - Subject of email.
        :param email_path: str - Path of email template (.html)
        :param context: dict - Context to pass into jinja2 template
        :return:
        """

        # msg has the multipart MIME-type, as the email may contain data of different MIME types.
        # For example, html, text, images, etc.
        msg = MIMEMultipart()

        # Search for template
        html_template = self.env.get_template(email_path)

        # Populate template with context
        populated_html_template = html_template.render(**context)

        # Set subject and recipients
        msg['Subject'] = subject
        msg['From'] = self.username
        msg['To'] = ",".join(recipients)

        # Attach populated jinja2 template
        msg.attach(MIMEText(populated_html_template))

        # Connect to SMTP server
        server = smtplib.SMTP(host=self.smtp_host, port=self.smtp_port)
        server.starttls()
        server.login(user=self.username, password=self.password)
        server.send_message(msg)
