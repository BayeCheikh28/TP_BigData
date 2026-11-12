import streamlit as st
import plotly.express as px
import processing

st.set_page_config(page_title="NBA Big Data Dashboard", layout="wide")

st.title("Dashboard NBA - Analyse Big Data")
st.write("Analyse de l'historique des matchs NBA depuis 1946 (source : FiveThirtyEight nba-elo).")

victoires = processing.victoires_par_equipe()
scores = processing.score_moyen_par_saison()
matchs = processing.matchs_par_saison()
domicile = processing.taux_victoire_domicile_exterieur()
elo = processing.elo_moyen_par_equipe()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 15 franchises par nombre de victoires")
    fig1 = px.bar(victoires, x="equipe", y="victoires", color="victoires")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Top 15 franchises par score Elo moyen")
    fig2 = px.bar(elo, x="equipe", y="elo_moyen", color="elo_moyen")
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Evolution du score moyen par saison")
fig3 = px.line(scores, x="saison", y="score_moyen")
st.plotly_chart(fig3, use_container_width=True)

st.subheader("Nombre de matchs par saison")
fig4 = px.bar(matchs, x="saison", y="nb_matchs")
st.plotly_chart(fig4, use_container_width=True)

st.subheader("Repartition des victoires/defaites : domicile vs exterieur")
fig5 = px.bar(domicile, x="lieu", y="nb", color="resultat", barmode="group")
st.plotly_chart(fig5, use_container_width=True)

st.caption("Projet Big Data - Ingestion, Persistance, Traitement et Insights")
