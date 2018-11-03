from flask import Flask, render_template, url_for, jsonify, request, session, Response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html') 
