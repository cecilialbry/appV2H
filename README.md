# appV2H – Streamlit Application

This repository contains the **Streamlit application** for the V2H (Vehicle-to-Home) energy simulator, developed as part of an internship at the LUCAMI Laboratory – University of Ljubljana.

🔗 **App Links**  
- First version: https://appv2h-juezzmflsjsuvucgecthpd.streamlit.app/  
- Optimized version: https://appv2h.streamlit.app/ 
- Comparison version: https://appv2h-7jqrlvgtjyd6h7wkjzka6x.streamlit.app/
- dropbox paper : https://paper.dropbox.com/doc/Erasmus-Work-plan-for-Cecilia-2025--CoeQu16DDLFZZb8rRVPYdHU1Ag-ne8HBrNTSoXsAu0wKfxL0

## 🎯 Purpose

This application offers a simple and interactive interface to simulate energy exchanges between:
- an electric vehicle (EV),
- a house (hourly consumption),
- solar power production (PV),
- and the electrical grid.

The user can choose:
- their consumption profile,
- the simulation period (month),
- the EV characteristics,
- and view the results through plots and tables.

## 🗂️ Project Structure

appV2H/
├── app/ # Streamlit Python files
├── data/ # Data: user profiles, PV production, tariffs
├── assets/ # Images, logos for the interface
├── .streamlit/ # Streamlit configuration files (layout, theme)
├── requirements.txt # Required Python libraries
├── CHANGELOG.md # App version history
└── README.md

