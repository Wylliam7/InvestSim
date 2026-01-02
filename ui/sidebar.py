import streamlit as st

def render_sidebar():
    st.sidebar.header("Paramètres de la simulation")

    capital_initial = st.sidebar.number_input(
        "Capital initial ($)", min_value=0, value=10000, step=1000
    )
    monthly = st.sidebar.number_input(
        "Versement mensuel ($)", min_value=0, value=200, step=50
    )
    rate = st.sidebar.number_input(
        "Rendement annuel (%)", min_value=0.0, value=5.0, step=0.1
    )
    fee = st.sidebar.number_input(
        "Frais annuels (%)", min_value=0.0, value=1.0, step=0.1
    )
    years = st.sidebar.number_input(
        "Nombre d'années", min_value=1, value=20, step=1
    )

    return {
        "capital_initial": capital_initial,
        "monthly": monthly,
        "rate": rate,
        "fee": fee,
        "years": years
    }
