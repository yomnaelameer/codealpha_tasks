# 🌐 AI Language Translation Tool

A simple and user-friendly AI Language Translation Tool built with Python and Streamlit.

The application allows users to enter text, select a source language and a target language, and translate the text using the MyMemory Translation API.

## ✨ Features

* Translate text between multiple languages.
* Supports:

  * English
  * Arabic
  * French
  * Spanish
  * German
* Simple and clean Streamlit interface.
* Input validation.
* Error handling for API requests.
* Fast translation using a REST API.

## 🛠️ Technologies Used

* Python
* Streamlit
* Requests
* REST API
* JSON
* MyMemory Translation API

## 📂 Project Structure

```text
AI-Language-Translation-Tool/
│
├── app.py
├── translator.py
├── run.bat
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Language-Translation-Tool.git
```

### 2. Open the project folder

```bash
cd AI-Language-Translation-Tool
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

Or on Windows, you can simply run:

```text
run.bat
```

## 🚀 How to Use

1. Select the source language.
2. Select the target language.
3. Enter the text you want to translate.
4. Click **Translate ✨**.
5. The translated text will be displayed.

## 🔌 API

This project uses the **MyMemory Translation API** to perform translations.

The application sends the entered text and selected language pair to the API and processes the returned JSON response.

## 🎯 Project Goal

This project was created as part of the **CodeAlpha Artificial Intelligence Internship** to practice:

* Working with REST APIs
* Sending HTTP requests using Python
* Processing JSON responses
* Building a user interface with Streamlit
* Structuring a Python project
* Using Git and GitHub

## 👩‍💻 Author

**Yomna Elameer**

Computer Science Student
