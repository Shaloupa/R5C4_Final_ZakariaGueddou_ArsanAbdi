from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    # Configuration CORS pour Angular
    CORS(app)

    # Enregistrer les blueprints
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app