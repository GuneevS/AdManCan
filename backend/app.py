from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db, Ad, Channel, Detection, Setting
from fingerprinting import generate_fingerprint, match_fingerprint, serialize_fingerprint, deserialize_fingerprint
import os
from werkzeug.utils import secure_filename
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
import logging
from logging.handlers import RotatingFileHandler
from schema import AdSchema, ChannelSchema, SettingSchema

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///admeneev1.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER', 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size
db.init_app(app)

limiter = Limiter(app, key_func=get_remote_address)

# Set up logging
if not app.debug:
    file_handler = RotatingFileHandler('app.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('AdMeneerV1 startup')

@app.before_first_request
def create_tables():
    db.create_all()
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

@app.errorhandler(404)
def not_found_error(error):
    return jsonify(error="Resource not found"), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify(error="Internal server error"), 500

@app.route('/api/ads', methods=['GET', 'POST'])
@limiter.limit("100/day")
def handle_ads():
    if request.method == 'GET':
        ads = Ad.query.all()
        return jsonify([ad.to_dict() for ad in ads])
    elif request.method == 'POST':
        try:
            ad_schema = AdSchema()
            data = ad_schema.load(request.form)
            file = request.files.get('file')

            if not file:
                return jsonify({'error': 'No file provided'}), 400

            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            new_ad = Ad(**data)
            db.session.add(new_ad)
            db.session.commit()

            fingerprint = generate_fingerprint(file_path)
            new_ad.fingerprint = serialize_fingerprint(fingerprint)
            db.session.commit()

            return jsonify(new_ad.to_dict()), 201
        except Exception as e:
            app.logger.error(f'Error creating ad: {str(e)}')
            return jsonify({'error': 'Error creating ad'}), 500

# ... (similar improvements for other routes)

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')