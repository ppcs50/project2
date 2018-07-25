import os, requests

from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

# list of all channels

message_list = []
channel_list = ['Quincy', 'Leverett', 'Kirkland']


class Messages:
    def __init__(self, user, message, channel, timestamp):
        self.user = user
        self.message = message
        self.channel = channel
        self.timestamp = timestamp

    def print_message(self):
        print(self.user, 'says', self.message, 'in channel: ', self.channel, '[', self.timestamp, ']')


@app.route("/")
def index():
    message = 'CHATTERBOX'
    return render_template("index.html", channel_list=channel_list, message_list=message_list, message=message)


@socketio.on("generate channel")
def generate_ch(channel_name):
    print ('channel created: ', channel_name)

    count = channel_list.count(channel_name)
    print(count)

    if count > 0:
        return jsonify({"ERROR": 'There are duplicate in the list.'})
    else:
        print ('There are no duplicates in this list')
        channel_list.append(channel_name)
        print ('current channel list: ', channel_list)

    emit("list channel", channel_name, broadcast=True)


@app.route("/<channel_name>", methods=['GET'])
def chat(channel_name):

    # I don't know how to retrieve it from JavaScript side, so I couldn't use it.
    resultlist = [m for m in message_list if m['channel_name'] == channel_name]
    for data in resultlist:
        msg = data['msg']
        username = data['username']
        timestamp = data['timestamp']
        message = str(username) + ': [' + str(timestamp) + '] ' + str(msg)
        print (message)

    return '<html><head><h3 class="channel_name">"' + channel_name + '"</h3></head><body><hr><ul><div id="result_'+channel_name+'"></ul><ul class="enter" id="enter_'+channel_name+'"></ul><ul class="chat" id="chatting_'+channel_name+'"></ul></body></html>'

    if not channel_name in channel_list:
        return jsonify({"ERROR": 'Invalid channel name.'})


@socketio.on("send msgs")
def message(data):
    username = data['username']
    msg = data['msg']
    channel = data['channel_name']
    timestamp = data['timestamp']

    m = Messages(user=username, message=msg, channel=channel, timestamp=timestamp)
    m.print_message()

    message_list.append(data)
    # chatlog = (m.channel + ', ' + m.user  + ': ' + m.message+ ' --:' + m.timestamp)
    # print ('chatlog: ', chatlog)
    # print (message_list)

    emit("announce msg", data, broadcast=True)