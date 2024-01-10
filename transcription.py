import streamlit as st
import openai
import whisper

API_KEY = st.secrets["API_KEY"]
model_id = "whisper-1"

audio_file = st.file_uploader("Upload a file")

<<<<<<< HEAD
model = whisper.load_model("base")

if audio_file is not None:
    result = model.transcribe(audio_file.name)
    st.write(result["text"])
    st.write(audio_file.name)
=======
if audio is not None:
    audio_file_path = audio.name 
    audio_file = open(audio_file_path, "rb")
    transcript = openai.Audio.transcribe(model_id, audio_file, API_KEY)
    st.write(transcript)
>>>>>>> 0eb1f779553e250d8c26b0d5ce61acc16a62e57b
