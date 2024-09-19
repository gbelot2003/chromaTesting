from flask_socketio import emit

def send_message(message):
    emit('receive_message', {'message': message}, broadcast=True)