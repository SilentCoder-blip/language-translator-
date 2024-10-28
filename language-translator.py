import streamlit as st
from transformers import pipeline
from gtts import gTTS
import tempfile

# Load the translation pipeline from Hugging Face
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-hi")

# Translation Function Using Hugging Face Pipeline
def translate_text(text, src_lang, dest_lang):
    # Here we only support "en" to "hi" for demonstration; expand with more models for additional languages
    if src_lang == "en" and dest_lang == "hi":
        translated_text = translator(text, src_lang=src_lang, tgt_lang=dest_lang)
        return translated_text[0]['translation_text']
    else:
        return "Currently, only English to Hindi translation is supported in this example."

# Text-to-Speech Function
def text_to_speech(text, lang):
    tts = gTTS(text=text, lang=lang)
    temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_audio.name)
    return temp_audio.name

# Streamlit Interface
def main():
    st.title("Multilingual Translator and TTS")

    # Language Options
    languages = {
        'English': 'en',
        'Hindi': 'hi'
    }

    # Language Selection
    src_lang = st.selectbox("Select Input Language", list(languages.keys()))
    dest_lang = st.selectbox("Select Output Language", list(languages.keys()))

    # Input Text
    text = st.text_area("Enter Text to Translate")

    # Translation and Display
    if st.button("Translate"):
        translated_text = translate_text(text, languages[src_lang], languages[dest_lang])
        st.write("Translated Text:", translated_text)

        # TTS and Playback
        if st.button("Play Translation"):
            audio_file = text_to_speech(translated_text, languages[dest_lang])
            with open(audio_file, "rb") as file:
                audio_bytes = file.read()
                st.audio(audio_bytes, format="audio/mp3")
                st.download_button("Download Audio", audio_bytes, file_name="translation.mp3", mime="audio/mp3")

# Run the app
if __name__ == '__main__':
    main()
