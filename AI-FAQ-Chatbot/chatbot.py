import pandas as pd
import nltk
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# Download NLTK resources
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


# Text preprocessing
def preprocess_text(text):

    text = text.lower()

    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    tokens = text.split()

    tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
    ]

    return " ".join(tokens)


# Load FAQ dataset
faq_data = pd.read_csv("faq_dataset.csv")

print(faq_data.columns)


# Get questions and answers
questions = faq_data["Question"]
answers = faq_data["Answer"]


# Preprocess FAQ questions
questions = questions.apply(preprocess_text)

print(questions)
print(answers)


# TF-IDF Vectorization
vectorizer = TfidfVectorizer()

faq_vectors = vectorizer.fit_transform(questions)

print(faq_vectors)


# Find the best answer
def get_answer(user_question):

    # Preprocess user question
    clean_question = preprocess_text(user_question)

    # Convert user question to TF-IDF vector
    user_vector = vectorizer.transform([clean_question])

    # Calculate similarity
    similarities = cosine_similarity(
        user_vector,
        faq_vectors
    )

    # Get the index of the best match
    best_match = similarities.argmax()

    print("User question:", user_question)
    print("Best match:", questions.iloc[best_match])
    print("Best score:", similarities[0][best_match])

    # Get the corresponding answer
    answer = answers.iloc[best_match]

    # Set threshold
    threshold = 0.5

    # Check similarity score
    if similarities[0][best_match] < threshold:
        return "I'm sorry, I don't have an answer for that."

    else:
        return answer


# Chatbot loop
# while True:

#     user_question = input("Ask your question: ")

#     # Exit chatbot
#     if user_question.lower() == "exit":
#         print("Goodbye!")
#         break

#     # Get answer
#     answer = get_answer(user_question)

#     print(f"Answer: {answer}")