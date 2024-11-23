#!/usr/bin/env python3
"""
Flask app serving as user interface

modules imported: Flask, jsonify

"""
from flask import (
    abort,
    Flask,
    make_response,
    redirect,
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
        abort(400)  # bad request, email or password missing

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


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """Logout a user via the passed session cookie, destroys the session"""
    session_id = request.cookies.get('session_id')
    if not session_id:
        abort(400)  # bad request

    # get the user with the corresponding cookie
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)  # forbidden, incorrect cookie in header

    # destroy the session
    AUTH.destroy_session(user.id)

    # redirect the user to the homepage
    return redirect('/')


@app.route('/profile', strict_slashes=False)
def profile():
    """Displays the profile of the user matching the credentials"""
    session_id = request.cookies.get('session_id')
    if not session_id:
        abort(403)  # forbidden, missing session_id cookie

    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)  # forbidden, incorrect/unmatched session_id

    return jsonify({"email": f"{user.email}"}), 200


@app.route('/reset_password', strict_slashes=False)
def get_reset_password_token():
    """Displays a rest_token for a password reset request by a user
    Not Secure: the users prov password isnt asked for before a
    reset token is created
    """
    email = request.form.get('email')
    if not email:
        abort(403)  # forbidden, missing email paarm in form data

    try:
        reset_token = AUTH.get_reset_password_token(email)
    except ValueError:  # user not found with the passed email
        abort(403)

    return jsonify({
        "email": f"{user.email}",
        "reset_token": f"{reset_token}"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
