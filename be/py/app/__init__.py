from flask import Flask

def create_app():
    app = Flask(__name__)

    from .router import register_routes
    register_routes(app)

    return app
