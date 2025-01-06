# TrailService Micro-Service

The **TrailService** micro-service is designed to enhance users' well-being by encouraging outdoor exploration through trail discovery and management. It provides essential functionalities for trail management, including CRUD operations, database integration, and RESTful API endpoints.

## Features

- **Trail Data Management**: Create, retrieve, update, and delete trail information.
- **Database Integration**: A normalized SQL database (3NF) with tables for users, trails, and comments.
- **RESTful API**: Endpoints to interact with trail data, built using Flask.
- **Scalable Design**: Modular structure with controllers, models, and utilities for maintainability.

## Project Structure

```plaintext
TrailService/
├── app.py               # Entry point for the Flask application
├── controllers/         # Handles API endpoints
│   ├── auth_controller.py   # User authentication and session management
│   ├── trail_controller.py  # CRUD operations for trails
│   ├── user_controller.py   # User-specific functionalities
├── models/              # Defines database schemas
│   ├── trail_model.py       # Trail schema
│   ├── user_model.py        # User schema
│   ├── comment_model.py     # Comment schema
├── database.py          # Manages database connections and queries
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── swagger_config.py    # Swagger configuration for API documentation
