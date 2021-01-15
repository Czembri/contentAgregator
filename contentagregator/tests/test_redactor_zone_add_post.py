from contentagregator.tests.base import BaseTestCase
import io

class TestCreateAPost(BaseTestCase):
    # polish news api get endpoints
    def test_create(self):
        with self.client:
            file_name = "fake-text-stream.txt"
            try:
                to_send={
                    'post_groups':1,
                    'post_title':'TEST',
                    'post_content':"test content",
                    'post_attachments[]': (io.BytesIO(b"some initial text data"), file_name)
                }
                result = client.post(
                    '/redactor-zone/forum/create-post',
                    data=to_send,
                    follow_redirects=True
                )
                self.assertEqual(
                result.data,
                json.dumps(sent)
                )
            except:
                self.assert500