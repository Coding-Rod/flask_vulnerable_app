from flask import Blueprint, render_template, session
from controllers.user_controller import get_all_users
from middlewares.auth import login_required

html_routes = Blueprint('html_routes', __name__)

# Home page
@html_routes.route('/')
@login_required
def home():
    users = get_all_users()
    
    user = list(
        filter(lambda user: user.id == session['token'], users)
    )[0]
    
    return render_template('index.html', users=users, name=user.name)

@html_routes.route('/login')
def login():
    return render_template('login.html')