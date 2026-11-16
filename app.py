import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
nltk.download('punkt_tab')
nltk.download('stopwords')

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):

    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.markdown(
            '<div class="result-card spam">⚠️ SPAM DETECTED!</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="result-card ham">✓ NOT SPAM!</div>',
            unsafe_allow_html=True
        )

import base64
from pathlib import Path

# Load background image
image_path = Path(__file__).parent / "img.png"

with open(image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()


import base64

# Load background image
with open("img.png", "rb") as f:
    data = base64.b64encode(f.read()).decode()


# Apply background image
st.markdown(f"""
<style>
.stApp {{
    background-image: linear-gradient(
        rgba(0, 0, 0, 0.65),
        rgba(0, 0, 0, 0.65)
    ), url("data:image/jpeg;base64,{data}");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}
</style>
""", unsafe_allow_html=True)
st.markdown("""



<style>

/* 3D effect on movie posters */
.stImage img {
    transition: transform 0.4s ease, box-shadow 0.4s ease;
    border-radius: 12px;
}

.stImage img:hover {
    transform: perspective(1000px) rotateY(8deg) scale(1.08);
    box-shadow: 0px 15px 30px rgba(255, 0, 0, 0.4);
}

/* Button styling */
.stButton button {
    background-color: #e50914;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 25px;
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.08);
    box-shadow: 0 0 20px rgba(229, 9, 20, 0.7);
}

/* 3D Glassmorphism Input Box */
.stTextInput input {
    background: rgba(15, 15, 15, 0.75) !important;
    color: white !important;

    border: 1px solid rgba(255, 255, 255, 0.25) !important;
    border-radius: 14px !important;

    padding: 15px 18px !important;
    font-size: 17px !important;

    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);

    box-shadow:
        0 7px 0 rgba(0, 0, 0, 0.35),
        0 12px 25px rgba(0, 0, 0, 0.3),
        inset 0 1px 2px rgba(255, 255, 255, 0.12);

    transition: all 0.35s ease;
}

/* Input Hover Effect */
.stTextInput input:hover {
    border-color: #e50914 !important;
    transform: translateY(-3px);

    box-shadow:
        0 10px 0 rgba(0, 0, 0, 0.3),
        0 15px 30px rgba(229, 9, 20, 0.25);
}

/* Input Focus / Glow Effect */
.stTextInput input:focus {
    border: 1px solid #ff2530 !important;

    transform: translateY(-3px);

    box-shadow:
        0 0 0 3px rgba(229, 9, 20, 0.15),
        0 0 25px rgba(229, 9, 20, 0.4),
        0 10px 25px rgba(0, 0, 0, 0.3);
}

/* Placeholder Styling */
.stTextInput input::placeholder {
    color: rgba(255, 255, 255, 0.55) !important;
    font-size: 15px;
}

/* Input Label */
.stTextInput label {
    color: white !important;
    font-size: 17px !important;
    font-weight: 600 !important;
    margin-bottom: 10px;
}

/* Smooth Input Animation */
.stTextInput {
    transition: all 0.3s ease;
}

/* Text Area Styling */
.stTextArea textarea {
    background: rgba(15, 15, 15, 0.75) !important;
    color: white !important;

    border: 1px solid rgba(255, 255, 255, 0.25) !important;
    border-radius: 14px !important;

    padding: 16px !important;
    font-size: 16px !important;

    backdrop-filter: blur(15px);

    box-shadow:
        0 8px 0 rgba(0, 0, 0, 0.3),
        0 12px 25px rgba(0, 0, 0, 0.3);

    transition: all 0.3s ease;
}

.stTextArea textarea:focus {
    border-color: #e50914 !important;
    box-shadow: 0 0 22px rgba(229, 9, 20, 0.35);
}

/* ================================= */
/* SPAM RESULT - RED GLASS EFFECT */
/* ================================= */

.result-card.spam {
    display: block;
    margin-top: 30px;
    padding: 25px;

    text-align: center;
    font-size: 27px;
    font-weight: 800;
    letter-spacing: 1px;

    color: #ff526e;
    background: rgba(255, 30, 65, 0.16);

    border: 1px solid rgba(255, 60, 90, 0.8);
    border-radius: 18px;

    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);

    box-shadow:
        0 0 15px rgba(255, 40, 70, 0.3),
        0 0 35px rgba(255, 40, 70, 0.2),
        inset 0 0 15px rgba(255, 255, 255, 0.05);

    animation: spam-appear 0.8s ease;
}

/* ================================= */
/* NOT SPAM RESULT - GREEN GLASS */
/* ================================= */

.result-card.ham {
    display: block;
    margin-top: 30px;
    padding: 25px;

    text-align: center;
    font-size: 27px;
    font-weight: 800;
    letter-spacing: 1px;

    color: #40ffc0;
    background: rgba(0, 220, 150, 0.15);

    border: 1px solid rgba(0, 255, 180, 0.8);
    border-radius: 18px;

    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);

    box-shadow:
        0 0 15px rgba(0, 255, 170, 0.3),
        0 0 35px rgba(0, 255, 170, 0.2),
        inset 0 0 15px rgba(255, 255, 255, 0.05);

    animation: ham-appear 0.8s ease;
}

/* SPAM ANIMATION */
@keyframes spam-appear {
    0% {
        opacity: 0;
        transform: scale(0.8) translateY(20px);
    }

    60% {
        opacity: 1;
        transform: scale(1.04);
    }

    100% {
        transform: scale(1);
    }
}

/* NOT SPAM ANIMATION */
@keyframes ham-appear {
    0% {
        opacity: 0;
        transform: scale(0.8) translateY(20px);
    }

    60% {
        opacity: 1;
        transform: scale(1.04);
    }

    100% {
        transform: scale(1);
    }
}


</style>
""", unsafe_allow_html=True)
