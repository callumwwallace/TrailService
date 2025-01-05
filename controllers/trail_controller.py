from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from models.trail_model import fetch_trails, insert_trail, update_trail, delete_trail, get_trail_by_id

trail_ns = Namespace("trails", description="Trail operations")

# Swagger model for Trail
trail_model = trail_ns.model('Trail', {
    'Name': fields.String(required=True, description="The trail name"),
    'Description': fields.String(required=True, description="The trail description"),
    'Difficulty': fields.String(required=True, description="The trail difficulty"),
    'Duration': fields.Integer(required=True, description="Duration in minutes"),
    'Elevation': fields.Integer(required=True, description="Elevation gain in meters"),
    'TrailLength': fields.Float(required=True, description="Length of the trail in kilometers"),
    'UserID': fields.Integer(required=True, description="The ID of the user who created the trail"),
})

@trail_ns.route("/")
class Trails(Resource):
    def get(self):
        """Fetch all trails."""
        try:
            trails = fetch_trails()
            return jsonify(trails)
        except Exception as e:
            return {"error": str(e)}, 500

    @trail_ns.expect(trail_model)
    def post(self):
        """Add a new trail."""
        try:
            data = request.json
            insert_trail(
                data['Name'], data['Description'], data['Difficulty'], 
                data['Duration'], data['Elevation'], data['TrailLength'], data['UserID']
            )
            return {"message": "Trail added successfully!"}, 201
        except Exception as e:
            return {"error": str(e)}, 500


@trail_ns.route("/<int:trail_id>")
class TrailByID(Resource):
    def get(self, trail_id):
        """Get a Trail by ID"""
        try:
            trail = get_trail_by_id(trail_id)
            if trail:
                return trail, 200
            else:
                return {"message": "Trail not found"}, 404
        except Exception as e:
            return {"error": str(e)}, 500

    @trail_ns.expect(trail_model)
    def put(self, trail_id):
        """Update a Trail by ID"""
        try:
            data = request.json
            success = update_trail(
                trail_id, data['Name'], data['Description'], data['Difficulty'],
                data['Duration'], data['Elevation'], data['TrailLength'], data['UserID']
            )
            if success:
                return {"message": "Trail updated successfully"}, 200
            else:
                return {"message": "Trail not found"}, 404
        except Exception as e:
            return {"error": str(e)}, 500

    def delete(self, trail_id):
        """Delete a Trail by ID"""
        try:
            success = delete_trail(trail_id)
            if success:
                return {"message": "Trail deleted successfully"}, 200
            else:
                return {"message": "Trail not found"}, 404
        except Exception as e:
            return {"error": str(e)}, 500