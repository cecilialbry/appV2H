
import streamlit as st
from simulateur_streamlit_ready import run_simulation

st.title("V2X Energy Simulator")

# User inputs
st.sidebar.header("Simulation Parameters")

profile_name = st.sidebar.selectbox("Select user profile:", [
    "Evening Users",
    "Late Afternoon Peakers",
    "Coffee Makers",
    "Night Owls",
    "Morning Glory"
])

arrival_hour = st.sidebar.slider("Vehicle arrival hour (0–23):", 0, 23, 18)
departure_hour = st.sidebar.slider("Vehicle departure hour (1–24):", 1, 24, 8)
initial_soc = st.sidebar.slider("Initial SoC (%)", 0, 100, 50)
target_soc = st.sidebar.slider("Target SoC (%)", 0, 100, 80)
num_vehicles = st.sidebar.slider("Number of vehicles:", 1, 20, 1)

vehicle_type = st.sidebar.selectbox("Vehicle type:", [
    "Renault Zoe (40 kWh)",
    "Peugeot e-208 (50 kWh)",
    "Hyundai Kona (64 kWh)",
    "Tesla Model 3 (75 kWh)",
    "BMW iX3 (80 kWh)"
])

mode = st.sidebar.selectbox("Simulation mode:", ["V2H", "V2B", "V2G"])

peak_power_kwp = st.sidebar.slider("PV peak power (kWp):", 1, 20, 5)

city = st.sidebar.selectbox("Select location:", ["Paris", "Ljubljana", "Copenhagen", "Athens", "Lisbon"])
month = st.sidebar.selectbox("Select month:", list(range(1, 13)))

# Launch simulation
if st.button("Run Simulation"):
    try:
        run_simulation(
            profile_name=profile_name,
            arrival_hour=arrival_hour,
            departure_hour=departure_hour,
            initial_soc=initial_soc,
            target_soc=target_soc,
            num_vehicles=num_vehicles,
            mode=mode,
            vehicle_type=vehicle_type,
            peak_power_kwp=peak_power_kwp,
            country=country,
            month=month
        )
    except Exception as e:
        st.error(f"An error occurred during the simulation: {e}")

