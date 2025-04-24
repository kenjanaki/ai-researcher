import streamlit as st
from ui.style import apply_custom_style
from ui.layout import render_interface
from app_logic.workflow import run_research
from app_logic.nodes import init_agents

st.set_page_config(page_title="Deep Research AI", layout="centered")
apply_custom_style()

st.title("Researcher")

# Initialize the agent variables
research_node, answer_node, summarizer_node = None, None, None

# Initialize keys and agents only if the user hasn't already entered them
if "keys_entered" not in st.session_state:
    st.session_state.keys_entered = False

if not st.session_state.keys_entered:
    # Ask for API keys if they are not entered
    tavily_key = st.text_input("Enter Tavily API Key:", type="password")
    groq_key = st.text_input("Enter Groq API Key:", type="password")

    if tavily_key and groq_key:
        # Store the keys in session state and initialize agents
        st.session_state.tavily_key = tavily_key
        st.session_state.groq_key = groq_key
        st.session_state.keys_entered = True
        
        # Initialize agents with the entered API keys
        research_node, answer_node, summarizer_node = init_agents(tavily_key, groq_key)
        
        # Automatically rerun the app to clear the API input fields
        st.rerun()
else:
    # API keys have been entered, display success message
    st.info("API Keys loaded successfully!")
    # Initialize agents from session state
    research_node, answer_node, summarizer_node = init_agents(st.session_state.tavily_key, st.session_state.groq_key)

# Once the keys are entered and agents are initialized, handle the research flow
if research_node and answer_node and summarizer_node:
    if "result" not in st.session_state:
        st.session_state.result = None

    query, add_summary, submitted = render_interface()

    if submitted and query:
        # Perform the research and get the result
        st.session_state.result = run_research(query, add_summary, research_node, answer_node, summarizer_node)

    if st.session_state.result:
        result = st.session_state.result

        # Display the internal reasoning if available
        if result.get("thinking"):
            with st.expander("Internal Reasoning"):
                st.markdown(result["thinking"])

        # Display the answer
        st.subheader("Answer")
        st.markdown(result["answer"])

        # Display the summary if available
        if result.get("summary"):
            st.subheader("Summary")
            st.markdown(result["summary"])

        # Allow asking another question, which resets the result
        if st.button("Ask another question"):
            st.session_state.result = None
            st.rerun()
else:
    # If the API keys are not entered, show a warning
    st.warning("Please enter both Tavily and Groq API keys to proceed.")

