import streamlit as st
import openai
import json
import tempfile

# --- SET YOUR VALID OPENAI KEY HERE ---
openai.api_key = "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"

def load_patient_data():
    with open("data/mock_patients.json", "r") as file:
        return json.load(file)

def transcribe_audio(audio_bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
        temp_audio_file.write(audio_bytes)
        temp_audio_file.flush()
        with open(temp_audio_file.name, "rb") as audio_file:
            transcript = openai.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
            return transcript.text

def render():
    st.header("Write Chief Complaints")

    patient_id = st.text_input("Patient ID")
    if not patient_id:
        return

    patients = load_patient_data()
    patient = next((p for p in patients if p["id"] == patient_id), None)

    if not patient:
        st.error("Patient ID not found.")
        return

    st.success(f"Patient Found: {patient['name']} ({patient['age']} y/o, {patient['gender']})")

    st.subheader("🎙️ Upload or Record Audio")

    audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])
    transcribed_text = ""

    if audio_file is not None:
        audio_bytes = audio_file.read()
        with st.spinner("Transcribing..."):
            try:
                transcribed_text = transcribe_audio(audio_bytes)
                st.success("Transcription Complete")
            except Exception as e:
                st.error(f"Transcription failed: {e}")

    complaint = st.text_area("Chief Complaint", value=transcribed_text, height=100)

    if st.button("Submit Complaint"):
        st.session_state[f"{patient_id}_chief_complaint"] = complaint
        st.success(f"Complaint for {patient['name']} submitted.")
