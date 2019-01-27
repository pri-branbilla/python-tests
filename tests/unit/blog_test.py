from unittest import TestCase
from blog.tests.blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Author', b.author)
        self.assertListEqual([], b.posts)

    def test_json(self):
        b = Blog('Title', 'Author')
        expected = {
            'title': 'Title',
            'author': 'Author',
            'posts': [],
        }
        self.assertDictEqual(expected, b.json())

    def test_repr(self):
        b = Blog('Test', 'Author')
        b2 = Blog('A', 'B')

        self.assertEqual(b.__repr__(), 'Test by Author (0 posts)')
        self.assertEqual(b2.__repr__(), 'A by B (0 posts)')

    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Author')
        b.posts = ['batata']
        b2 = Blog('A', 'B')
        b2.posts = ['batata', 'banana']

        self.assertEqual(b.__repr__(), 'Test by Author (1 post)')
        self.assertEqual(b2.__repr__(), 'A by B (2 posts)')
