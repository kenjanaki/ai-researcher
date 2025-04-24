import streamlit as st

def apply_custom_style():
    style = """
    <style>
    * {
        font-family: "Lucida Console", "Courier New", monospace !important;
    }

    body {
        background-color: #1e1e2f !important;
        color: #e0d7ff !important;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #cdb4ff !important;
        text-align: center;
    }

    /* Text input styles */
    .stTextInput > div > div > input {
        background-color: #2c2c4a !important;
        color: #e0d7ff !important;
        border-radius: 8px;
        border: 1px solid #6a4c93 !important;
    }

    .stTextInput > div > div > input:focus {
        outline: none !important;
        border: 1px solid white !important;
        box-shadow: 0 0 5px white !important;
    }

    /* Checkbox */
    input[type="checkbox"] {
        accent-color: #6a4c93 !important;
    }

    .stCheckbox > label {
        color: #cdb4ff !important;
    }

    /* Button styling */
    .stButton button {
        background-color: #6a4c93 !important;
        color: white !important;
        border-radius: 10px;
        border: none;
        transition: background-color 0.3s ease;
    }

    .stButton button:hover {
        background-color: #7b5aa7 !important;
    }

    /* Misc text and layout */
    .stExpanderHeader, .stMarkdown, .stText, .stSubheader, .stFormLabel {
        color: #e0d7ff !important;
    }
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)