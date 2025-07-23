import random
import re, hashlib
import string

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user

import config
from ext import db
from models import User, Link

app = Blueprint('admin_dashboard', __name__)


@app.route('/')
@login_required
def index():
    return render_template('admin_dashboard/dashboard.html')


@app.route(config.ADMIN_LOGIN_ROUTE_URL, methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('admin_dashboard/login.html')
    else:
        email = request.form.get('email')
        password = request.form.get('password')

        has_error = False

        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            flash('لطفا ایمیل معتبر وارد کنید')
            has_error = True

        if len(password) < 8:
            flash('رمز عبور باید حداقل 8 کاراکتر باشد')
            has_error = True

        if has_error:
            return redirect(url_for('admin_dashboard.login'))

        user = User.query.filter(User.email == email).first()
        if user is None:
            if config.ADMIN_REGISTRATION_IS_ALLOWED is False:
                flash('ثبت نام ادمین جدید غیر فعال است')
                return redirect(url_for('admin_dashboard.login'))

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


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin_dashboard.login'))


@app.route('/shorten', methods=['POST'])
@login_required
def shorten():
    url = request.json.get('url')
    short_id = request.json.get('short_id')

    if short_id == "":
        short_id = ''.join(random.choices(string.ascii_letters + string.digits, k=4))

    check_link = Link.query.filter(Link.short_id == short_id).first()
    if check_link is not None:
        return {'status': 'error', 'error': 'شناسه کوتاه تکراری است'}

    link = Link(short_id=short_id, long_url=url)
    link.user_id = current_user.id
    db.session.add(link)
    db.session.commit()

    return {'status': 'success', 'shortUrl': request.url_root + short_id}
