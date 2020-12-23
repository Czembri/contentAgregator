from flask_testing import TestCase
import os, sys

sys.path = [os.path.abspath('')] + sys.path

from contentagregator import app, db


class BaseTestCase(TestCase):
    """A base test case for flask-tracking."""

    def create_app(self):
        app.config.from_object('contentagregator.config.TestConfig')
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()