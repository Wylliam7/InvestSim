import streamlit as st

def render_sidebar_simulation_frais():
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
    palier = st.sidebar.number_input(
        "Palier à visualiser ($)", min_value=1_000, value=100_000, step=1_000
    )
    max_paliers = st.sidebar.number_input(
        "Nombre maximal de paliers à afficher",min_value=1,value=10, step=1
    )

    return {
        "capital_initial": capital_initial,
        "monthly": monthly,
        "rate": rate,
        "fee": fee,
        "years": years,
        "palier": palier,
        "max_paliers": max_paliers
    }
   
   
   
def render_sidebar_paliers():
    st.sidebar.header("Paramètres de la simulation")

    capital_initial = st.sidebar.number_input(
        "Capital initial ($)", value=10_000, step=1_000
    )
    monthly = st.sidebar.number_input(
        "Versement mensuel ($)", value=200, step=50
    )
    rate = st.sidebar.number_input(
        "Rendement annuel (%)", value=5.0, step=0.1
    )
    years = st.sidebar.number_input(
        "Durée (années)", value=20, step=1
    )
    palier = st.sidebar.number_input(
        "Grandeur des paliers ($)", min_value=1_000, value=100_000, step=1_000
    )
    max_paliers = st.sidebar.number_input(
        "Nombre de paliers à afficher", min_value=1, value=10, step=1
    )

    return {
        "capital_initial": capital_initial,
        "monthly": monthly,
        "rate": rate,
        "years": years,
        "palier": palier,
        "max_paliers": max_paliers
    }
