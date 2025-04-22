import streamlit as st
from ui.style import apply_custom_style
from ui.layout import render_interface
from app_logic.workflow import run_research

st.set_page_config(page_title="Deep Research AI", layout="centered")
apply_custom_style()

if "result" not in st.session_state:
    st.session_state.result = None

title, query, add_summary, submitted = render_interface()

if submitted and query:
    st.session_state.result = run_research(query, add_summary)

if st.session_state.result:
    result = st.session_state.result

    if result.get("thinking"):
            with st.expander("Internal Reasoning"):
                st.markdown(result["thinking"])

    st.subheader("Answer")
    st.markdown(result["answer"])    

    if result.get("summary"):
        st.subheader("Summary")
        st.markdown(result["summary"])

    if st.button("Ask another question"):
        st.session_state.result = None
        st.experimental_rerun()