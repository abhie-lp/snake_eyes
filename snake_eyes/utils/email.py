"""Email related functions"""

from smtplib import SMTP_SSL
from email.message import EmailMessage

from flask import current_app


def send_mail(subject: str, to: str, via: str, content: str) -> None:
    """Send mail to the user"""
    msg = EmailMessage()
    msg["To"] = to
    msg["From"] = via
    msg["Subject"] = subject
    msg.set_content(content)

    with SMTP_SSL(current_app.config["MAIL_SERVER"]) as smtp:
        print(current_app.config["MAIL_USERNAME"],
              current_app.config["MAIL_PASSWORD"],
              current_app.config["MAIL_SERVER"])
        smtp.login(current_app.config["MAIL_USERNAME"],
                   current_app.config["MAIL_PASSWORD"])
        smtp.send_message(msg)
