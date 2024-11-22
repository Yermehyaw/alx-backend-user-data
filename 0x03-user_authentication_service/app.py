#!/usr/bin/env python3
"""
Flask app serving as user interface

modules imported: Flask, jsonify

"""
from flask import (
    abort,
    Flask,
    make_response,
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


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """Handles user login and attains a session for the user"""
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password:
        abort(401)

    if not AUTH.valid_login(email, password):
        abort(401)

    new_session = AUTH.create_session(email)

    response = make_response(
        jsonify({
            "email": f"{email}",
            "message": "logged in"
        })
    )
    response.set_cookie('session_id', new_session)

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
