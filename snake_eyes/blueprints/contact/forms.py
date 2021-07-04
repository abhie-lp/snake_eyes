"""Forms related to contacts"""

from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms_components import EmailField
from wtforms.validators import DataRequired, Length


class ContactForm(FlaskForm):
    """Contact form to enter email and message"""
    email = EmailField("What's your email address", [DataRequired(), Length(3, 254)])
    message = TextAreaField("What's your question or issue?", [DataRequired(), Length(1, 8192)])
