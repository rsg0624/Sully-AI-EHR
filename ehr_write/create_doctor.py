import streamlit as st
import json
import os

def load_doctors():
    with open("data/mock_doctors.json", "r") as f:
        return json.load(f)

def save_doctors(doctors):
    with open("data/mock_doctors.json", "w") as f:
        json.dump(doctors, f, indent=2)

def render():
    st.header("Create Doctor Record")

    doctor_id = st.text_input("Doctor ID")
    name = st.text_input("Doctor Name")
    specialty = st.text_input("Specialty")
    phone = st.text_input("Phone (optional)")
    email = st.text_input("Email (optional)")
    npi = st.text_input("NPI (optional)")

    if st.button("Create Doctor"):
        if not doctor_id or not name or not specialty:
            st.error("Doctor ID, Name, and Specialty are required.")
            return

        doctors = load_doctors()
        if any(d["id"] == doctor_id for d in doctors):
            st.error("A doctor with this ID already exists.")
            return

        new_doctor = {
            "id": doctor_id,
            "name": name,
            "specialty": specialty,
            "phone": phone,
            "email": email,
            "npi": npi
        }
        doctors.append(new_doctor)
        save_doctors(doctors)
        st.success("Doctor record created successfully!")