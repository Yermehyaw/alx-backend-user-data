#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
auth = getenv('AUTH_TYPE')
if auth == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorizef(error) -> str:
    """401 not authorized handler"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """403 forbidden err handler"""
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def filter_request():
    """Filters authentication necessary requests"""
    # these endpoints can be accessed withoit authentication/authorization
    auth_endpoints = [
        '/api/v1/status/', '/api/v1/unauthorized/',
        '/api/v1/forbidden/', '/api/v1/auth_session/login/'
    ]

    if not auth:
        return

    if not auth.require_auth(request.path, auth_endpoints):
        # requested path is an endpoint that doesnt need auth
        return

    if not auth.authorization_header(request):
        # theres no Authorization header in the users request
        abort(401)

    if not current_user(request):
        # No client currently logged in, abort with forbidden
        abort(403)

    if not auth.session_cookie(request):
        # user has no running session, abort with unauthorized
        abort(401)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
