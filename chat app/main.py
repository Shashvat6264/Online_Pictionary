from flask import Flask, render_template, redirect, url_for
from flask_socketio import SocketIO, join_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)
user_name = {}

@app.route('/')
def givetemp():
    return render_template('index.html')

@socketio.on('user')
def handle_my_custom_event(json,method=['GET', 'POST']):
    print('User Registered'+str(json))
    if json['room'] not in user_name.keys():
        user_name[json['room']] = []
    if json['username'] not in user_name[json['room']]:
        user_name[json['room']].append(json['username'])
    print(user_name)


@app.route('/<username>/<int:room>')
def sessions(room, username):
    return render_template('session.html', username=username, room=room)

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('join')
def handle_my_custom_event(json, method=['GET', 'POST']):
    # print(username)
    print('Joined' + str(json))
    join_room(int(json['room']))
    socketio.emit('print_msg',json, to=int(json['room']),callback=messageReceived)


@socketio.on('send_msg')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('print_msg', json, to=int(json['room']) ,callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)