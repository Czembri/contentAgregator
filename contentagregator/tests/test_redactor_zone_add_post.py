from contentagregator.tests.base import BaseTestCase
import io

from datetime import datetime

class TestCreateAPost(BaseTestCase):
    # polish news api get endpoints
    def test_create_one_file(self): # testing with one txt file
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


    def test_create_multiple_files(self): # testing with multiple txt files
        with self.client:
            file_name = "fake-text-stream.txt"
            file_name_2 = "fake-2-text-stream.txt"
            try:
                to_send={
                    'post_groups':1,
                    'post_title':'TEST',
                    'post_content':"test content",
                    'post_attachments[]': [
                        (io.BytesIO(b"some initial text data"), file_name), 
                        (io.BytesIO(b"some initial text data 2"), file_name_2)
                        ]
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

    def test_create_no_group(self): # testing with no group
        with self.client:
            try:
                to_send={
                    'post_title':'testtest',
                    'post_content':"test content"
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


    def test_add_commentary(self):
        with self.client:
            post_id, user_id=1
            try:
                to_send={
                    'user_id':user_id,
                    'post_id':post_id,
                    'add_commentary':'simple comment',
                    'creation_time': datetime.utcnow(),
                    'modification_time':datetime.utcnow()
                }
                result = client.post(
                    f'/redactor-zone/forum/add-comment/{post_id}',
                    data=to_send,
                    follow_redirects=True
                )
                self.assertEqual(
                result.data,
                json.dumps(sent)
                )
            except:
                self.assert500


    def test_add_commentary(self): # no user id - user not in session
        with self.client:
            post_id=1
            to_send={
                'post_id':post_id,
                'add_commentary':'simple comment',
                'creation_time': datetime.utcnow(),
                'modification_time':datetime.utcnow()
            }
            try:
                result = client.post(
                    f'/redactor-zone/forum/add-comment/{post_id}',
                    data=to_send,
                    follow_redirects=True
                )
            except:
                self.assert400


    def test_update_post(self): # no user id - user not in session
        with self.client:
            post_id=1
            to_send={
                'post_id':post_id,
                'post_title':'simple title',
                'post_content': 'simple content'
            }
            try:
                result = client.PUT(
                    f'/redactor-zone/forum/edit-post/{post_id}',
                    data=to_send,
                    follow_redirects=True
                )
            except:
                self.assert400