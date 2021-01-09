from contentagregator.tests.base import BaseTestCase

class TestCreateAnArticle(BaseTestCase):
    # polish news api get endpoints
    def test_create(self):
        with self.client:
            try:
                to_send={
                    'check-category':1,
                    'title':'TEST',
                    'trumbowyg':"test content"
                }
                result = client.post(
                    '/redactor-zone/create-an-article',
                    data=to_send,
                    follow_redirects=True
                )
                self.assertEqual(
                result.data,
                json.dumps(sent)
                )
            except:
                self.assert500


    def test_update(self):
        with self.client:
            try:
                to_send={
                    'article_id':1,
                    'check-category':1,
                    'title':'TEST',
                    'trumbowyg':"test content"
                }
                result = client.post(
                    '/redactor-zone/user-article/<int:article_id>',
                    data=to_send,
                    follow_redirects=True
                )
                self.assertEqual(
                result.data,
                json.dumps(sent)
                )
            except:
                self.assert500