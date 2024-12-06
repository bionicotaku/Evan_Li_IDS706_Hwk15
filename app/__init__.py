from flask import Flask
from flask_cors import CORS
from app.services.llm_service import LLMService
import logging
import sys



def create_app():
    app = Flask(__name__)

    # initialize CORS
    CORS(app)

    # set up logging
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.INFO)
    
    with app.app_context():
        llm_service = LLMService()
        app.llm_service = llm_service
    
    # register blueprint
    from app.api import chat_bp
    app.register_blueprint(chat_bp)

    return app
