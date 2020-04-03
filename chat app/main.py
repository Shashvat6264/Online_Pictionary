from flask import Flask, render_template
from flask_socketio import SocketIO, join_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def givetemp():
    return render_template('index.html')


@app.route('/<int:room>')
def sessions(room):
    return render_template('session.html', room=room)

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('join')
def handle_my_custom_event(json, method=['GET', 'POST']):
    print('Joined' + str(json))
    join_room(int(json['room']))
    socketio.emit('print_msg',json, to=int(json['room']),callback=messageReceived)


@socketio.on('send_msg')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('print_msg', json, to=int(json['room']) ,callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)