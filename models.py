import time
from sqlalchemy import Column, Integer, String
from ext import db

def get_current_timestamp():
    return int(time.time())

class User(db.Model):
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, index=True)
    password = Column(String, nullable=False)

    created_at = Column(default=get_current_timestamp)

    def __repr__(self):
        return f'<User {self.id}>'



class Link(db.Model):
    id = Column(Integer, primary_key=True)
    short_id = Column(String, nullable=False, index=True)
    long_url = Column(String, nullable=False)

    created_at = Column(default=get_current_timestamp)

    def __repr__(self):
        return f'<Link {self.id}>'