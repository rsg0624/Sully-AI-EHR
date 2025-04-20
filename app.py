import streamlit as st
from ehr_write import auth, chief_complaints, soap_notes, medications, referrals, view_patient

st.set_page_config(page_title="EHR Write Prototype")

st.title("EHR Write Prototype")

user = auth.login()

if user:
    st.sidebar.success(f"Logged in as {user}")
    module = st.sidebar.radio("Select Module", [
        "Chief Complaints", "SOAP Notes", "Medications", "Referrals", "View Patient Record"
    ])

    if module == "Chief Complaints":
        chief_complaints.render()
    elif module == "SOAP Notes":
        soap_notes.render()
    elif module == "Medications":
        medications.render()
    elif module == "Referrals":
        referrals.render()
    elif module == "View Patient Record":
        view_patient.render()
else:
    st.warning("Please log in to continue.")