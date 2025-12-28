def media_analysis_prompt(transcript: str) -> str:
    return f"""
You are an AI system analyzing audio content.

Given the transcript below:
1. Detect the primary language
2. Classify the main topics (max 3)
3. Extract 5 important keywords

Respond ONLY in valid JSON:
{{
  "language": "...",
  "topics": ["...", "..."],
  "keywords": ["...", "..."]
}}

Transcript:
{transcript}
"""
