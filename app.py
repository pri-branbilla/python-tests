from blog import Blog

blogs = dict()
POST_TEMPLATE = '''
--- {} ---

{}

'''
MENU_PROMPT = 'Enter c to create a blog, l to list, r to read one, p to create a post or q to quit: '

def menu():
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            read_blog()
        elif selection == 'p':
            create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))

def create_blog():
    title = input('Blog title: ')
    author = input('Author: ')

    blogs[title] = Blog(title, author)

def read_blog():
    title = input('Enter the blog title you want to read: ')
    print_posts(blogs[title])


def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))

def create_post():
    blog = input('Enter the blog title to enter the post: ')
    title = input('Enter title: ')
    content = input('Enter content: ')

    blogs[blog].create_post(title, content)
