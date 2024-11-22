#!/usr/bin/env python3
"""
Flask app servibg as user interface

modules imported: Flask, jsonify

"""
from flask import (
    Flask,
    jsonify,
)


app = Flask(__main__)


@app.route('/', strict_slashes=False)
def index():
    """Honepage of app"""
    return jsonify({"message": "Bienvenue"})
