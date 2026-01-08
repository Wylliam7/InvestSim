# pages/3_🎯_Objectif.py

import streamlit as st
from core.simulation import monthly_investment_for_goal
from ui.sidebar import render_sidebar_objectif

st.set_page_config(page_title="Objectif d'investissement", page_icon="🎯", layout="wide")
st.title("🎯 Objectif d'investissement")

params = render_sidebar_objectif()

try:
    monthly_needed = monthly_investment_for_goal(
        current_age=params["current_age"],
        target_age=params["target_age"],
        target_amount=params["target_amount"],
        annual_return=params["annual_return"],
        annual_fee=params["annual_fee"],
        capital_initial=params["capital_initial"],
    )

    years = params["target_age"] - params["current_age"]
    months = years * 12

    st.subheader("📌 Résultat")

    col1, col2, col3 = st.columns(3)
    col1.metric("Durée", f"{years} ans")
    col2.metric("Objectif", f"{params['target_amount']:,.0f} $")
    col3.metric("Investissement mensuel requis", f"{monthly_needed:,.2f} $")

    st.info(
    f"""
### 🎯 Résumé de votre objectif

Pour atteindre **{params['target_amount']:,.0f} $** en **{years} ans**  
avec un rendement de **{params['annual_return']} %** et un frais annuel de **{params['annual_fee']} %**,  

👉 vous devez investir environ :

## 💰 **{monthly_needed:,.2f} $ par mois**
"""
)



except ValueError as e:
    st.error(str(e))
