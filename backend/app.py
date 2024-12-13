from flask import Flask
from controllers.company_controller import company_bp
from controllers.user_controller import user_bp
from controllers.conversation_controller import conversation_bp
from controllers.message_controller import message_bp
from controllers.satisfaction_controller import satisfaction_bp
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

app.register_blueprint(company_bp)
app.register_blueprint(user_bp)
app.register_blueprint(conversation_bp)
app.register_blueprint(message_bp)
app.register_blueprint(satisfaction_bp)

