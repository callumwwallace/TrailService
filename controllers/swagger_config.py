from flask_restx import Api

def configure_swagger(app):
    """Configure Swagger for the Flask app."""
    api = Api(
        app,
        version="1.0",
        title="Trail Service API",
        description="API for managing trails and users",
        doc="/"  # Set Swagger UI to the root URL
    )
    return api