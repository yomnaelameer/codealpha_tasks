import requests


def translate_text(text, source_lang, target_lang):
    url = "https://api.mymemory.translated.net/get"

    params = {
        "q": text,
        "langpair": f"{source_lang}|{target_lang}"
    }

    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    result = response.json()

    translated_text = result["responseData"]["translatedText"]

    return translated_text