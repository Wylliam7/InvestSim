import streamlit as st
from core.simulation import simulate_capital
from core.simulation import capital_steps_table
from ui.sidebar import render_sidebar_simulation_frais
from ui.charts import plot_capital_interactive

st.set_page_config(page_title="InvestSIM", page_icon="📈", layout="wide")
st.title("📈 Simulation")

# Récupérer les paramètres depuis la sidebar
params = render_sidebar_simulation_frais()

# Calculer le capital avec la fonction importée
capital_no_fee, capital_with_fee = simulate_capital(
    params["capital_initial"],
    params["monthly"],
    params["rate"],
    params["fee"],
    params["years"]
)

# Créer le graphique
fig = plot_capital_interactive(
    capital_no_fee,
    capital_with_fee,
    params["years"]
)

# Afficher le graphique
st.plotly_chart(fig, use_container_width=True)



# Valeurs finales
final_no_fee = capital_no_fee[-1]
final_with_fee = capital_with_fee[-1]
final_fees = final_no_fee - final_with_fee

# Montant total investi
total_invested = params["capital_initial"] + params["monthly"] * 12 * params["years"]

# Gains
gain_no_fee = final_no_fee - total_invested
gain_with_fee = final_with_fee - total_invested


# Affichage sous le graphique
col1, col2, col3, col4 = st.columns(4)
col1.metric("Capital final sans frais", f"{final_no_fee:,.0f} $")
col2.metric("Capital final avec frais", f"{final_with_fee:,.0f} $")
col3.metric("Frais cumulés", f"{final_fees:,.0f} $")
col4.metric("Frais annuel moyen", f"{final_fees / params['years']:,.0f} $")


col5, col6, col7, col8 = st.columns(4)
col5.metric("Gain sans frais", f"{gain_no_fee:,.0f} $")
col6.metric("Gain avec frais", f"{gain_with_fee:,.0f} $")
col7.metric("Différence de gain", f"{gain_no_fee - gain_with_fee:,.0f} $")
col8.metric("Montant total investi", f"{total_invested:,.0f} $")
