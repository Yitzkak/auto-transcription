import streamlit as st
import openai
import whisper
from tempfile import NamedTemporaryFile
import os

audio_file = st.file_uploader("Upload a file")

model = whisper.load_model("base")

if audio_file is not None:
    # Save the uploaded audio file to a temporary file
    temp_file = NamedTemporaryFile(delete=False, suffix=".mp3")
    temp_file.write(audio_file.read())
    temp_file.close()

    # Transcribe using the temporary file
    result = model.transcribe(temp_file.name)

    # Display the result
    st.write(result["text"])
    st.write(temp_file.name)

    # Clean up: Remove the temporary file
    os.remove(temp_file.name)
