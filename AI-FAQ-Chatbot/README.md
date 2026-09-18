# 🤖 AI FAQ Chatbot

An AI-powered FAQ chatbot for e-commerce customer support using Natural Language Processing (NLP), TF-IDF, and Cosine Similarity.

## 📌 Overview

This project was developed as part of the **CodeAlpha Artificial Intelligence Internship**.

The chatbot allows users to ask questions about common e-commerce topics such as orders, shipping, payments, returns, refunds, and customer support.

Instead of generating new answers, the system searches through a predefined FAQ dataset and retrieves the most relevant answer based on text similarity.

## ✨ Features

* 💬 Interactive chatbot interface
* 🔎 FAQ retrieval using Natural Language Processing
* 🧹 Text preprocessing using NLTK
* 📊 TF-IDF text vectorization
* 📐 Cosine Similarity for question matching
* 🎯 Similarity threshold for unknown questions
* 🖥️ Streamlit web interface
* 📚 E-commerce customer support FAQ dataset

## 🧠 How It Works

The chatbot follows this pipeline:

```text
User Question
      ↓
Text Preprocessing
      ↓
TF-IDF Vectorization
      ↓
Cosine Similarity
      ↓
Find Best Matching FAQ
      ↓
Threshold Check
      ↓
Return Answer / Fallback
```

### 1. Text Preprocessing

The input text is processed using NLTK.

The preprocessing steps include:

* Lowercasing
* Removing punctuation
* Tokenization
* Stopword removal
* Lemmatization

### 2. TF-IDF

The cleaned FAQ questions are converted into numerical vectors using **TF-IDF (Term Frequency-Inverse Document Frequency)**.

TF-IDF gives more importance to words that are useful for distinguishing between different questions.

### 3. Cosine Similarity

The user's question is compared with all FAQ questions using **Cosine Similarity**.

The FAQ with the highest similarity score is selected as the best match.

### 4. Similarity Threshold

A threshold is used to prevent the chatbot from returning an unrelated answer when the similarity score is too low.

If the score is below the threshold, the chatbot returns:

> I'm sorry, I don't have an answer for that.

## 📂 Project Structure

```text
Chatbot for FAQs/
│
├── app.py
├── chatbot.py
├── faq_dataset.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## 🛠️ Technologies

* Python
* NLTK
* Pandas
* Scikit-learn
* TF-IDF
* Cosine Similarity
* Streamlit
* Git & GitHub

## 📊 Dataset

The dataset contains **170 FAQ questions** covering 17 e-commerce customer support categories.

Categories include:

* Track Order
* Shipping Time
* Cancel Order
* Payment Methods
* Return Product
* Password Reset
* Refund
* Discounts
* Change Email
* Product Availability
* Change Shipping Address
* International Shipping
* Delayed Package
* Lost Package
* Damaged Product
* Exchange Product
* Customer Support

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yomnaelameer/CodeAlpha_AI_FAQ_Chatbot.git
```

Navigate to the project directory:

```bash
cd CodeAlpha_AI_FAQ_Chatbot
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 💡 Example Questions

Try questions such as:

```text
How can I track my order?
```

```text
What payment methods do you accept?
```

```text
How can I return a product?
```

```text
How long does shipping take?
```

```text
How can I get a refund?
```

## ⚠️ Limitations

The current chatbot uses **TF-IDF and Cosine Similarity**, which mainly rely on lexical similarity between words.

This means that two questions with similar meanings but different vocabulary may not always receive the correct answer.

For example:

```text
How can I track my order?
```

and

```text
How can I find my order?
```

may not always be recognized as semantically equivalent.

## 🚀 Future Improvements

Possible improvements include:

* Sentence Transformers
* Semantic Embeddings
* Better intent matching
* Larger FAQ datasets
* Conversation memory
* Multilingual support
* Advanced confidence scoring
* Database integration

## 🎓 Internship

This project was developed as part of the:

**CodeAlpha Artificial Intelligence Internship — September 2026**

## 👩‍💻 Author

**Yomna Mohamed Elameer**

GitHub:
https://github.com/yomnaelameer
