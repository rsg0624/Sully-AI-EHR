import streamlit as st
from ehr_write import auth, chief_complaints, soap_notes, medications, referrals, view_patient, clinical_data, scheduling, create_patient, create_doctor

st.set_page_config(page_title="Sully-EHR Platform")

st.title("EHR Write & Scheduling Platform")

user = auth.login()

if user:
    st.sidebar.success(f"Logged in as {user}")
    module = st.sidebar.radio("Select Module", [
        "Chief Complaints", "SOAP Notes", "Medications", "Referrals",
        "Clinical Data", "Scheduling", "View Patient Record", 
        "Create Patient Record", "Create Doctor Record"
    ])

    if module == "Chief Complaints":
        chief_complaints.render()
    elif module == "SOAP Notes":
        soap_notes.render()
    elif module == "Medications":
        medications.render()
    elif module == "Referrals":
        referrals.render()
    elif module == "Clinical Data":
        clinical_data.render()
    elif module == "Scheduling":
        scheduling.render()
    elif module == "View Patient Record":
        view_patient.render()
    elif module == "Create Patient Record":
        create_patient.render()
    elif module == "Create Doctor Record":
        create_doctor.render()
else:
    st.warning("Please log in to continue.")
