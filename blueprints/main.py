from flask import Blueprint, render_template

from ext import db
from models import Link

app = Blueprint('main', __name__)


@app.route('/<short_id>')
def redirect(short_id):
    link = Link.query.filter_by(short_id=short_id).first_or_404()
    link.views += 1
    db.session.commit()
    return render_template('main/redirect.html', long_url=link.long_url)