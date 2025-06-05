import streamlit as st
from app.simulateur import lancer_simulation

st.set_page_config(page_title="Simulateur V2H", layout="wide")

st.title("🔋 Simulateur énergétique V2H (Vehicle-to-Home)")
st.markdown("""
Bienvenue dans l'application de simulation énergétique V2H.  
Cette interface vous permet de visualiser les échanges d’énergie entre :
- un véhicule électrique (VE),
- une maison (demande énergétique),
- une production photovoltaïque (PV),
- et le réseau.
""")

if st.button("Lancer la simulation"):
    fig, df = lancer_simulation()
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df)
