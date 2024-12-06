from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.services.llm_service import LLMService


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 初始化CORS
    CORS(app)

    # 预加载LLM模型
    llm_service = LLMService()
    app.llm_service = llm_service  # 将LLM服务实例添加到app上下文

    # 注册蓝图
    from app.api import chat_bp
    app.register_blueprint(chat_bp)

    return app
