import random 
from flask import Flask, render_template, url_for, jsonify, request, session, Response

app = Flask(__name__)

# TODO 
# Create new video player file for each new client
# If someone wants to connect to an exisiting session, send that html
# At the end of the session, if both people close, then kill the page after x
# amount of time (garbage collection, or else we will fill up our directories)

@app.route("/")
def index():
    if 'VideoID' in request.headers:
        send_video_page(request.headers['VideoID'])
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
