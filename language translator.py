import streamlit as st
from googletrans import Translator
from gtts import gTTS
import tempfile

# Translation Function
def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

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
        'English': 'en', 'Hindi': 'hi', 'Bengali': 'bn', 'Tamil': 'ta',
        'Telugu': 'te', 'Marathi': 'mr', 'Kannada': 'kn', 'Gujarati': 'gu',
        'Malayalam': 'ml', 'Punjabi': 'pa'
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
