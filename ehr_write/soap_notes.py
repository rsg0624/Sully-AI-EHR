import streamlit as st
import json

def load_patient_data():
    with open("data/mock_patients.json", "r") as file:
        return json.load(file)

def render():
    st.header("Write SOAP Notes")
    patient_id = st.text_input("Patient ID")
    if patient_id:
        patients = load_patient_data()
        patient = next((p for p in patients if p["id"] == patient_id), None)
        if patient:
            st.success(f"Patient Found: {patient['name']} ({patient['age']} y/o, {patient['gender']})")
            subjective = st.text_area("Subjective")
            objective = st.text_area("Objective")
            assessment = st.text_area("Assessment")
            plan = st.text_area("Plan")
            if st.button("Submit SOAP Notes"):
                st.session_state[f"{patient_id}_soap"] = {
                    "Subjective": subjective,
                    "Objective": objective,
                    "Assessment": assessment,
                    "Plan": plan
                }
                st.success(f"SOAP notes for {patient['name']} submitted.")
        else:
            st.error("Patient ID not found.")