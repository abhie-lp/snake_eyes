"""Email related functions"""

from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import current_app as app, render_template


def send_mail(
        subject: str, to: str, via: str, template: str, ctx: dict
) -> None:
    """Send mail to the user"""
    msg = MIMEMultipart("alternative")
    msg["To"] = to
    msg["From"] = via
    msg["Subject"] = subject
    msg.preamble = "Your browser does not support mail format."
    content = MIMEText(render_template(template, **ctx),
                       "html" if template.rsplit(".", 1)[1] == "html" else "plain")
    msg.attach(content)

    with SMTP_SSL(app.config["MAIL_SERVER"]) as smtp:
        smtp.login(app.config["MAIL_USERNAME"], app.config["MAIL_PASSWORD"])
        smtp.send_message(msg)
