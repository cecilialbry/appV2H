
import streamlit as st
from simulateur_streamlit_clean import run_simulation

st.set_page_config(page_title="V2H Simulator", layout="wide")
st.title("Vehicle-to-Home (V2H) Energy Simulation")

st.sidebar.header("Vehicle Parameters")
arrival_hour = st.sidebar.slider("Arrival Hour", 0, 23, 18)
departure_hour = st.sidebar.slider("Departure Hour", 0, 23, 8)

st.sidebar.markdown("---")
if st.sidebar.button("Run Simulation"):
    try:
        run_simulation(arrival_hour, departure_hour)
    except Exception as e:
        st.error(f"An error occurred during the simulation: {e}")

