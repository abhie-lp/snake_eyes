"""Pytest config file"""

import pytest
from flask import Flask

from snake_eyes.app import create_app


@pytest.fixture
def app() -> Flask:
    """Setup flask test app which only gets executed once"""
    params = {"DEBUG": False, "TESTING": True}

    _app = create_app(settings_override=params)

    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture
def client(app: Flask):
    """Setup an app client, this gets executed for each test function"""
    yield app.test_client()
