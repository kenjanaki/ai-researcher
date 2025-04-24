import streamlit as st

def render_interface():
    with st.form("research_form"):
        query = st.text_input("Enter your research question:")
        add_summary = st.checkbox("Include Summary", value=True)
        submitted = st.form_submit_button("Run Research")
    return query, add_summary, submitted