import streamlit as st
from core.simulation import simulate_capital, capital_steps_table
from ui.sidebar import render_sidebar_paliers
import pandas as pd

st.set_page_config(page_title="InvestSIM - Paliers", page_icon="📊", layout="wide")
st.title("📊 Simulation des paliers (sans frais)")

# Récupérer les mêmes paramètres que la première page
params = render_sidebar_paliers()

# On fait la simulation SANS frais
capital_no_fee, _ = simulate_capital(
    params["capital_initial"],
    params["monthly"],
    params["rate"],
    0, 
    params["years"]
)

# Récupérer le palier choisi et le nombre max à afficher
step = params["palier"]
max_display = params["max_paliers"]

# Calcul des paliers
steps = capital_steps_table(capital_no_fee, step)
steps = steps[:max_display]

years = [y for s, y in steps]
delta_years = [years[0]]  
for i in range(1, len(years)):
    delta_years.append(years[i] - years[i-1])

# Créer DataFrame pour afficher
df = pd.DataFrame({
    "Palier ($)": [s for s, y in steps],
    "Années": [y for s, y in steps],
     "Temps depuis palier précédent (ans)": delta_years
})

st.subheader(f"Temps pour atteindre chaque palier ({step:,.0f} $)")
st.dataframe(df)