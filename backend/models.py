from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Ad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    media_type = db.Column(db.String(10), nullable=False)
    duration = db.Column(db.String(10), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    fingerprint = db.Column(db.LargeBinary)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'mediaType': self.media_type,
            'duration': self.duration,
            'isActive': self.is_active,
            'createdAt': self.created_at.isoformat()
        }

class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    media_type = db.Column(db.String(10), nullable=False)
    folder_path = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'mediaType': self.media_type,
            'folderPath': self.folder_path,
            'isActive': self.is_active,
            'createdAt': self.created_at.isoformat()
        }

class Detection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ad_id = db.Column(db.Integer, db.ForeignKey('ad.id'), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    confidence_score = db.Column(db.Float, nullable=False)

    ad = db.relationship('Ad', backref=db.backref('detections', lazy=True))
    channel = db.relationship('Channel', backref=db.backref('detections', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'adId': self.ad_id,
            'channelId': self.channel_id,
            'timestamp': self.timestamp.isoformat(),
            'confidenceScore': self.confidence_score
        }

class Setting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    default_media_type = db.Column(db.String(10), default='video')
    notification_email = db.Column(db.String(100))
    data_retention_days = db.Column(db.Integer, default=30)
    confidence_threshold = db.Column(db.Float, default=0.8)

    def to_dict(self):
        return {
            'defaultMediaType': self.default_media_type,
            'notificationEmail': self.notification_email,
            'dataRetentionDays': self.data_retention_days,
            'confidenceThreshold': self.confidence_threshold
        }