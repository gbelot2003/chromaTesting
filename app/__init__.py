from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'

    from .routes import chat
    app.register_blueprint(chat.bp)

    socketio.init_app(app)
    return app