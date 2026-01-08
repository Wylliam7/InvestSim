import streamlit as st

st.set_page_config(page_title="À propos", page_icon="ℹ️", layout="wide")
st.title("ℹ️ À propos d'InvestSIM")

st.markdown("""
## 📈 Qu'est-ce qu'InvestSIM ?

**InvestSIM** est une application à caractère pédagogique de simulation financière qui permet de visualiser l’évolution d’un capital dans le temps en fonction :
- d’un capital initial,
- de versements mensuels,
- d’un taux de rendement annuel,
- et de frais de gestion.

L’objectif est de montrer concrètement l’impact des intérêts composés et des frais sur le long terme.

---

## 🎯 Pourquoi cette application ?

Ce simulateur a été créé pour :
- Mieux comprendre la finance personnelle
- Illustrer l'effet des frais de gestion
- Illustrer l'effet du temps lorsqu'on parle d'investissement
- Aider à la planification d’objectifs financiers (épargne, retraite, projets à long terme)
- Et servir de projet d’apprentissage en programmation

---

## 🧮 Ce que vous pouvez faire

Avec InvestSIM, vous pouvez :
- Simuler la croissance d’un capital avec ou sans frais
- Comparer différents scénarios d’investissement
- Analyser le temps entre chaque palier d'investissement
- Calculer combien investir chaque mois pour atteindre un objectif financier précis

---

## ⚠️ Avertissement

Cette application est un outil éducatif.  
Elle ne constitue pas un conseil financier et ne remplace pas l’avis d’un professionnel.

Les résultats sont basés sur des hypothèses simplifiées (rendement constant, frais moyens, etc.) et peuvent différer de la réalité des marchés.

---

## 👨‍💻 Auteur

Développé par Wylliam Sareault dans le cadre d’un projet personnel autour de la finance et du développement logiciel.
""")
