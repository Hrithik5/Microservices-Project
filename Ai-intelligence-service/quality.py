import librosa
import numpy as np

def score_quality(audio_path: str) -> float:
    audio, sr = librosa.load(audio_path, sr=None)
    rms = np.mean(librosa.feature.rms(y=audio))
    spectral = np.mean(librosa.feature.spectral_centroid(y=audio, sr=sr))
    score = min((rms + spectral) / 1000, 1.0)
    return round(score, 2)
