import time
import os
from models import db, Ad, Channel, Detection
from fingerprinting import generate_fingerprint, match_fingerprint, deserialize_fingerprint
from app import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def monitor_channels():
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    Session = sessionmaker(bind=engine)

    while True:
        with app.app_context():
            session = Session()
            channels = session.query(Channel).filter_by(is_active=True).all()
            ads = session.query(Ad).all()

            stored_fingerprints = {ad.id: deserialize_fingerprint(ad.fingerprint) for ad in ads}

            for channel in channels:
                folder_path = channel.folder_path
                for filename in os.listdir(folder_path):
                    if filename.endswith(('.mp3', '.wav', '.ogg', '.mp4', '.avi', '.mov')):
                        file_path = os.path.join(folder_path, filename)
                        fingerprint = generate_fingerprint(file_path)
                        best_match, confidence = match_fingerprint(fingerprint, stored_fingerprints)

                        if best_match and confidence > 0.8:  # Adjust threshold as needed
                            new_detection = Detection(
                                ad_id=best_match,
                                channel_id=channel.id,
                                timestamp=time.time(),
                                confidence_score=confidence
                            )
                            session.add(new_detection)
                            session.commit()

                        # Optional: Move or delete processed file
                        # os.remove(file_path)

            session.close()
        time.sleep(60)  # Check every minute, adjust as needed

if __name__ == '__main__':
    monitor_channels()