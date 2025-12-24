from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    @app.route("/health")
    def health():
        return "OK", 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))  # nosec B104
