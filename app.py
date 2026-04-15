# import streamlit as st
# from utils.predict import predict_news

# # Page config
# st.set_page_config(page_title="Fake News Detector", page_icon="📰")

# # Title
# st.title("📰 Fake News Detection System")
# st.write("developed by Dayansh Kuroliya")
# st.write("Detect whether a news article is Real or Fake using AI")

# # Input box
# user_input = st.text_area("Enter News Text Here:")

# # Button
# if st.button("Analyze News"):

#     if user_input.strip() == "":
#         st.warning("⚠️ Please enter some text")
#     else:
#         label, confidence = predict_news(user_input)

#         # Display result
#         if "Fake" in label:
#             st.error(f"{label}")
#         else:
#             st.success(f"{label}")

#         st.write(f"**Confidence:** {confidence:.2f}%")

#         # Basic explanation
#         st.subheader("Explanation:")
#         if confidence < 60:
#             st.write("Model is not very confident. Text may be ambiguous.")
#         elif "Fake" in label:
#             st.write("This news may contain misleading or exaggerated claims.")
#         else:
#             st.write("This news appears to be factual and neutral.")
#=====================================================================================================

# better ui development :-
from utils.recommender import get_similar_news
import streamlit as st
from utils.predict import predict_news

import base64

def set_bg():
    with open("assets/background.jpg", "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    page_bg = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}

    /* Optional: make text readable */
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.6);
        z-index: 0;
    }}

    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

set_bg()



# Page config
st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered")

# Title
st.title("📰 AI Fake News Detection System")
st.markdown("### Analyze news using Machine Learning")

# Sidebar
st.sidebar.header("About")
st.sidebar.write("This system detects whether a news article is Fake or Real using AI.")

# Session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# Input box
user_input = st.text_area("Enter News Text Here:")

# Analyze button
if st.button("🔍 Analyze News"):

    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text")
    else:
        label, confidence, reason = predict_news(user_input)

        # Save to history
        st.session_state.history.append((user_input, label, confidence))

        # Result
        st.subheader("Result")

        if "Fake" in label:
            st.error(label)
        else:
            st.success(label)

        # Confidence bar
        st.write(f"**Confidence:** {confidence:.2f}%")
        st.progress(int(confidence))

        # Explanation
        st.subheader("🧠 Explanation")
        st.write(reason)

        if confidence < 60:
            st.info("Low confidence → Text is unclear or mixed.")
        elif "Fake" in label:
            st.error("Possible misleading or exaggerated content detected.")
        else:
            st.success("Content appears factual and neutral.")

        # Category detection (simple rule-based)
        st.subheader("🏷️ Category")

        text = user_input.lower()

        if "government" in text or "policy" in text:
            st.write("Politics 🏛️")
        elif "health" in text or "doctor" in text:
            st.write("Health 🏥")
        elif "technology" in text or "ai" in text:
            st.write("Technology 💻")
        elif "sports" in text:
            st.write("Sports ⚽")
        else:
            st.write("General 📰")

# Show real news suggestions if fake
        if "Fake" in label:
            st.subheader("📰 Related Real News")

            suggestions = get_similar_news(user_input)

            for i, news in enumerate(suggestions, 1):
                st.write(f"{i}. {news}...")

        
# Show history
st.subheader("📜 Recent Predictions")

if st.session_state.history:
    for item in reversed(st.session_state.history[-5:]):
        st.write(f"➡️ {item[1]} ({item[2]:.2f}%)")
else:
    st.write("No history yet")