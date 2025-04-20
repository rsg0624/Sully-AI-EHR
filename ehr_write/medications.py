import streamlit as st
import json

def load_patient_data():
    with open("data/mock_patients.json", "r") as file:
        return json.load(file)

def render():
    st.header("Write Medications")
    patient_id = st.text_input("Patient ID")
    if patient_id:
        patients = load_patient_data()
        patient = next((p for p in patients if p["id"] == patient_id), None)
        if patient:
            st.success(f"Patient Found: {patient['name']} ({patient['age']} y/o, {patient['gender']})")
            medication = st.text_input("Medication Name")
            dosage = st.text_input("Dosage")
            frequency = st.text_input("Frequency")
            if st.button("Submit Medication"):
                st.session_state[f"{patient_id}_meds"] = {
                    "Medication": medication,
                    "Dosage": dosage,
                    "Frequency": frequency
                }
                st.success(f"Medication for {patient['name']} submitted.")
        else:
            st.error("Patient ID not found.")