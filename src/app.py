import random 
from flask import Flask, render_template, url_for, jsonify, request, session, Response
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
        query_string = request.query_string.decode("utf-8")
        key, value = query_string.split("=")
        if key == "VideoID":
            return send_video_page(value)

    return render_template('index.html') 

@app.route("/generate_route")
def generate_route():
    pass

@app.route("/<video_key>")
def send_video_page(video_key):
    return render_template('video_page.html', video_key=video_key)

@app.route("/update_video/<video_key>")
def update_video(video_key):
    print("Trying to update", video_key)
    return "success"

@socketio.on('video_update')
def handle_video_update(data):
    print(data, "VIDEO UPDATE??")
    emit('video_update', data, broadcast=True)

if __name__ == "__main__":
    socketio.run(app)
