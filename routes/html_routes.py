from flask import Blueprint, render_template
from controllers.user_controller import get_all_users
from middlewares.auth import login_required

html_routes = Blueprint('html_routes', __name__)

# Home page
@html_routes.route('/<int:id>')
@login_required
def home(id = 1):
    users = get_all_users()
    
    user = list(
        filter(lambda user: user['id'] == id, users)
    )[0]
    
    return render_template('index.html', users=users, name=user['name'])

@html_routes.route('/login')
def login():
    return render_template('login.html')