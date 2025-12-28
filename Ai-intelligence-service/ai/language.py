import langdetect

def detect_language(media_url):
    transcript = load_transcript(media_url)
    return langdetect.detect(transcript)
