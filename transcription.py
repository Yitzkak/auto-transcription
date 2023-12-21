import streamlit as st
import openai

API_KEY = st.secrets["API_KEY"]
model_id = "whisper-1"

audio = st.file_uploader("Upload a file")

if audio is not None:
    audio_file_path = audio.name 
    audio_file = open(audio_file_path, "rb")
    transcript = openai.Audio.transcribe(model_id, audio_file, API_KEY)
    st.write(transcript)
