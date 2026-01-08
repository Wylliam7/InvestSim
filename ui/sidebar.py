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

    return {
        "capital_initial": capital_initial,
        "monthly": monthly,
        "rate": rate,
        "fee": fee,
        "years": years,
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


def render_sidebar_objectif():
    st.sidebar.header("🎯 Objectif financier")

    current_age = st.sidebar.number_input(
        "Âge actuel", min_value=0, max_value=100, value=25
        )
    target_age = st.sidebar.number_input(
        "Âge objectif", min_value=0, max_value=120, value=65
        )

    target_amount = st.sidebar.number_input(
        "Montant objectif ($)", min_value=0.0, value=500000.0, step=10000.0
        )
    capital_initial = st.sidebar.number_input(
        "Capital initial ($)", min_value=0.0, value=0.0, step=1000.0
        )
    annual_return = st.sidebar.slider(
        "Rendement annuel (%)", 0.0, 15.0, 5.0, 0.1
        )
    annual_fee = st.sidebar.slider(
        "Frais de gestion (%)", 0.0, 3.0, 1.0, 0.1
        )

    return {
        "current_age": current_age,
        "target_age": target_age,
        "target_amount": target_amount,
        "capital_initial": capital_initial,
        "annual_return": annual_return,
        "annual_fee": annual_fee,
    }
