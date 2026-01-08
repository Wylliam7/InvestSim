import streamlit as st

st.set_page_config(
    page_title="InvestSim",
    layout="wide"
)

st.title("📊 InvestSim")
st.write("Simulateur de croissance d'un capital")

st.subheader("Simulateur de croissance de capital et de planification financière")

st.markdown("""
**InvestSim** est une application interactive qui vous permet de comprendre comment un capital évolue dans le temps,
l’impact des intérêts composés et l’effet des frais de gestion sur le long terme.

Que vous souhaitiez simuler un investissement, analyser des paliers de croissance ou planifier un objectif financier,
InvestSim vous fournit des outils simples, visuels et pédagogiques.
""")

st.info("👉 Utilisez le menu de gauche pour naviguer entre les pages.")

st.markdown("---")
st.markdown("## 🚀 Fonctionnalités disponibles")


st.markdown("""
### 1️⃣ Simulation de capital avec frais de gestion 

Cette page vous permet de visualiser l’évolution de votre patrimoine au fil du temps et d'y ajouter l'effet d'un frais de gestion si nécéssaire.

Vous devez entrer les informations suivantes :
- Un capital initial
- Un montant investi chaque mois
- Un taux de rendement annuel (on considère que celui-ci est constant pour la simulation)
- Des frais de gestion annuels en pourcentage
- Une durée d’investissement en année

L’application vous affiche:
- La croissance de votre capital avec et sans frais au fil du temps à l'aide dun graphique
- Le montant total investi
- La valeur du capital avec et sans frais ainsi que la différence entre les deux
- Les frais totals cumulés ainsi que les frais annuels moyens
- L'impact réel des frais sur le long terme à l’aide d’un graphique interactif
""")


st.markdown("""
### 2️⃣ Simulation des paliers de capital

Cette fonctionnalité a pour but de montrer directement l'impact des intérêts composés et de la puissance de ceux-ci.

Vous devez entrer les informations suivantes :
- Les mêmes paramètres qu'à la première fonctionnalité ainsi que les suivants
- Un montant de palier (ex : 100 000 $)
- Un nombre maximal de paliers à analyser

L’application vous affiche :
- Le temps nécessaire pour atteindre chaque palier
- Le temps entre chaque palier
- Cet outil met en évidence l’accélération de la croissance grâce aux intérêts composés afin d'illustrer le dicton suivant : 
« Les premiers 100 000 sont les plus dures »



""")



st.markdown("""
### 3️⃣ Objectif financier

Cette page vous aide à planifier un objectif précis (retraite, projet, indépendance financière, etc.).

Vous devez entrer les informations suivantes :
- Votre âge actuel
- L’âge auquel vous souhaitez atteindre votre objectif
- Le montant cible
- Un taux de rendement annuel
- Des frais de gestion
- Et éventuellement un capital initial

L’application vous affiche :
👉 le montant à investir chaque mois pour atteindre votre objectif à l’âge souhaité.
""")

st.markdown("---")

st.markdown("""
## 🎯 Objectif d’InvestSim

InvestSim a été conçu pour :
- Rendre la finance personnelle plus accessible
- Visualiser concrètement l’effet du temps et des intérêts composés
- Montrer l’impact souvent sous-estimé des frais de gestion
- Et fournir des outils simples pour mieux planifier son avenir financier

---

⚠️ **Avertissement :**  
Cette application est un outil éducatif. Les résultats sont basés sur des hypothèses simplifiées
(rendement constant, frais moyens, etc.) et ne constituent pas un conseil financier.
""")