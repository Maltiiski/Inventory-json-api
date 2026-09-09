import json
import os
from flask import Flask, jsonify, render_template, request

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


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/items", methods=["GET"])
def get_items():
    items = load_data
    return jsonify(items), 200

@app.route("/api/inventory", methods=["POST"])
def add_inventory():
    req_data = request.json or {}

    try:
        new_item = Item(
            name=req_data.get("name", "Unnamed Object"),
            quantity=req_data.get("quantity", 1),
            owner=req_data.get("owner", "N/A"),
            valuation=req_data.get("valuation", "Medium")
        )

        Items = load_data
        Items.append(new_item.to_dict())
        save_data(Items)

        return (
            jsonify(
                {
                    "status": "success",
                    "message": "Item created",
                    "item": new_item.to_dict(),
                }
            ),
            201,
        )

    except ValueError as e:
        return jsonify(
            {
                "status": "error",
                "message": str(e)
            }
        ), 400

@app.route("/api/inventory/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    items = load_data()

    updated_items = [item for item in items if item.get("id") !=item_id]

    if len(items) == len(updated_items):
        return jsonify({
            "status": "error",
            "message": "Item ilang"
        }), 404

    save_data(updated_items)
    return(
        jsonify(
            {"status": "success", "message": f"item {item_id} deleted!"}
        ), 200,
    )

