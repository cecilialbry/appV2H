import streamlit as st

st.set_page_config(page_title="V2H Simulator", layout="wide")

st.title("🔋 V2H Energy Simulator (Vehicle-to-Home)")

st.markdown("""
Welcome to the V2H energy simulation application.  
This interface allows you to visualize the energy exchanges between:
- an electric vehicle (EV),
- a house (energy demand),
- photovoltaic (solar) production (PV),
- and the power grid.

🚧 This version is under construction. Many features will be added soon.
""")

if st.button("Run simulation"):
    st.success("Simulation started (simulation engine coming soon)")
