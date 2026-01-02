import streamlit as st
from core.simulation import simulate_capital
from ui.sidebar import render_sidebar
from ui.charts import plot_capital_interactive

st.set_page_config(page_title="InvestSIM", page_icon="📈", layout="wide")
st.title("📈 Simulation")

# Récupérer les paramètres depuis la sidebar
params = render_sidebar()

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

# Affichage sous le graphique
col1, col2, col3 = st.columns(3)
col1.metric("Capital final sans frais", f"{final_no_fee:,.0f} $")
col2.metric("Capital final avec frais", f"{final_with_fee:,.0f} $")
col3.metric("Frais cumulés", f"{final_fees:,.0f} $")
