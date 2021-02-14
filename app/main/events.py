from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio
from collections import defaultdict

members = defaultdict(int)

@socketio.on('joined', namespace='/chat')
def joined(message):
    global members
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    join_room(room)
    members[room] += 1
    emit('status', {'msg': session.get('name') + ' has entered the room.', 'name': session.get('name'), 'members': members[room]}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    emit('message', {'msg':  message['msg'], 'name': session.get('name')}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    global members
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    members[room] -= 1
    emit('status', {'msg': session.get('name') + ' has left the room.', 'name': session.get('name')}, room=room)



