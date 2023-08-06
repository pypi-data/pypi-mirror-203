from views.home import home, about, display_users, create_user_and_post

# Define the routes
urls = {
    '/': home,
    '/about': about,
    '/create-user-and-post': create_user_and_post,
    # '/display-posts': display_posts,
    '/display-users': display_users,
}