import streamlit as st
import openai
import whisper

model = whisper.load_model("base")

audio_file = st.file_uploader("Upload a file")

if audio_file is not None:
    result = model.transcribe(audio_file.name)
    st.write(result["text"])
    st.write(audio_file.name)
