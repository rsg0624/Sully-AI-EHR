import streamlit as st
import json
import os

def load_patients():
    with open("data/mock_patients.json", "r") as f:
        return json.load(f)

def save_patients(patients):
    with open("data/mock_patients.json", "w") as f:
        json.dump(patients, f, indent=2)

def render():
    st.header("Create Patient Record")

    patient_id = st.text_input("Patient ID")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    phone = st.text_input("Phone")
    email = st.text_input("Email (optional)")
    address = st.text_area("Address (optional)")

    if st.button("Create Patient"):
        if not patient_id or not name or not phone:
            st.error("Patient ID, Name, and Phone are required.")
            return

        patients = load_patients()
        if any(p["id"] == patient_id for p in patients):
            st.error("A patient with this ID already exists.")
            return

        new_patient = {
            "id": patient_id,
            "name": name,
            "age": age,
            "gender": gender,
            "phone": phone,
            "email": email,
            "address": address
        }
        patients.append(new_patient)
        save_patients(patients)
        st.success("Patient record created successfully!")