import streamlit as st
import openai
import json

# --- USE SAME API KEY AS WHISPER ---
openai.api_key = "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"

def load_patient_data():
    with open("data/mock_patients.json", "r") as file:
        return json.load(file)

def generate_soap_notes(complaint):
    prompt = f"""
You are a clinical assistant. Based on the following chief complaint, generate a SOAP note:

Chief Complaint: "{complaint}"

Return only the SOAP sections in the following format:
Subjective: ...
Objective: ...
Assessment: ...
Plan: ...
"""

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )
    return response.choices[0].message.content

def render():
    st.header("Write SOAP Notes")

    patient_id = st.text_input("Patient ID")
    if not patient_id:
        return

    patients = load_patient_data()
    patient = next((p for p in patients if p["id"] == patient_id), None)

    if not patient:
        st.error("Patient ID not found.")
        return

    st.success(f"Patient Found: {patient['name']} ({patient['age']} y/o, {patient['gender']})")

    complaint = st.text_area("Chief Complaint (for AI)", placeholder="E.g. Patient has chest tightness...")
    if st.button("💡 Generate SOAP Notes"):
        with st.spinner("Generating SOAP Note..."):
            try:
                soap_text = generate_soap_notes(complaint)
                st.session_state["generated_soap"] = soap_text
            except Exception as e:
                st.error(f"Failed to generate SOAP: {e}")
                return

    soap = st.session_state.get("generated_soap", "")
    subj, obj, assess, plan = "", "", "", ""

    if soap:
        st.subheader("Generated SOAP Note")
        st.markdown(f"```text\n{soap}\n```")
        # Optionally split sections
        try:
            subj = soap.split("Subjective:")[1].split("Objective:")[0].strip()
            obj = soap.split("Objective:")[1].split("Assessment:")[0].strip()
            assess = soap.split("Assessment:")[1].split("Plan:")[0].strip()
            plan = soap.split("Plan:")[1].strip()
        except:
            pass

    subjective = st.text_area("Subjective", value=subj, height=100)
    objective = st.text_area("Objective", value=obj, height=100)
    assessment = st.text_area("Assessment", value=assess, height=100)
    plan = st.text_area("Plan", value=plan, height=100)

    if st.button("Submit SOAP Note"):
        st.session_state[f"{patient_id}_soap"] = {
            "Subjective": subjective,
            "Objective": objective,
            "Assessment": assessment,
            "Plan": plan
        }
        st.success("SOAP note submitted.")
