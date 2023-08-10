from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal_with, fields
from pymongo import MongoClient

user_bp = Blueprint('user_bp', __name__)
api = Api(user_bp)

client = MongoClient('mongodb://mongodb:27017/')
db = client['mydatabase']
users_collection = db['users']

# Define fields for user serialization
user_fields = {
    '_id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'password': fields.String,
}

# Request parser
user_parser = reqparse.RequestParser()
user_parser.add_argument('id', type=int, required=True)
user_parser.add_argument('name', type=str, required=True)
user_parser.add_argument('email', type=str, required=True)
user_parser.add_argument('password', type=str, required=True)

# Just a Greeting message
class Index(Resource):
    def get(self):
        return "Welcome to our User database"

class UsersResource(Resource):
    @marshal_with(user_fields)
    def get(self):
        users = list(users_collection.find({}))
        return users

    def post(self):
        args = user_parser.parse_args()
        
        user = users_collection.find_one({'_id': args['id']})
        if user:
            return {'message': 'User with the given ID already exists'}, 400

        new_user_data = {
            '_id': args['id'],
            'name': args['name'],
            'email': args['email'],
            'password': args['password']
        }

        result = users_collection.insert_one(new_user_data)

        if result.inserted_id:
            return {'message': 'User created successfully', 'user_id': args['id']}, 201
        else:
            return {'message': 'Failed to create user'}, 400

class UserResource(Resource):

    def get(self, user_id):
        user = users_collection.find_one({'_id': user_id})
        if user:
            return user
        return {'message': 'User not found'}, 404

    def put(self, user_id):
        args = user_parser.parse_args()
        updated_user_data = {
            'name': args['name'],
            'email': args['email'],
            'password': args['password']
        }

        result = users_collection.update_one({'_id': user_id}, {'$set': updated_user_data})

        if result.modified_count > 0:
            return {'message': 'User updated successfully'}, 200
        else:
            return {'message': 'User not found or no changes made'}, 404

    def delete(self, user_id):
        user = users_collection.find_one({'_id': user_id})

        if user:
            users_collection.delete_one({'_id': user_id})
            return {'message': 'User deleted successfully'}, 200
        else:
            return {'message': 'User not found'}, 404

api.add_resource(Index, '/')
api.add_resource(UsersResource, '/users')
api.add_resource(UserResource, '/users/<int:user_id>')



