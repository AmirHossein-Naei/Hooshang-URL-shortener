import re , hashlib

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user

from ext import db
from models import User

app = Blueprint('admin_dashboard', __name__)


@app.route('/')
@login_required
def index():
    return f"Hello, {current_user.email}! You're logged in! <a href='/admin/logout'>Logout</a>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('admin_dashboard/login.html')
    else:
        email = request.form.get('email')
        password = request.form.get('password')

        has_error = False

        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) :
            flash('لطفا ایمیل معتبر وارد کنید')
            has_error = True

        if len(password) < 8:
            flash('رمز عبور باید حداقل 8 کاراکتر باشد')
            has_error = True

        if has_error:
            return redirect(url_for('admin_dashboard.login'))


        user = User.query.filter(User.email==email).first()
        if user is None:
            user = User(email=email)
            user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()

            db.session.add(user)
            db.session.commit()

        else:
            if user.password != hashlib.sha256(password.encode('utf-8')).hexdigest():
                flash('رمز عبور اشتباه است')
                return redirect(url_for('admin_dashboard.login'))


        login_user(user, remember=True)

        return redirect(url_for('admin_dashboard.index'))


        return ""

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin_dashboard.login'))