import streamlit as st
from ui.style import apply_custom_style
from ui.layout import render_interface
from app_logic.workflow import run_research
from app_logic.nodes import init_agents

st.set_page_config(page_title="Deep Research AI", layout="centered")
apply_custom_style()

st.title("Researcher")

tavily_key, groq_key = None, None

research_node, answer_node, summarizer_node = init_agents(tavily_key, groq_key)

if research_node is None or answer_node is None or summarizer_node is None:
    if "keys_entered" not in st.session_state:
        st.session_state.keys_entered = False

    if not st.session_state.keys_entered:
        tavily_key = st.text_input("Enter Tavily API Key:", type="password")
        groq_key = st.text_input("Enter Groq API Key:", type="password")

        if tavily_key and groq_key:
            st.session_state.keys_entered = True
            research_node, answer_node, summarizer_node = init_agents(tavily_key, groq_key)

            st.rerun()

    else:
        st.info("API Keys loaded successfully!")

if research_node and answer_node and summarizer_node:
    if "result" not in st.session_state:
        st.session_state.result = None

    query, add_summary, submitted = render_interface()

    if submitted and query:
        st.session_state.result = run_research(query, add_summary, research_node, answer_node, summarizer_node)

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
            st.rerun()
else:
    st.warning("Please enter both Tavily and Groq API keys to proceed.")

for key in st.session_state.keys():
    del st.session_state[key]