"""Views file for contacts"""

from flask import Blueprint, flash, redirect, request, url_for, render_template
from .forms import ContactForm

contact = Blueprint("contact", __name__, template_folder="templates")


@contact.route("/contact/", methods=["GET", "POST"])
def index():
    """Contact form page"""
    form = ContactForm()
    if form.validate_on_submit():
        # Importing here to avoid circular import
        from .task import send_contact_email
        send_contact_email.delay(request.form["email"], request.form["message"])
        flash("Thanks, expect a response shortly", "success")
        return redirect(url_for("contact.index"))
    return render_template("contact/index.html", form=form)
