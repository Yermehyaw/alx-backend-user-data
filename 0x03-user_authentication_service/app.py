#!/usr/bin/env python3
"""
Flask app serving as user interface

modules imported: Flask, jsonify

"""
from flask import (
    Flask,
    request,
    jsonify,
)
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', strict_slashes=False)
def index():
    """Honepage of app"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """Registers a new user on the db"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return

    try:
        user = AUTH.register_user(email, password)
        return jsonify({  # user not in db, new user has been created
            "email": f"{email}",
            "message": "user created"
        })
    except ValueError:  # raised of user alreasu exist in db
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
