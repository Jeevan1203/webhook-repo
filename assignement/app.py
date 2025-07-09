from flask import Flask
from flask_cors import CORS
from assignement.routes import webhook_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(webhook_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5000)
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404

