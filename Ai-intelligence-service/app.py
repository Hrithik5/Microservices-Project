from ai.language import detect_language
from ai.topics import classify_topics
from ai.keywords import extract_keywords
from ai.quality import score_quality
from storage import save_metadata
from events import publish_event
import logging

log = logging.getLogger(__name__)

def analyze_media(event):
    media_id = event["media_id"]
    media_url = event["media_url"]

    log.info("Starting AI analysis", extra={"media_id": media_id})

    try:
        language = detect_language(media_url)
        topics = classify_topics(media_url)
        keywords = extract_keywords(media_url)
        quality = score_quality(media_url)

        metadata = {
            "media_id": media_id,
            "language": language,
            "topics": topics,
            "keywords": keywords,
            "quality_score": quality,
            "status": "ANALYZED"
        }

        save_metadata(metadata)
        publish_event("MediaMetadataUpdated", metadata)

        log.info("AI analysis completed", extra={"media_id": media_id})

    except Exception as e:
        log.error("AI analysis failed", extra={"media_id": media_id, "error": str(e)})
