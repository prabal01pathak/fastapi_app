from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    return jsonify({
        "message": "Hello World"
    })