
from flask import url_for, request, Response
from flask_login import current_user

from contentagregator.tests.base import BaseTestCase
from contentagregator.modules.auth.models import User


class TestUserLogin(BaseTestCase):
    # Ensure id is correct for the current/logged in user
    def test_login(self):
        with self.client:
            self.client.post('/login', data=dict(
                username="test", password='test'
            ), follow_redirects=True)
            self.assert200

    def test_invalid_login(self):
        with self.client:
            self.client.post('/login', data=dict(
                username="test2", password='test2'
            ), follow_redirects=True)
            self.assert500

    def test_users_can_logout(self):
        with self.client:
            try:
                self.client.post("/login", data={"username": "test", "password": "test"}, follow_redirects=True)
                self.assert200
            except:
                self.assert500
                raise 'Can not login into app'
            finally:
                self.client.post("/logout")
                self.assert200


if __name__ == '__main__':
    unittest.main()