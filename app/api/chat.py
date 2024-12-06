from flask import Blueprint, jsonify, request, current_app, render_template, Response, stream_with_context
import json

chat_bp = Blueprint('chat', __name__)


@chat_bp.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '').strip()
        if not user_message:
            return jsonify({"error": "Message cannot be empty"}), 400

        current_app.logger.info(f"Received message: {user_message}")
        def generate():
            for token in current_app.llm_service.generate_response(user_message):
                yield f"data: {json.dumps({'token': token})}\n\n"

        return Response(stream_with_context(generate()),
                        mimetype='text/event-stream')
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@chat_bp.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200


@chat_bp.route('/')
def index():
    return render_template('index.html')
