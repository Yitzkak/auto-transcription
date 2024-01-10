import streamlit as st
import openai
import whisper

API_KEY = "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 "
model_id = "whisper-1"

audio_file = st.file_uploader("Upload a file")

model = whisper.load_model("base")

if audio_file is not None:
    result = model.transcribe(audio_file.name)
    st.write(result["text"])
    st.write(audio_file.name)