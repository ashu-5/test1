from db import db

# We pull the classmethods from previous items code as they aren't resources users can interact him. 
# So we put them in models. As convention, @classmethods are separated by 2 lines in python.

class ItemModel(db.Model):

    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {"name":self.name, "price": self.price}


    @classmethod
    def find_by_name(cls, name):
        # We don't need any of the connection and return object changes now. SQLAlchemy will do that for us.
        
        # Equivalent to "SELECT * FROM items WHERE name=name LIMIT 1". And also converts it to an ItemModel object.

        return cls.query.filter_by(name=name).first() 
        

    # These no longer need to be a classmethod, as they're going to insert an item object that already exists to the db.
    # These insert and update an item

    # This method can both update and insert the data -> upserting. We don't need update method anymore. 
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()



#var JsonData = pm.response.json();

#pm.test("Access token test") = jsonData.access_token!== undefined
#pm.environment.set("jwt_token", jsonData.access_token);

#var jsonData = JSON.parse(responseBody)
#tests("Access token test") = jsonData.access_token !== undefined
#postman.setEnvironmentVariable("jwt_token", jsonData.access_token);