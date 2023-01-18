from flask_restful import Resource
from flask import request
from flask_jwt_extended import create_access_token

from models.user import UserModel


class UserLogin(Resource):
    @classmethod
    def post(cls) -> any:
        user_json = request.get_json()
        user_data = UserModel.find_by_login(user_json['login'])

        if user_data and user_data.password == user_json['password']:
            access_token = create_access_token(identity=user_data.id, fresh=True)

            return {'access_token': access_token}, 200

        return {'message': 'Invalid credentials'}, 401
