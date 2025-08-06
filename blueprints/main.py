from flask import Blueprint, render_template, abort, redirect

import config
from ext import db
from models import Link

app = Blueprint('main', __name__)


@app.route('/')
def index():
    if config.MAIN_PAGE_REDIRECT_TO == "":
        abort(404)
    else:
        return redirect(config.MAIN_PAGE_REDIRECT_TO)


@app.route('/<short_id>')
def redirect_to_long_url(short_id):
    short_id = short_id.lower()

    link = Link.query.filter_by(short_id=short_id).first_or_404()
    link.views += 1
    db.session.commit()
    return render_template('main/redirect.html', long_url=link.long_url)