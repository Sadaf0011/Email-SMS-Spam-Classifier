# 📩 Email/SMS Spam Classifier

A Machine Learning-based Email/SMS Spam Classifier built using **Python, Natural Language Processing (NLP), TF-IDF Vectorization, and Streamlit**. This project predicts whether a given text message is Spam or Not Spam using a trained machine learning model.

## 🚀 Project Overview

The Email/SMS Spam Classifier analyzes the text entered by the user and classifies it into one of two categories:

- 🔴 **Spam:** Identifies unwanted or potentially fraudulent messages.
- 🟢 **Not Spam:** Identifies legitimate messages.

The application features an interactive Streamlit interface with a modern design and real-time predictions.

## ✨ Features

- Email and SMS spam detection.
- Text preprocessing using NLP techniques.
- Tokenization and removal of stopwords.
- Word stemming using Porter Stemmer.
- TF-IDF text vectorization.
- Machine Learning-based prediction.
- Interactive Streamlit web interface.
- Custom background and visual styling.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation |
| Scikit-learn | Machine Learning and TF-IDF |
| NLTK | Natural Language Processing |
| Pickle | Saving and loading trained models |
| Streamlit | Web application development |
| HTML & CSS | User interface styling |

## 🧠 NLP Workflow

The project follows these text preprocessing steps:

1. **Lowercasing:** Converts all text into lowercase.
2. **Tokenization:** Splits the message into individual words.
3. **Removing Special Characters:** Filters out unwanted characters.
4. **Stopword Removal:** Removes commonly used words that provide limited information.
5. **Stemming:** Converts words into their root forms using Porter Stemmer.
6. **TF-IDF Vectorization:** Converts processed text into numerical features.
7. **Prediction:** The trained machine learning model classifies the message as Spam or Not Spam.

## 📂 Project Structure

```text
Email-SMS-Spam-Classifier/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── img.png
├── requirements.txt
├── README.md
└── .gitignore
```

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Natural Language Processing (NLP).
- Text preprocessing and feature extraction.
- TF-IDF Vectorization.
- Machine Learning model integration.
- Building interactive applications using Streamlit.
- Deploying Python applications.

## 👩‍💻 Author

**Sadaf**

B.Tech Computer Science and Engineering (AI)

GitHub: [Sadaf0011](https://github.com/Sadaf0011)

---

⭐ If you find this project useful, consider giving it a star!
