import yake

def extract_keywords(media_url):
    transcript = load_transcript(media_url)
    kw_extractor = yake.KeywordExtractor(top=5)
    keywords = kw_extractor.extract_keywords(transcript)
    return [kw for kw, score in keywords]
