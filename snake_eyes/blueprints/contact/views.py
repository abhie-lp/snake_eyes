"""Views file for contacts"""

from decouple import config
from flask import Blueprint, flash, redirect, request, url_for, render_template

from snake_eyes.utils.email import send_mail
from .forms import ContactForm

contact = Blueprint("contact", __name__, template_folder="templates")


@contact.route("/contact/", methods=["GET", "POST"])
def index():
    """Contact form page"""
    form = ContactForm()
    if form.validate_on_submit():
        send_mail(
            "[Snake Eyes] Contact", config("MAIL_USERNAME"),
            request.form["email"], "contact/mail.txt",
            {"email": request.form["email"], "message": request.form["message"]}
        )
        flash("Thanks, expect a response shortly", "success")
        return redirect(url_for("contact.index"))
    return render_template("contact/index.html", form=form)
