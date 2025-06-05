import streamlit as st
from simulateur import lancer_simulation


st.set_page_config(page_title="V2H Simulator", layout="wide")
st.title("🔋 V2H Energy Simulator")

st.markdown("Click below to run the simulation:")

if st.button("Run simulation"):
    df, fig = lancer_simulation()
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df)
