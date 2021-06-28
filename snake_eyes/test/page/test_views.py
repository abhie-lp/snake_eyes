"""Tests for page views"""

from flask import url_for
from flask.testing import FlaskClient
from werkzeug.test import TestResponse as Response


class TestPage:
    def test_home_page_loads_successfully(self, client: FlaskClient):
        """Test home page response of 200"""
        response: Response = client.get(url_for("page.home"))
        assert response.status_code == 200

    def test_terms_page_loads_successfully(self, client: FlaskClient):
        """Test terms and conditions page successful load"""
        response: Response = client.get(url_for("page.terms"))
        assert response.status_code == 200

    def test_privacy_page_loads_successfully(self, client: FlaskClient):
        """Test privacy page successful load"""
        response: Response = client.get(url_for("page.privacy"))
        assert response.status_code == 200
