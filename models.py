import time

from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from ext import db

def get_current_timestamp():
    return int(time.time())

class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, index=True, unique=True)
    password = Column(String, nullable=False)

    created_at = Column(default=get_current_timestamp)

    def __repr__(self):
        return f'<User {self.id}>'



class Link(db.Model):
    id = Column(Integer, primary_key=True)
    short_id = Column(String, nullable=False, index=True)
    long_url = Column(String, nullable=False)
    views = Column(Integer, default=0)
    created_at = Column(default=get_current_timestamp)

    user_id = Column(Integer, db.ForeignKey(User.id), nullable=False)
    user = db.relationship(User, backref=db.backref('links', lazy=True))

    def __repr__(self):
        return f'<Link {self.id}>'