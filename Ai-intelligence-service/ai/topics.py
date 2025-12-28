from sklearn.feature_extraction.text import TfidfVectorizer

def classify_topics(media_url):
    transcript = load_transcript(media_url)
    vectorizer = TfidfVectorizer(stop_words="english", max_features=5)
    features = vectorizer.fit_transform([transcript])
    return vectorizer.get_feature_names_out().tolist()
