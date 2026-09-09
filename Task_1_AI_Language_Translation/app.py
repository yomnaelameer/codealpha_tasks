import streamlit as st
from translator import translate_text


# Page configuration
st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌐",
    layout="centered"
)


# Application title
st.title("🌐 AI Language Translation Tool")
st.markdown(
    "Translate text quickly and easily between different languages."
)


# Supported languages
languages = {
    "English": "en",
    "Arabic": "ar",
    "French": "fr",
    "Spanish": "es",
    "German": "de"
}


# Language selection
col1, col2 = st.columns(2)

with col1:
    source_lang_name = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target_lang_name = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=1
    )


# Text input
user_text = st.text_area(
    "Enter text to translate:",
    height=150,
    placeholder="Write your text here..."
)


# Translation button
if st.button("Translate ✨", type="primary"):

    if not user_text.strip():
        st.warning("Please enter some text first.")

    elif source_lang_name == target_lang_name:
        st.info("Source and target languages are the same.")

    else:
        source_code = languages[source_lang_name]
        target_code = languages[target_lang_name]

        try:
            translated = translate_text(
                user_text,
                source_lang=source_code,
                target_lang=target_code
            )

            st.success("Translation completed! ✅")

            st.write("### Translated Text")

            st.code(translated)

        except Exception as error:
            st.error(
                f"Translation failed: {error}"
            )