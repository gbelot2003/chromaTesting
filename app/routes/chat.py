from flask import Blueprint, render_template
from flask_socketio import emit
from ..services.deepseek_service import get_deepseek_response
from ..utils.websocket_utils import send_message
from .. import socketio  # Importar socketio aquí

bp = Blueprint('chat', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/chat')
def chat():
    return render_template('templates/index.html')

@socketio.on('send_message')
def handle_message(data):
    user_message = data['message']
    response = get_deepseek_response(user_message)
    send_message(response)