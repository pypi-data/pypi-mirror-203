
from models.model import User, Post, session

def home():
    context = {
        'title': 'Jaguar',
        'description': 'A simple Python web framework.',
    }
    return {'_template': 'base.html.jq', **context}

def about():
    context = {
        'title': 'About Jaguar',
        'description': 'A simple Python web framework.',
    }
    return {'_template': 'about.html.jq', **context}

def create_user_and_post():
    user = User(name='John Doe', email='johndoe@example.com')
    session.add(user)
    session.commit()

    # post = Post(title='My first post', content='Hello, world!', author=user)
    # session.add(post)
    # session.commit()

    return {'_template': 'index.html.jq', 'message': 'User and post created successfully'}

# def display_posts():
#     posts = session.query(Post).all()
#     context = {
#         'title': 'Posts',
#         'description': 'A simple Python web framework.',
#         'posts': posts,
#     }
#     return {'_template': 'posts.html.jq', **context}
def display_users():
    users = session.query(User).all()
    context = {
        'title': 'Users',
        'description': 'A simple Python web framework.',
        'users': users,
    }
    return {'_template': 'users.html.jq', **context}