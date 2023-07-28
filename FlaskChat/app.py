from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit   
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from DatabaseFunc import *

app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config['SECRET_KEY'] = 'abcdefghijklmnop'
socketio = SocketIO(app)

@app.route('/chat', methods=['GET'])
def chatPage():
    return render_template('chat.html', l=[], u= request.values.get('q'))

@app.route('/')
def userPage():
    return render_template('user.html')

if __name__ == "__main__":
    socketio.run(app)