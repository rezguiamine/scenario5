from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


@app.route("/")
def index():
    return jsonify(message="MEDIANET service", env=os.getenv("APP_ENV", "dev")), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
