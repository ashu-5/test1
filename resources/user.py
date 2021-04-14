import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type=str,
        required=True,
        help="USername parameter cannot be left blank"
    )
    parser.add_argument(
        "password",
        type=str,
        required=True,
        help="Password parameter cannot be left blank"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message":"Username already exists. Please select another username"}, 400
        
        # Else add user to the users db
        # we can replace below with data as our parser ensures that there are only those two arguments - username & password
        #user = UserModel(data['username'],data['password'])
        user = UserModel(**data)
        user.save_to_db()

        return {"message":"User registered successfully"}, 201







