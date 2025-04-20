import streamlit as st
import json

def load_patient_data():
    with open("data/mock_patients.json", "r") as file:
        return json.load(file)

def render():
    st.header("Patient Overview")
    patient_id = st.text_input("Enter Patient ID")
    if not patient_id:
        return

    patients = load_patient_data()
    patient = next((p for p in patients if p["id"] == patient_id), None)

    if not patient:
        st.error("Patient not found.")
        return

    st.success(f"{patient['name']} ({patient['age']} y/o, {patient['gender']})")

    st.subheader("Chief Complaint")
    st.write(st.session_state.get(f"{patient_id}_chief_complaint", "Not recorded"))

    st.subheader("SOAP Notes")
    st.write(st.session_state.get(f"{patient_id}_soap", "Not recorded"))

    st.subheader("Medication")
    st.write(st.session_state.get(f"{patient_id}_meds", "Not recorded"))

    st.subheader("Referral")
    st.write(st.session_state.get(f"{patient_id}_referral", "Not recorded"))