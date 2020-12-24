
from flask import url_for, request, Response
from flask_login import current_user

from contentagregator.tests.base import BaseTestCase
from contentagregator.modules.auth.models import User


class TestUserApi(BaseTestCase):
    # Ensure id is correct for the current/logged in user
    def test_login_api(self):
        with self.client:
            self.client.post('/api/auth/login', data=dict(
                username="test", password='test'
            ), follow_redirects=True)
            self.assert200

    def test_invalid_login_api(self):
        with self.client:
            self.client.post('/api/auth/login', data=dict(
                username="test2", password='test2'
            ), follow_redirects=True)
            self.assert500

    def test_users_can_logout_api(self):
        with self.client:
            self.client.post("/api/auth/login", data={"username": "test", "password": "test"}, follow_redirects=True)
            self.client.post("/api/auth/logout/access")
            self.assert200



if __name__ == '__main__':
    unittest.main()
