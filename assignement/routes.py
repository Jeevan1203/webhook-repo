import os
from flask import Blueprint, request, jsonify, send_file
from assignement.models import collection
from assignement.utils import parse_event
from datetime import datetime

webhook_bp = Blueprint('webhook_bp', __name__)

@webhook_bp.route('/webhook', methods=['POST'])
def webhook():
    event_type = request.headers.get('X-GitHub-Event', '')
    payload = request.json

    event = parse_event(event_type, payload)
    if event:
        event["timestamp"] = datetime.utcnow()
        collection.insert_one(event)
        return jsonify({"message": "Event stored"}), 200
    return jsonify({"message": "Ignored"}), 400

@webhook_bp.route('/events', methods=['GET'])
def get_events():
    data = list(collection.find().sort("timestamp", -1).limit(10))
    for d in data:
        d['_id'] = str(d['_id'])
        d['timestamp'] = d['timestamp'].strftime("%d %b %Y - %I:%M %p UTC")
    return jsonify(data)

@webhook_bp.route('/')
def index():
    # Correctly resolve the absolute path to index.html
    frontend_path = os.path.join(os.path.dirname(__file__), 'frontend', 'index.html')
    return send_file(frontend_path)
@webhook_bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "OK"}), 200
@webhook_bp.route('/delete-bad-events', methods=['POST'])
def delete_bad_events():
    result = collection.delete_many({"type": {"$exists": False}})
    return jsonify({"deleted": result.deleted_count})
