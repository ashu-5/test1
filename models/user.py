import sqlite3
from db import db

# User is not a resource, so doesn't belong in resources. As API cannot receive or post data from this. 
# It is a helper. Resource is external representation of an entity - APIs communicate with resources.
# When we deal internally with our resources, we're using a model. Models are helpers that give us more flexibility without 
# polluting what the clients see.

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    # id is no longer required to be passed, sqlalchemy will already autoincrement it as it is primary key integer

    def __init__(self,username,password):
        #self.id = _id
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()


    @classmethod
    def find_by_userid(cls, _id):
        return cls.query.filter_by(id=_id).first()