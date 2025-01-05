from flask_restx import Namespace, Resource, fields
from flask import request

auth_ns = Namespace("auth", description="User Authentication")

# Swagger model for authentication request
auth_model = auth_ns.model('Auth', {
    'Username': fields.String(required=True, description="The user's username"),
    'Password': fields.String(required=True, description="The user's password"),
})

@auth_ns.route("/")
class Auth(Resource):
    @auth_ns.expect(auth_model)
    def post(self):
        """Authenticate User"""
        data = request.json
        # Auth logic
        if data['Username'] == "admin" and data['Password'] == "password":
            return {"message": "Authentication successful!", "token": "example_token"}, 200
        else:
            return {"message": "Invalid credentials"}, 401