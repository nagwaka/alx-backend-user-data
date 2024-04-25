#!/usr/bin/env python3
"""A basic Flask app
"""
from flask import Flask, jsonify, request, abort, redirect


app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """GET /
    Return:
        - The home page's payload.
    """
    return jsonify({"message": "Bienvenue"})
