import streamlit as st

def render_sidebar():
    st.sidebar.header("Paramètres")

    return {
        "capital_initial": st.sidebar.number_input("Capital initial ($)", 0, 1000000, 5000),
        "monthly": st.sidebar.number_input("Versement mensuel ($)", 0, 10000, 200),
        "rate": st.sidebar.slider("Rendement annuel (%)", 0, 50, 5),
        "fee": st.sidebar.slider("Frais de gestion (%)", 0, 5, 2),
        "years": st.sidebar.slider("Durée (années)", 1, 60, 20)
    }
