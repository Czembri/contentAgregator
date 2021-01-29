from contentagregator.tests.base import BaseTestCase

class TestGetApi(BaseTestCase):
    # polish news api get endpoints
    def test_rmf(self):
        with self.client:
            try:
                self.client.get('/api/v1/pl/rmf', follow_redirects=True)
                self.assert200
            except:
                self.assert500


    def test_interia(self):
        with self.client:
            try:
                self.client.get('/api/v1/pl/interia', follow_redirects=True)
                self.assert200
            except:
                self.assert500


    def test_gazeta(self):
        with self.client:
            try:
                self.client.get('/api/v1/pl/gazeta', follow_redirects=True)
                self.assert200
            except:
                self.assert500


    # english news api get endpoints
    def test_google(self):
        with self.client:
            try:
                self.client.get('/api/v1/en/google', follow_redirects=True)
                self.assert200
            except:
                self.assert500

    
    def test_bbc(self):
        with self.client:
            try:
                self.client.get('/api/v1/en/bbc', follow_redirects=True)
                self.assert200
            except:
                self.assert500


    def test_cnn(self):
        with self.client:
            try:
                self.client.get('/api/v1/en/cnn', follow_redirects=True)
                self.assert200
            except:
                self.assert500


    def test_posts(self):
        with self.client:
            try:
                self.client.get('/redactor-zone/forum/api/posts', follow_redirects=True)
                self.assert200
            except:
                self.assert500


    def test_articles(self):
        with self.client:
            try:
                self.client.get('/redactor-zone/api/all-articles', follow_redirects=True)
                self.assert200
            except:
                self.assert500

    def translations(self):
        with self.client:
            try:
                self.client.get('/api/translations', follow_redirects=True)
                self.assert200
            except:
                self.assert500

    def current_language(self):
        with self.client:
            try:
                self.client.get('/api/language', follow_redirects=True)
                self.assert200
            except:
                self.assert500


if __name__ == '__main__':
    unittest.main()