from utils.predict import predict_news

text = input("Enter news: ")

label, confidence = predict_news(text)

print(f"\nPrediction: {label}")
print(f"Confidence: {confidence:.2f}%")