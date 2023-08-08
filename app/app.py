from flask import Flask, request, jsonify, redirect
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://mongodb:27017/')
db = client['mydatabase']
users_collection = db['users']


@app.route('/')
def index():
    return "Welcome to our User database"


# Redirect route /user/ to /users/
@app.route('/users/')
def redirect_to_users():
    return redirect('/users/')


# Redirect route /user/user_id/ to /users/user_id/
@app.route('/users/<user_id>/')
def redirect_to_user(user_id):
    return redirect(f'/users/{user_id}/')


# Getting all users
@app.route('/users', methods=['GET'])
def get_users():
    users = list(users_collection.find({}))     # Get all the users
    return jsonify(users)
    

# Getting single user using User_id
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users_collection.find({'_id': int(user_id)})     # Get User based on user_id
    user = list(user)
    return jsonify(user)
    

# Creating New user
@app.route('/users', methods=['POST'])
def create_user():
    new_user_data = request.json  # Get the JSON data from the request body
    result = users_collection.insert_one(new_user_data)
    
    if result.inserted_id:
        return jsonify({'message': 'User created successfully', 'user_id': str(result.inserted_id)}),201
    else:
        return jsonify({'message': 'Failed to create user'}),400


# Updating Existing User
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    updated_user_data = request.json  # Get the JSON data from the request body
    print(type(user_id),type(updated_user_data['_id']))
    if '_id' in updated_user_data and int(user_id) != int(updated_user_data['_id']):      # Not Allowing user to update the _id parameter
        return jsonify({'message': 'Updating _id is not allowed'}), 400

    result = users_collection.update_one({'_id': int(user_id)}, {'$set': updated_user_data})
    
    if result.modified_count > 0:
        return jsonify({'message': 'User updated successfully'}),200
    else:
        return jsonify({'message': 'User not found or no changes made'}),404


# Deleting user
@app.route('/users/delete/<user_id>', methods=['GET'])
def delete_user(user_id):
    user = list(users_collection.find({'_id':int(user_id)}))    # Get User based on user_id

    if user:
        user = users_collection.delete_one({'_id':int(user_id)})
        return jsonify({'message': 'User deleted successfully'}),200

    else:
         return jsonify({'message': 'User not found'}),404


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

