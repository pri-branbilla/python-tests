from unittest import TestCase
from unittest.mock import patch
from blog.tests.blog import Blog
from blog.tests import app


class AppTest(TestCase):
    def test_print_blogs(self):
        b = Blog('Test', 'Author')
        app.blogs = {'Test': b}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Author (0 posts)')

    def test_menu_prints_prompt(self):
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

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