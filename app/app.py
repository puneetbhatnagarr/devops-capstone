from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "DevOps Capstone Application",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })


@app.route("/students")
def students():
    return jsonify([
        {
            "id": 1,
            "name": "Puneet",
            "course": "DevOps"
        },
        {
            "id": 2,
            "name": "Rahul",
            "course": "Cloud"
        }
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
