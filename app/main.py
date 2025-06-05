
import streamlit as st
from simulateur_streamlit_ready import run_simulation

st.set_page_config(page_title="V2X Simulator", layout="wide")
st.title("Vehicle-to-X (V2X) Energy Simulation")

st.sidebar.header("Simulation Parameters")

profile_name = st.sidebar.selectbox("Select User Profile", ["Standard", "Family", "Worker"])
arrival_hour = st.sidebar.slider("Arrival Hour", 0, 23, 18)
departure_hour = st.sidebar.slider("Departure Hour", 0, 23, 8)
initial_soc = st.sidebar.slider("Initial SoC (%)", 0, 100, 50)
target_soc = st.sidebar.slider("Target SoC (%)", 0, 100, 80)
num_vehicles = st.sidebar.number_input("Number of Vehicles", min_value=1, max_value=100, value=1)
mode = st.sidebar.selectbox("Simulation Mode", ["V2H", "V2B", "V2G"])
vehicle_type = st.sidebar.selectbox("Vehicle Type", ["Car", "Bus", "Truck"])
peak_power_kwp = st.sidebar.slider("PV Peak Power (kWp)", 0.0, 20.0, 5.0, step=0.5)

st.sidebar.markdown("---")
if st.sidebar.button("Run Simulation"):
    try:
        run_simulation(profile_name, arrival_hour, departure_hour,
                       initial_soc, target_soc, num_vehicles,
                       mode, vehicle_type, peak_power_kwp)
    except Exception as e:
        st.error(f"An error occurred during the simulation: {e}")
