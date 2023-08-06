import os
from flask import Flask, request, render_template, send_from_directory, render_template_string, jsonify, Response, \
    make_response
from flask_socketio import SocketIO, join_room, leave_room
import eventlet
import msgpack
import threading
import struct
import logging
import time
import json

host_name = "0.0.0.0"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='eventlet', max_http_buffer_size=100000000, ping_timeout=60)

connected_clients = dict()
# connected_clients:
#   key: client session id
#   value: client room id

storage = dict()
datas = dict()


# storage:
#    key: room id
#    value: array of length 2, where:
#        array[0]: integer counter of sent items within a room
#        array[1]: dictionary, where:
#            key: integer indicating order number
#            value: command or data item encoded in binary
#
# OBJECT                        TYPE            DESCRIPTION
#
# storage                       dictionary      dictionary of rooms
# storage[room]                 array           of length 2: [int, dict]
# storage[room][0]              integer         denoting item count of one room
# storage[room][1]              dictionary      dictionary of room items
# storage[room][1][counter]     binary item     contains command or data


@app.route('/test_connection')
def ok():
    return '', 222


@app.route('/resources/<path:path>')
def send_resource(path):
    return send_from_directory('./static/resources', path)


@app.route('/static/<path:path>')
def send_static_resource(path):
    return send_from_directory('./static', path)


@app.route('/room_response')
def room_response():
    room = request.args.get('id')
    if room in connected_clients.values():
        return '', 200
    return '', 400


@app.route('/')
def index():
    room = request.args.get('id')
    return render_template('index.html', room=room)


@socketio.on('connect')
def connect():
    connected_clients[request.sid] = 'default'


@socketio.on('disconnect')
def handle_disconnect():
    del connected_clients[request.sid]


@socketio.on('message')
def receive_message(data):
    print(data)


@app.route('/message', methods=['POST'])
def send_message():
    message = request.json['message']
    socketio.emit('message', {'message': message}, broadcast=True)
    return '', 200


def remove_item(room, key):
    del storage[room][1][key]


@socketio.on('join')
def join(room):
    join_room(room)
    connected_clients[request.sid] = room
    if room in storage:
        socketio.emit('exec', to=room)


@socketio.on('callback')
def resend_item(data):
    room = data['room']
    client_counter = data['counter']
    local_counter = storage[room][0]
    if local_counter > client_counter:
        for key in range(client_counter + 1, local_counter + 1):
            if str(key) in storage[room][1]:
                socketio.emit('item', storage[room][1][str(key)], binary=True, to=request.sid)


@app.route('/item', methods=['POST'])
def send_item():
    room = request.args.get('id')
    binary_data = request.data

    if room not in storage:
        storage[room] = [0, dict()]
    storage[room][0] += 1

    if room in connected_clients.values():
        socketio.emit('item', binary_data, binary=True, to=room)

    data = msgpack.unpackb(binary_data)
    key = str(storage[room][0])
    storage[room][1][key] = data
    return '', 200


@app.route('/data', methods=['POST'])
def send_data():
    room = request.args.get('id')
    data_id = request.args.get('data_id')
    data_bytes = request.data
    datas[data_id] = data_bytes
    return '', 200


@app.route('/exec')
def execute():
    room = request.args.get('id')
    if room in connected_clients.values():
        socketio.emit('exec', to=room)
    return '', 200


@app.route('/fetch_data')
def fetch_data():
    room = request.args.get('id')
    try:
        data = msgpack.packb(storage[room][1])
        return Response(data, mimetype='application/msgpack')
    except:
        return Response(status=404)


@app.route('/clear', methods=['POST'])
def clear():
    room = request.args.get('id')
    binary_data = request.data

    counter_bytes = struct.pack("!i", -1)
    if room in storage:
        del storage[room]
    binary_data = counter_bytes + binary_data

    if room in connected_clients.values():
        socketio.emit('item', binary_data, binary=True, to=room)

    return '', 200


def start_thread(port: int = 5656):
    server_thread = threading.Thread(target=lambda: socketio.run(
        app,
        host=host_name,
        port=port,
        debug=True,
        log_output=False,
        use_reloader=False
    ))
    print(f'\n'
          f'###############################################################\n'
          f' Flask server opened on port {port}.\n'
          f' You can leave this console open for the rest of your session.\n'
          f'###############################################################\n')
    server_thread.start()
    return server_thread


if __name__ == '__main__':
    socketio.run(
        app,
        use_reloader=False,
        debug=True,
        port=5656
    )
