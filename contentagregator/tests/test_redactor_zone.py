from contentagregator.tests.base import BaseTestCase

class TestGetRedactorZone(BaseTestCase):
    # polish news api get endpoints
    def test_redactor_zone(self):
        with self.client:
            try:
                self.client.get('/redactor-zone', follow_redirects=True)
                self.assert200
            except:
                self.assert500

    def test_redactor_zone(self):
        with self.client:
            try:
                self.client.get('/redactor-zone/create-an-article', follow_redirects=True)
                self.assert200
            except:
                self.assert500