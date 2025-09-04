#!/usr/bin/env python3

from flask import Flask
from usur.routes import bp as user_bp

app = Flask(__name__)

app.register_blueprint(user_bp, url_prefix="/user")

if __name__ == "__main__":
	app.run(debug=True)
