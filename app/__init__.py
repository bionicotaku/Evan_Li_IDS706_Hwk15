from flask import Flask
from flask_cors import CORS
from app.services.llm_service import LLMService


def create_app():
    app = Flask(__name__)

    # initialize CORS
    CORS(app)

    # preload LLM model
    llm_service = LLMService()
    app.llm_service = llm_service  # add LLM service instance to app context

    # register blueprint
    from app.api import chat_bp
    app.register_blueprint(chat_bp)

    return app
