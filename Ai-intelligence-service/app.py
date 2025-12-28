import json
import logging
from openai_client import analyze_text
from prompts import media_analysis_prompt
from quality import score_quality
from storage import save_metadata
from events import publish_event

log = logging.getLogger(__name__)

def analyze_media(event: dict):
    media_id = event["media_id"]
    transcript = event["transcript"]
    audio_path = event["audio_path"]

    log.info("AI analysis started", extra={"media_id": media_id})

    prompt = media_analysis_prompt(transcript)
    ai_response = analyze_text(prompt)

    ai_data = json.loads(ai_response)

    quality = score_quality(audio_path)

    metadata = {
        "media_id": media_id,
        "language": ai_data["language"],
        "topics": ai_data["topics"],
        "keywords": ai_data["keywords"],
        "quality_score": quality,
        "status": "ANALYZED"
    }

    save_metadata(metadata)
    publish_event("MediaMetadataUpdated", metadata)

    log.info("AI analysis completed", extra={"media_id": media_id})
