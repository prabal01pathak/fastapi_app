from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    return jsonify({
        "message": "Hello From Flask"
    })

if __name__=="__main__":
    app.run(host="0.0.0.0")