from unittest import TestCase
from post import Post

class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Title', 'Content')

        self.assertEqual('Title', p.title)
        self.assertEqual('Content', p.content)

    def test_json(self):
        p = Post('Title', 'Content')
        expected = {
            'title': 'Title',
            'content': 'Content'
        }
        self.assertDictEqual(expected, p.json())