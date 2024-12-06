from flask import Blueprint, jsonify, request, current_app, render_template

chat_bp = Blueprint('chat', __name__)


@chat_bp.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '').strip()
        if not user_message:
            return jsonify({"error": "Message cannot be empty"}), 400

        print("user_message: ", user_message)
        response = current_app.llm_service.generate_response(user_message)
        print("response: ", response)

        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@chat_bp.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200


@chat_bp.route('/')
def index():
    return render_template('index.html')
