from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog('Test', 'Author')
        b.create_post('banana', 'potato')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'banana')
        self.assertEqual(b.posts[0].content, 'potato')

    def test_json_no_posts(self):
        b = Blog('Test', 'Author')

        expected = {
            'title': 'Test',
            'author': 'Author',
            'posts': []
        }

        self.assertDictEqual(b.json(), expected)

    def test_json(self):
        b = Blog('Test', 'Author')
        b.create_post('banana', 'potato')

        expected = {
            'title': 'Test',
            'author': 'Author',
            'posts': [{
                'title': 'banana',
                'content': 'potato'
            }]
        }

        self.assertDictEqual(b.json(), expected)