import streamlit as st
from simulateur import run_simulation

st.set_page_config(page_title="Simulateur V2H", layout="wide")

st.title("Simulation énergétique V2H")

if st.button("Lancer la simulation"):
    fig, df = run_simulation(
        country="Paris",
        month="January",
        profile_name="Evening Users",
        arrival_hour=17,
        departure_hour=8,
        initial_soc=0.3,
        target_soc=0.6,
        num_vehicles=1,
        mode="V2H",
        vehicle_type="Renault Zoe (40 kWh)",
        peak_power_kwp=6
    )
    st.plotly_chart(fig)
    st.dataframe(df)
