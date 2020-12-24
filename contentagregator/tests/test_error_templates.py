from contentagregator.tests.base import BaseTestCase
from contentagregator.modules.auth.models import User


class TestErrorTemplates(BaseTestCase):
    # Ensure id is correct for the current/logged in user
    def test_404(self):
        with self.client:
            self.client.get('/undefined', follow_redirects=True)
            self.assert404



if __name__ == '__main__':
    unittest.main()