import librosa
import numpy as np

def score_quality(media_url):
    audio, sr = librosa.load(media_url)
    signal_power = np.mean(audio**2)
    return round(min(signal_power * 10, 1.0), 2)
