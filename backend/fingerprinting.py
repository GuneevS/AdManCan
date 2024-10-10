import librosa
import numpy as np
from scipy.ndimage import maximum_filter
from scipy.ndimage import generate_binary_structure, iterate_structure
import cv2
import pickle

def generate_audio_fingerprint(file_path):
    y, sr = librosa.load(file_path, sr=None)
    
    # Compute the mel-spectrogram
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
    S_dB = librosa.power_to_db(S, ref=np.max)
    
    # Find local peaks
    size = 5
    structure = generate_binary_structure(2, 1)
    neighborhood = iterate_structure(structure, size)
    local_max = maximum_filter(S_dB, footprint=neighborhood) == S_dB
    background = (S_dB == S_dB.min())
    eroded_background = maximum_filter(background, footprint=neighborhood)
    detected_peaks = local_max ^ eroded_background
    
    # Extract peak frequencies and times
    amps = S_dB[detected_peaks]
    freqs, times = np.where(detected_peaks)
    
    # Sort peaks by amplitude and keep only the strongest ones
    i = amps.argsort()[::-1][:100]
    freqs = freqs[i]
    times = times[i]
    
    # Create fingerprint
    fingerprint = list(zip(freqs, times))
    
    return fingerprint

def generate_video_fingerprint(file_path):
    cap = cv2.VideoCapture(file_path)
    fingerprint = []
    frame_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        if frame_count % 30 == 0:  # Process every 30th frame
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            resized = cv2.resize(gray, (64, 64))
            flat = resized.flatten()
            fingerprint.append(flat)
        
        frame_count += 1
    
    cap.release()
    return np.array(fingerprint)

def generate_fingerprint(file_path):
    if file_path.lower().endswith(('.mp3', '.wav', '.ogg')):
        return ('audio', generate_audio_fingerprint(file_path))
    elif file_path.lower().endswith(('.mp4', '.avi', '.mov')):
        return ('video', generate_video_fingerprint(file_path))
    else:
        raise ValueError("Unsupported file format")

def match_fingerprint(fingerprint, stored_fingerprints):
    media_type, fp = fingerprint
    best_match = None
    best_score = 0
    
    for ad_id, (stored_type, stored_fp) in stored_fingerprints.items():
        if media_type != stored_type:
            continue
        
        if media_type == 'audio':
            score = len(set(fp) & set(stored_fp)) / len(fp)
        else:  # video
            score = np.mean([np.corrcoef(f1, f2)[0, 1] for f1, f2 in zip(fp, stored_fp)])
        
        if score > best_score:
            best_score = score
            best_match = ad_id
    
    return best_match, best_score

def serialize_fingerprint(fingerprint):
    return pickle.dumps(fingerprint)

def deserialize_fingerprint(serialized_fingerprint):
    return pickle.loads(serialized_fingerprint)