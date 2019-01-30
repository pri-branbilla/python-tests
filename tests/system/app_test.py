from unittest import TestCase
from unittest.mock import patch

from blog import Blog
from post import Post
import app

class AppTest(TestCase):
    def setUp(self):
        b = Blog('Test', 'Author')
        app.blogs = {'Test': b}

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Author (0 posts)')

    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_create_blog(self):
        with patch('app.create_blog') as mocked_create_blog:
            with patch('builtins.input') as mocked_input:
                mocked_input.side_effect = ('c', 'q')
                app.menu()
                mocked_create_blog.assert_called()

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Author')
            app.create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))

    def test_read_blog(self):
        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.read_blog()

                mocked_print_posts.assert_called_with(app.blogs['Test'])

    def test_print_posts(self):
        b = app.blogs['Test']
        b.create_post('Title', 'Content')
        with patch('app.print_post') as mocked_print_post:
            app.print_posts(b)

            mocked_print_post.assert_called_with(b.posts[0])

    def test_print_post(self):
        post = Post('Title', 'Content')
        expected_print = '''
--- Title ---

Content

'''
        with patch('builtins.print') as mocked_print:
            app.print_post(post)

            mocked_print.assert_called_with(expected_print)


    def test_create_post(self):
        b = app.blogs['Test']
        app.blogs = {'Test': b}

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Title', 'Content')

            app.create_post()
            self.assertEqual(b.posts[0].title, 'Title')
            self.assertEqual(b.posts[0].content, 'Content')