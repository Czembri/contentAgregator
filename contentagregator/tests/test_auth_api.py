
from flask import url_for, request, Response
from flask_login import current_user

from contentagregator.tests.base import BaseTestCase
from contentagregator.modules.auth.models import User


class TestUserApi(BaseTestCase):
    # Ensure id is correct for the current/logged in user
    def test_login_api(self):
        with self.client:
            self.client.post('/auth/login', data=dict(
                username="test", password='test'
            ), follow_redirects=True)
            self.assert200

    def test_invalid_login_api(self):
        with self.client:
            self.client.post('/auth/login', data=dict(
                username="test2", password='test2'
            ), follow_redirects=True)
            self.assert500


if __name__ == '__main__':
    unittest.main()

# class UserViewsTests(BaseTestCase):
#     def test_users_can_login(self):
#         User.create(username="Joe", email="joe@joes.com", password="12345")

#         with self.client:
#             response = self.client.post("/login/", data={"username": "Joe", "password": "12345"})

#             self.assert_redirects(response, url_for("index"))
#             self.assertTrue(current_user.name == "Joe")
#             self.assertFalse(current_user.is_anonymous())

#     def test_users_can_logout(self):
#         User.create(name="Joe", email="joe@joes.com", password="12345")

#         with self.client:
#             self.client.post("/login/", data={"username": "Joe", "password": "12345"})
#             self.client.get("/logout/")

#             self.assertTrue(current_user.is_anonymous())

#     def test_invalid_password_is_rejected(self):
#         User.create(username="Joe", email="joe@joes.com", password="12345")

#         with self.client:
#             self.client.post("/login/", data={"username": "Joe", "password": "****"})

#             self.assertTrue(current_user.is_anonymous())