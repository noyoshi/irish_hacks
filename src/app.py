import random 
from flask import Flask, render_template, url_for, redirect, request, session, Response
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# TODO 
# Create new video player file for each new client
# If someone wants to connect to an exisiting session, send that html
# At the end of the session, if both people close, then kill the page after x
# amount of time (garbage collection, or else we will fill up our directories)

@app.route("/")
def index():
    if request.query_string:
        base_url = request.base_url
        query_string = request.query_string.decode("utf-8")
        chat_key = request.args.get("ChatKey") 
        video_id = request.args.get("VideoID")
        if len(chat_key.strip()) == 0:
            chat_key = "yt_share_default"
        new_url = base_url + "{}*{}".format(video_id, chat_key)
        return new_url 

    return render_template('index.html') 

@app.route("/generate_route")
def generate_route():
    pass

@app.route("/<video_code>")
def send_video_page(video_code):
    print("VIDEO CODE", video_code)
    data = video_code.split("*") 
    print(data)
    if len(data) > 1:
        video_key, chat_key = data
    else:
        video_key = data[0]
        chat_key = "ytshare_default_chat"
    if len(chat_key) == 0:
        chat_key = "ytshare_default_chat" 
    print(video_key, chat_key)
    return render_template('video_page.html', 
            video_key=video_key, 
            chat_key=chat_key)

@socketio.on('video_update')
def handle_video_update(data):
    print(data)
    emit('video_update', data, broadcast=True)

if __name__ == "__main__":
    socketio.run(app)
