import streamlit as st

def init_state():
    if "scenarios" not in st.session_state:
        st.session_state.scenarios = []
        
        