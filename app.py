from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from datetime import timedelta

from db import db

app = Flask(__name__)
app.secret_key='Nadal'
api = Api(app)

jwt = JWT(app,authenticate,identity)

# SQLALCHEMY db is going to live at the root folder of our project. Doesn't have to be sqlite - it can be postgresql, mysql, etc.
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

# Turns off flask_SQLAlchemy modification tracker to save resource. We'll use SQLAlchemy's built in one to do that.
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

# config JWT to expire within half an hour
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister,'/register')

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5010, debug=True)