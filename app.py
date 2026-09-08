import json
import os
from flask import Flask, jsonify, request

try:
    from flask_cors import CORS
except ImportError:
    def CORS(app=None, *args, **kwargs):
        if app is None:
            def decorator(f):
                return f
            return decorator
        return app

from model import Item

app = Flask(__name__)
CORS(app)

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load()
    except json.JSONDecodeError:
        return []


