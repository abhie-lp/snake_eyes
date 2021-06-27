"""Pages blueprints"""

from flask import Blueprint, render_template

page = Blueprint("page", __name__, template_folder="templates")


@page.get("/")
def home():
    """Home page of the application"""
    return render_template("page/home.html")


@page.get("/terms/")
def terms():
    """Terms and Conditions page"""
    return render_template("page/terms.html")


@page.get("/privacy/")
def privacy():
    """Privacy page"""
    return render_template("page/privacy.html")
