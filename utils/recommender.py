import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# Load vectorizer
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

# Load real news
real_news = pd.read_csv("model/real_news.csv")

# Convert real news to vectors
real_vectors = vectorizer.transform(real_news["content"])

def get_similar_news(text, top_n=3):
    text_vec = vectorizer.transform([text])

    similarities = cosine_similarity(text_vec, real_vectors)[0]

    # Get top similar indices
    top_indices = similarities.argsort()[-top_n:][::-1]

    results = []
    for idx in top_indices:
        results.append(real_news["content"][idx][:200])  # show first 200 chars

    return results