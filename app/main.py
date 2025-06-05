import streamlit as st
from simulateur_streamlit_ready import lancer_simulation

st.set_page_config(page_title="Simulateur V2H", layout="wide")

st.title("Simulateur V2H")

if st.button("Lancer la simulation"):
    fig, df = lancer_simulation()
    if fig is not None and df is not None:
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(df)

