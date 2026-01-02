import streamlit as st
from core.simulation import simulate_capital
from ui.sidebar import render_sidebar
from ui.charts import plot_capital
from state.session import init_state

st.title("📈 Simulation")

init_state()
params = render_sidebar()

no_fee, with_fee = simulate_capital(
    params["capital_initial"],
    params["monthly"],
    params["rate"],
    params["fee"],
    params["years"]
)

st.pyplot(plot_capital(no_fee, with_fee))

st.metric("Capital final sans frais", f"{no_fee[-1]:,.0f} €")
st.metric("Capital final avec frais", f"{with_fee[-1]:,.0f} €")
