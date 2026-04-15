# 📰 AI Fake News Detection System

An AI-powered system that detects whether a news article is **Real or Fake** using a hybrid approach combining Machine Learning and Rule-Based Detection.

---

## 🚀 Features

- ✅ Fake / Real News Classification  
- 📊 Confidence Score Visualization  
- 🧠 Explanation of Prediction  
- 📰 Real News Suggestions (for fake inputs)  
- ⚡ Hybrid Model (ML + Rule-Based)  
- 🎨 Interactive Web UI (Streamlit)  
- 📜 Recent Prediction History  

---

## 🧠 Approach

Our system uses a **hybrid architecture**:

1. **Rule-Based Detection**
   - Detects unrealistic or fictional claims (e.g., aliens, magic)
   - Improves reliability for edge cases

2. **Machine Learning Model**
   - TF-IDF Vectorization
   - Logistic Regression Classifier
   - Trained on labeled dataset (Fake & Real news)

3. **Similarity Engine**
   - Suggests real news using cosine similarity

---

## 📊 Results

- **Accuracy:** 98.63%  
- **F1-Score:** ~0.99  
- Strong performance on structured datasets  

---

## 🛠️ Tech Stack

- Python  
- Scikit-learn  
- Pandas  
- Streamlit  
- NLP (TF-IDF)  

---

fake-news-nlp/
│
├── app.py # Streamlit UI
├── train.py # Model training
├── test_predict.py # Testing script
├── utils/
│ ├── predict.py # Prediction logic
│ └── recommender.py # Real news suggestion
├── assets/ # Images (UI background)
├── README.md


---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py

## 📂 Project Structure
