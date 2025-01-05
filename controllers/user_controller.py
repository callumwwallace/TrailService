from flask import Blueprint, request, jsonify
from flask_restx import Namespace, Resource, fields
from models.user_model import fetch_users, insert_user

user_ns = Namespace("users", description="User operations")

# Swagger model for User
user_model = user_ns.model('User', {
    'Username': fields.String(required=True, description="The user's username"),
    'Email': fields.String(required=True, description="The user's email"),
    'PasswordHash': fields.String(required=True, description="The user's password hash")
})

@user_ns.route("/")
class Users(Resource):
    def get(self):
        """Fetch all users."""
        users = fetch_users()
        return jsonify(users)

    @user_ns.expect(user_model)
    def post(self):
        """Add a new user."""
        data = request.json
        insert_user(data['Username'], data['Email'], data['PasswordHash'])
        return {"message": "User added successfully!"}, 201