# FastAPI email templates

(under development)

## Purpose:

FastAPI_email_templates is a package which allows you to send jinja2 template emails simply.



## Instructions:

This will show you how to send a jinja2 template email.



1. Initialize Mail object, providing the arguments:
   
   - username: str - Your email username (e.g. test@test.com).
   
   - password: str - Your email password.
   
   - smtp_host: str - SMTP host.
   
   - smtp_port: int - SMTP port.

```python
from fastapi_email_templates.main import Mail


mail = Mail(username=<email_username>, password=<email_password>, smtp_host=<smtp_host>, smtp_port=<smtp_port>)

```

To send a template, make sure that the `.html` template is found in the `templates` directory. This is where the `Mail` class will look for templates.



2. Send an email with the `send_email_template` method, providing the arguments:
   
   - recipients: List[str]
   
   - subject: str
   
   - email_path: str - The template name.
   
   - context: Optional[dict] - Context to populate template with.
   
   - cc : Optional[List[str]] - Cc'd recipients.
   
   - bcc: Optional[List[str]] - Bcc'd recipients.

```python
mail.send_email_template(recipients, subject, "test.html", context)
```

and you have sent your email template! 
