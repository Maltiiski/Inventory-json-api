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

