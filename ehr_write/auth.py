import streamlit as st

def login():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "username" not in st.session_state:
        st.session_state["username"] = ""

    if not st.session_state["logged_in"]:
        st.sidebar.header("Login")
        username_input = st.sidebar.text_input("Username", key="username_input")
        password_input = st.sidebar.text_input("Password", type="password", key="password_input")
        if st.sidebar.button("Login"):
            if username_input and password_input:
                st.session_state["logged_in"] = True
                st.session_state["username"] = username_input
                st.rerun()

    if st.session_state["logged_in"]:
        return st.session_state["username"]

    return None