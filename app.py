from flask import Flask
from controllers.auth_controller import auth_ns
from controllers.trail_controller import trail_ns
from controllers.swagger_config import configure_swagger

app = Flask(__name__)

# Configure Swagger
api = configure_swagger(app)

# Register namespaces
api.add_namespace(auth_ns, path="/auth")
api.add_namespace(trail_ns, path="/trails")

if __name__ == "__main__":
    app.run(debug=True)