# import pickle

# # Load model and vectorizer
# model = pickle.load(open("model/model.pkl", "rb"))
# vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

# def predict_news(text):
#     # Preprocess
#     text = text.lower()

#     # Transform
#     text_vec = vectorizer.transform([text])

#     # Predict
#     prediction = model.predict(text_vec)[0]
#     probability = model.predict_proba(text_vec)[0]

#     confidence = max(probability) * 100

#     if prediction == 0:
#         label = "Fake News ❌"
#     else:
#         label = "Real News ✅"

#     return label, confidence

#===================correction =========
import pickle

# Load model and vectorizer
model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

# 🚨 Rule-based keywords (can expand later)
fake_keywords = [
    "alien", "aliens", "ufo", "time travel", "zombie",
    "immortal", "magic", "superpower", "ghost",
    "cure cancer instantly", "miracle cure"
]

def predict_news(text):
    text_lower = text.lower()

    # Rule-based keywords
    fake_keywords = [
        "alien", "aliens", "ufo", "time travel", "zombie",
        "immortal", "magic", "ghost", "miracle cure"
    ]

    for word in fake_keywords:
        if word in text_lower:
            return "Fake News ❌", 95.0, f"Contains unrealistic term: '{word}'"

    # ML model
    text_vec = vectorizer.transform([text_lower])

    prediction = model.predict(text_vec)[0]
    probability = model.predict_proba(text_vec)[0]

    confidence = max(probability) * 100

    if prediction == 0:
        label = "Fake News ❌"
        reason = "Language pattern resembles misleading or exaggerated news"
    else:
        label = "Real News ✅"
        reason = "Content appears neutral and factual"

    return label, confidence, reason