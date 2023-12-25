from flask import Flask, render_template
from flask_socketio import SocketIO
from p import *

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/members')
def members():
    return {"members": ["1", "2"]}

@socketio.on('message')
def handle_message(msg):
    print('Message:', msg)
    socketio.emit('message', msg)

if __name__ == '__main__':
    app.run(debug=True)
