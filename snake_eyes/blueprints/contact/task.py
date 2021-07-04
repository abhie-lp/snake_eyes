"""Celery tasks for contacts blueprint"""

from flask import current_app

from snake_eyes.app import create_celery_app
from snake_eyes.utils.email import send_mail

celery = create_celery_app()


@celery.task()
def send_contact_email(email: str, message: str):
    """Task to send contact email from contact form"""
    send_mail(
        "[Snake Eyes] Contact", current_app.config["MAIL_USERNAME"],
        email, "contact/mail.txt",
        {"email": email, "message": message}
    )
