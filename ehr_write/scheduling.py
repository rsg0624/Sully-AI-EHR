import streamlit as st
import json
from datetime import datetime

def load_json(file_name):
    with open(file_name, "r") as f:
        return json.load(f)

def save_json(file_name, data):
    with open(file_name, "w") as f:
        json.dump(data, f, indent=2)

def render():
    st.header("Appointment Scheduling")

    patients = load_json("data/mock_patients.json")
    doctors = load_json("data/mock_doctors.json")
    appointments = load_json("data/appointments.json")

    st.subheader("Search Patients")
    search_phone = st.text_input("Search by Phone")
    search_name = st.text_input("Search by Name")

    found_patients = [p for p in patients if 
        (search_phone and search_phone in p.get("phone", "")) or
        (search_name and search_name.lower() in p.get("name", "").lower())
    ]

    for p in found_patients:
        st.markdown(f"- **{p.get('name', 'Unknown')}** ({p.get('phone', '-')})")

    st.subheader("Create New Appointment")
    patient_id = st.selectbox("Select Patient", [p["id"] for p in patients])
    doctor_id = st.selectbox("Select Doctor", [d["id"] + " - " + d["name"] for d in doctors])
    date = st.date_input("Select Date")
    time = st.time_input("Select Time")

    if st.button("Book Appointment"):
        new_appt = {
            "patient_id": patient_id,
            "doctor_id": doctor_id.split(" - ")[0],
            "date": date.strftime("%Y-%m-%d"),
            "time": time.strftime("%H:%M")
        }
        appointments.append(new_appt)
        save_json("data/appointments.json", appointments)
        st.success("Appointment booked!")

    st.subheader("All Appointments")
    for appt in appointments:
        st.write(appt)