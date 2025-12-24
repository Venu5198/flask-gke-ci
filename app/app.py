import os
import logging
from flask import Flask, jsonify

app = Flask(__name__)

# Structured logging
logging.basicConfig(
    level=logging.INFO,
    format='{"time":"%(asctime)s","level":"%(levelname)s","message":"%(message)s"}'
)
logger = logging.getLogger(__name__)

APP_ENV = os.getenv("APP_ENV", "dev")

@app.route("/health")
def health():
    return jsonify(status="ok", env=APP_ENV), 200

@app.route("/api/v1/users")
def users():
    logger.info("Users endpoint hit")
    return jsonify(users=["alice", "bob", "charlie"]), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))

