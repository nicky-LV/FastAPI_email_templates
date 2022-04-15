import os
import smtplib


def test_smtp_server_connection():
    """ Connect to SMTP server. SMTP_HOST and SMTP_PORT must be provided as environment variables. """
    server = smtplib.SMTP(host=os.environ['SMTP_HOST'], port=int(os.environ['SMTP_PORT']))