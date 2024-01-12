# Import necessary libraries
import streamlit as st
import whisper
from tempfile import NamedTemporaryFile
import os

# Set page title and introduction
st.title("Audio Transcription App")
st.write("This app allows you to transcribe audio files using the Whisper library.")

# Add a sidebar to the Streamlit app
st.sidebar.title("App Settings")

# Information section in the sidebar
st.sidebar.info(
    "This app allows you to transcribe audio files using the Whisper library."
)

# User input for their name
user_name = st.sidebar.text_input("Your Name")

# Select Whisper model version in the sidebar
model_version = st.sidebar.selectbox(
    "Select Whisper Model Version",
    ["base", "small", "medium", "large"],
    index=0  # Default selection
)

# File uploader widget to get user's audio file
audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

# Check if an audio file is uploaded
if audio_file is not None:
    # Display the uploaded audio file
    st.audio(audio_file, format='audio')

    # Load the Whisper model
    model = whisper.load_model(model_version)

    # Save the uploaded audio file to a temporary file
    temp_file = NamedTemporaryFile(delete=False, suffix=".mp3")
    temp_file.write(audio_file.read())
    temp_file.close()

    # Transcribe using the temporary file
    try:
        result = model.transcribe(temp_file.name)

        # Display the transcribed text in an editable area (editor)
        transcribed_text = st.text_area("Transcription Result", result["text"])

    except Exception as e:
        # Handle exceptions gracefully and provide a user-friendly error message
        st.error(f"Error occurred: {str(e)}")

    finally:
        # Clean up: Remove the temporary file
        os.remove(temp_file.name)

# Provide additional information and tips
st.info("Note: This app uses the Whisper library for audio transcription. Ensure your audio file is in a supported format (e.g., mp3, wav).")

# Footer with attribution and source code link
st.markdown("---")
st.write("Created by: Yitzkak")
st.write("[Source Code](https://github.com/Yitzkak/auto-transcription)")

# Additional resources or instructions for beginners
st.markdown("### Additional Resources:")
st.write("- [Streamlit Documentation](https://docs.streamlit.io)")
st.write("- [Whisper Documentation](https://whisper-ASR.readthedocs.io)")

# Acknowledge and thank the libraries used
st.markdown("### Special Thanks:")
st.write("- Streamlit for easy UI creation")
st.write("- Whisper for audio transcription capabilities")
