from flask import Blueprint, render_template

app = Blueprint('admin_dashboard', __name__)


@app.route('/')
def index():
    return 'Admin Dashboard'


@app.route('/login')
def login():
    return render_template('admin_dashboard/login.html')