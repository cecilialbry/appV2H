import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Simulateur énergétique V2H", layout="wide")

st.markdown("""
<style>
/* Supprime le header Streamlit par défaut */
header[data-testid="stHeader"] {
    height: 0rem;
    padding: 0rem;
    margin: 0rem;
}

/* Réduit le padding autour du contenu principal */
.block-container {
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
}

/* Réduit marges haut/bas des sections principales */
section.main > div:first-child {
    padding-top: 0rem;
}
section.main > div:last-child {
    padding-bottom: 0rem;
}

/* Réduit espace entre widgets */
section.main > div {
    gap: 0.3rem;
}

/* Sliders plus compacts */
.stSlider > div {
    padding-top: 0.1rem;
    padding-bottom: 0.1rem;
}
.stSlider .rc-slider {
    height: 8px;
}
.stSlider .rc-slider-handle {
    height: 14px;
    width: 14px;
    margin-top: -3px;
}

/* Réduit marges autour des titres */
h1, h2, h3 {
    margin-top: 0.2rem !important;
    margin-bottom: 0.2rem !important;
}

/* Texte général plus petit */
html, body, [class*="css"] {
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)
st.markdown("### 🔌 Simulateur énergétique V2H")



pv_data_by_country = {
    "Paris": {
        "January":  [0,0,0,0,0,0,0,0.057,0.135,0.174,0.195,0.196,0.188,0.149,0.079,0.022,0,0,0,0,0,0,0,0],
        "February": [0,0,0,0,0,0,0.045,0.163,0.252,0.281,0.311,0.310,0.276,0.259,0.188,0.092,0,0,0,0,0,0,0,0],
        "March":    [0,0,0,0,0,0,0.051,0.178,0.302,0.410,0.473,0.503,0.464,0.426,0.344,0.225,0.097,0.003,0,0,0,0,0,0],
        "April":    [0,0,0,0,0,0.045,0.174,0.334,0.487,0.599,0.664,0.696,0.660,0.582,0.459,0.335,0.183,0.049,0,0,0,0,0,0],
        "May":      [0,0,0,0,0,0.096,0.230,0.377,0.524,0.642,0.686,0.701,0.695,0.608,0.502,0.379,0.229,0.094,0,0,0,0,0,0],
        "June":     [0,0,0,0,0,0.111,0.245,0.397,0.533,0.636,0.692,0.702,0.669,0.609,0.519,0.401,0.260,0.127,0,0,0,0,0,0],
        "July":     [0,0,0,0,0,0.092,0.219,0.356,0.506,0.606,0.634,0.674,0.655,0.597,0.497,0.392,0.258,0.125,0,0,0,0,0,0],
        "August":   [0,0,0,0,0,0.083,0.179,0.321,0.460,0.558,0.625,0.634,0.598,0.538,0.435,0.331,0.206,0.078,0,0,0,0,0,0],
        "September":[0,0,0,0,0,0.015,0.124,0.271,0.408,0.492,0.536,0.562,0.518,0.440,0.337,0.236,0.106,0.011,0,0,0,0,0,0],
        "October":  [0,0,0,0,0,0,0.033,0.149,0.261,0.329,0.381,0.371,0.341,0.288,0.194,0.096,0.004,0,0,0,0,0,0,0],
        "November": [0,0,0,0,0,0,0,0.024,0.123,0.179,0.209,0.216,0.196,0.141,0.073,0.000,0,0,0,0,0,0,0,0],
        "December": [0,0,0,0,0,0,0,0,0.038,0.114,0.148,0.157,0.140,0.106,0.010,0,0,0,0,0,0,0,0,0]
    },
    "Ljubljana": {
        "January":  [0,0,0,0,0,0,0.156,0.290,0.336,0.368,0.400,0.421,0.380,0.347,0.144,0,0,0,0,0,0,0,0,0],
        "February": [0,0,0,0,0,0.001,0.260,0.349,0.432,0.451,0.490,0.486,0.483,0.424,0.317,0.060,0,0,0,0,0,0,0,0],
        "March":    [0,0,0,0,0.003,0.223,0.389,0.497,0.572,0.604,0.627,0.599,0.565,0.523,0.439,0.309,0.001,0,0,0,0,0,0,0],
        "April":    [0,0,0,0.0002,0.171,0.361,0.516,0.617,0.664,0.678,0.684,0.648,0.617,0.538,0.495,0.383,0.164,0,0,0,0,0,0,0],
        "May":      [0,0,0,0.068,0.248,0.402,0.542,0.639,0.691,0.692,0.682,0.646,0.604,0.540,0.508,0.419,0.266,0.003,0,0,0,0,0,0],
        "June":     [0,0,0,0.118,0.321,0.498,0.632,0.737,0.773,0.765,0.752,0.733,0.676,0.609,0.572,0.493,0.351,0.095,0,0,0,0,0,0],
        "July":     [0,0,0,0.085,0.311,0.506,0.646,0.747,0.804,0.808,0.797,0.778,0.722,0.674,0.621,0.532,0.375,0.079,0,0,0,0,0,0],
        "August":   [0,0,0,0.003,0.203,0.399,0.556,0.664,0.744,0.769,0.756,0.737,0.723,0.647,0.579,0.478,0.280,0.008,0,0,0,0,0,0],
        "September":[0,0,0,0.076,0.263,0.400,0.546,0.640,0.678,0.678,0.645,0.606,0.550,0.477,0.325,0.019,0,0,0,0,0,0,0,0],
        "October":  [0,0,0,0,0,0.147,0.237,0.332,0.414,0.517,0.551,0.524,0.499,0.429,0.305,0.021,0,0,0,0,0,0,0,0],
        "November": [0,0,0,0,0,0.010,0.163,0.227,0.254,0.307,0.327,0.342,0.329,0.258,0.071,0,0,0,0,0,0,0,0,0],
        "December": [0,0,0,0,0,0,0.123,0.235,0.258,0.275,0.301,0.302,0.300,0.245,0.0003,0,0,0,0,0,0,0,0,0]
    },
        

    "Copenhagen": {
        "January":  [0,0,0,0,0,0,0,0,0.056,0.135,0.174,0.195,0.188,0.150,0.079,0.001,0,0,0,0,0,0,0,0],
        "February": [0,0,0,0,0,0,0,0.045,0.163,0.252,0.281,0.311,0.277,0.259,0.188,0.092,0,0,0,0,0,0,0,0],
        "March":    [0,0,0,0,0,0,0.051,0.178,0.302,0.410,0.473,0.503,0.464,0.426,0.344,0.225,0.097,0,0,0,0,0,0,0],
        "April":    [0,0,0,0,0,0,0.001,0.173,0.334,0.488,0.599,0.696,0.660,0.582,0.459,0.335,0.183,0.049,0,0,0,0,0,0],
        "May":      [0,0,0,0,0,0,0.027,0.377,0.523,0.641,0.686,0.701,0.695,0.608,0.502,0.379,0.229,0.094,0,0,0,0,0,0],
        "June":     [0,0,0,0,0,0,0.039,0.397,0.533,0.636,0.692,0.702,0.669,0.609,0.519,0.401,0.260,0.127,0,0,0,0,0,0],
        "July":     [0,0,0,0,0,0,0.092,0.356,0.506,0.606,0.634,0.674,0.655,0.597,0.497,0.392,0.258,0.125,0,0,0,0,0,0],
        "August":   [0,0,0,0,0,0,0.083,0.321,0.460,0.558,0.625,0.634,0.598,0.538,0.435,0.331,0.206,0.078,0,0,0,0,0,0],
        "September":[0,0,0,0,0,0,0.015,0.124,0.271,0.408,0.492,0.562,0.518,0.440,0.337,0.236,0.106,0.011,0,0,0,0,0,0],
        "October":  [0,0,0,0,0,0,0,0.033,0.149,0.261,0.329,0.371,0.341,0.288,0.194,0.096,0.004,0,0,0,0,0,0,0],
        "November": [0,0,0,0,0,0,0,0,0.024,0.179,0.209,0.216,0.196,0.141,0.073,0,0,0,0,0,0,0,0,0],
        "December": [0,0,0,0,0,0,0,0,0.037,0.114,0.148,0.157,0.140,0.106,0.010,0,0,0,0,0,0,0,0,0]
        
    },
    "Lisbon": {
        "January":  [0,0,0,0,0,0,0.098,0.303,0.514,0.690,0.819,0.889,0.902,0.814,0.678,0.478,0.260,0.054,0,0,0,0,0,0],
        "February": [0,0,0,0,0,0,0.038,0.235,0.419,0.566,0.674,0.704,0.715,0.623,0.508,0.330,0.128,0.001,0,0,0,0,0,0],
        "March":    [0,0,0,0,0,0,0.051,0.302,0.410,0.473,0.503,0.464,0.426,0.344,0.225,0.097,0.003,0,0,0,0,0,0,0],
        "April":    [0,0,0,0,0,0,0.045,0.333,0.487,0.599,0.664,0.696,0.660,0.582,0.459,0.335,0.183,0.002,0,0,0,0,0,0],
        "May":      [0,0,0,0,0,0,0.096,0.377,0.524,0.642,0.686,0.701,0.695,0.608,0.502,0.379,0.229,0.003,0,0,0,0,0,0],
        "June":     [0,0,0,0,0,0,0.111,0.397,0.533,0.636,0.692,0.702,0.669,0.609,0.519,0.401,0.260,0.013,0,0,0,0,0,0],
        "July":     [0,0,0,0,0,0,0.093,0.356,0.506,0.606,0.634,0.674,0.655,0.597,0.497,0.392,0.258,0.008,0,0,0,0,0,0],
        "August":   [0,0,0,0,0,0,0.071,0.321,0.461,0.558,0.625,0.634,0.598,0.538,0.435,0.331,0.206,0.015,0,0,0,0,0,0],
        "September":[0,0,0,0,0,0,0.076,0.263,0.400,0.547,0.679,0.645,0.606,0.550,0.477,0.325,0.019,0,0,0,0,0,0,0],
        "October":  [0,0,0,0,0,0,0,0.147,0.237,0.332,0.414,0.551,0.499,0.429,0.305,0.021,0,0,0,0,0,0,0,0],
        "November": [0,0,0,0,0,0,0.010,0.163,0.227,0.254,0.307,0.342,0.329,0.258,0.071,0,0,0,0,0,0,0,0,0],
        "December": [0,0,0,0,0,0,0,0.123,0.235,0.258,0.275,0.301,0.300,0.245,0,0,0,0,0,0,0,0,0,0]
        
    },
    "Athens": {
        "January":  [0,0,0,0,0,0,0.056,0.135,0.174,0.195,0.187,0.150,0.079,0.049,0.028,0,0,0,0,0,0,0,0,0],
        "February": [0,0,0,0,0,0,0.045,0.163,0.252,0.281,0.277,0.259,0.188,0.092,0,0,0,0,0,0,0,0,0,0],
        "March":    [0,0,0,0,0,0,0.051,0.178,0.302,0.410,0.473,0.503,0.464,0.426,0.344,0.225,0.097,0,0,0,0,0,0,0],
        "April":    [0,0,0,0,0,0,0.045,0.333,0.487,0.599,0.664,0.696,0.660,0.582,0.459,0.335,0.183,0.049,0,0,0,0,0,0],
        "May":      [0,0,0,0,0,0,0.096,0.377,0.524,0.642,0.686,0.701,0.695,0.608,0.502,0.379,0.229,0.094,0,0,0,0,0,0],
        "June":     [0,0,0,0,0,0,0.111,0.397,0.533,0.636,0.692,0.702,0.669,0.609,0.519,0.401,0.260,0.127,0,0,0,0,0,0],
        "July":     [0,0,0,0,0,0,0.092,0.356,0.506,0.606,0.634,0.674,0.655,0.597,0.497,0.392,0.258,0.125,0,0,0,0,0,0],
        "August":   [0,0,0,0,0,0,0.083,0.321,0.460,0.558,0.625,0.634,0.598,0.538,0.435,0.331,0.206,0.078,0,0,0,0,0,0],
        "September":[0,0,0,0,0,0,0.015,0.124,0.271,0.408,0.492,0.562,0.518,0.440,0.337,0.236,0.106,0.011,0,0,0,0,0,0],
        "October":  [0,0,0,0,0,0,0,0.033,0.149,0.261,0.329,0.371,0.341,0.288,0.194,0.096,0.004,0,0,0,0,0,0,0],
        "November": [0,0,0,0,0,0,0,0,0.024,0.179,0.209,0.216,0.196,0.141,0.073,0,0,0,0,0,0,0,0,0],
        "December": [0,0,0,0,0,0,0,0,0.037,0.114,0.148,0.157,0.140,0.106,0.010,0,0,0,0,0,0,0,0,0]
        
    }
}


# === Profils utilisateurs ===
user_profiles = {
    "Evening Users": [0.3,0.2,0.2,0.2,0.1,0.2,0.3,0.5,0.6,0.7,0.8,0.9,1.2,1.5,1.8,2.0,2.1,2.2,2.5,2.0,1.2,0.8,0.5,0.4],
    "Late Afternoon Peakers": [0.2]*8 + [0.5,0.8,1.5,2.0,2.2,2.0,1.8,1.5,1.0,0.6,0.4,0.2,0.2,0.2,0.2,0.2],
    "Coffee Makers": [0.1,0.1,0.3,1.0,1.5,1.2,1.0,0.8,0.6,0.5,0.4,0.3,0.4,0.6,0.8,1.0,1.1,1.2,1.1,0.8,0.6,0.4,0.3,0.2],
    "Night Owls": [0.2]*18 + [0.8,1.2,1.5,1.6,1.3,1.0],
    "Morning Glory": [1.2,1.5,1.6,1.4,1.2,1.0,0.8,0.5,0.3,0.2,0.2,0.2,0.3,0.4,0.6,0.7,0.6,0.5,0.4,0.4,0.3,0.3,0.3,0.3]
}
tariff_blocks_by_city = {
    "Paris": {
        "off_peak": list(range(0, 7)) + list(range(22, 24)),
        "mid_peak": list(range(7, 15)),
        "peak": list(range(15, 22))
    },
    "Ljubljana": {
        "off_peak": list(range(0, 6)) + list(range(21, 24)),
        "mid_peak": list(range(6, 14)),
        "peak": list(range(14, 21))
    },
    "Copenhagen": {
        "off_peak": list(range(0, 8)) + list(range(21, 24)),
        "mid_peak": list(range(8, 16)),
        "peak": list(range(16, 21))
    },
    "Lisbon": {
        "off_peak": list(range(0, 6)) + list(range(23, 24)),
        "mid_peak": list(range(6, 14)),
        "peak": list(range(14, 23))
    },
    "Athens": {
        "off_peak": list(range(0, 5)) + list(range(22, 24)),
        "mid_peak": list(range(5, 13)),
        "peak": list(range(13, 22))
    }
}
tariff_rates_by_city = {
    "Paris": {
        "off_peak": 0.16,
        "mid_peak": 0.22,
        "peak": 0.28
    },
    "Ljubljana": {
        "off_peak": 0.14,
        "mid_peak": 0.20,
        "peak": 0.30
    },
    "Copenhagen": {
        "off_peak": 0.18,
        "mid_peak": 0.24,
        "peak": 0.32
    },
    "Lisbon": {
        "off_peak": 0.15,
        "mid_peak": 0.21,
        "peak": 0.27
    },
    "Athens": {
        "off_peak": 0.13,
        "mid_peak": 0.19,
        "peak": 0.25
 
    }
}
vehicle_options = {
    "Renault Zoe (40 kWh)": {"capacity_kWh": 40, "max_power_kW": 11},
    "Peugeot e-208 (50 kWh)": {"capacity_kWh": 50, "max_power_kW": 11},
    "Hyundai Kona (64 kWh)": {"capacity_kWh": 64, "max_power_kW": 11},
    "Tesla Model 3 (75 kWh)": {"capacity_kWh": 75, "max_power_kW": 11},
    "BMW iX3 (80 kWh)": {"capacity_kWh": 80, "max_power_kW": 11}
}

# === Fonction run_simulation corrigée ===
def run_simulation(country, month, profile_name, arrival_hour, departure_hour,
                   initial_soc, target_soc, num_vehicles, mode, vehicle_type, peak_power_kwp):
    battery_capacity_kWh = 70
    max_kWh_per_hour = 11
    min_soc_ratio = 0.20

    house_demand_profile = user_profiles[profile_name]
    pv_raw = pv_data_by_country[country][month]
    rendement = 0.205
    surface_par_kwp = 4.875
    surface_totale = surface_par_kwp * peak_power_kwp
    pv_profile = [irr * surface_totale * rendement for irr in pv_raw]

    tariff_blocks = tariff_blocks_by_city[country]
    tariff_rates = tariff_rates_by_city[country]
    vehicle = vehicle_options[vehicle_type]
    battery_capacity_kWh = vehicle["capacity_kWh"]
    max_kWh_per_hour = vehicle["max_power_kW"]

    initial_soc_kWh = initial_soc * battery_capacity_kWh
    target_soc_kWh = target_soc * battery_capacity_kWh
    current_soc = initial_soc_kWh

    soc_kWh = [None] * 24
    battery_flow = [0] * 24
    net_load = [0] * 24

    if arrival_hour <= departure_hour:
        connected_hours = list(range(arrival_hour, departure_hour))
    else:
        connected_hours = list(range(arrival_hour, 24)) + list(range(0, departure_hour))
    total_pv_connected = sum(pv_profile[h] for h in connected_hours)

    def decide_recharge(h, current_soc, house_demand, pv, mode, tariff_blocks, tariff_rates):
        energy_needed = target_soc_kWh - current_soc
        if energy_needed <= 0:
            return 0
        hours_left = (departure_hour - h) % 24 or 24
        max_possible_energy = hours_left * max_kWh_per_hour
        if energy_needed > max_possible_energy - 1e-3:
            return min(energy_needed, max_kWh_per_hour, battery_capacity_kWh - current_soc)
        future_surplus = sum(max(pv_profile[hh] - house_demand_profile[hh], 0)
                             for hh in range(h+1, departure_hour))
        if energy_needed > future_surplus:
            return min(energy_needed, max_kWh_per_hour, battery_capacity_kWh - current_soc)
        if h in tariff_blocks["off_peak"]:
            return min(energy_needed, max_kWh_per_hour, battery_capacity_kWh - current_soc)
        if h in tariff_blocks["mid_peak"]:
            return min(energy_needed, max_kWh_per_hour, battery_capacity_kWh - current_soc)
        if h in tariff_blocks["peak"] and energy_needed > (hours_left - 1) * max_kWh_per_hour:
            return min(energy_needed, max_kWh_per_hour, battery_capacity_kWh - current_soc)
        if hours_left <= 1 or energy_needed > (hours_left - 1) * max_kWh_per_hour:
            return min(energy_needed, max_kWh_per_hour, battery_capacity_kWh - current_soc)
        remaining_hours = (departure_hour - h) % 24
        remaining_possible_energy = remaining_hours * max_kWh_per_hour
        if energy_needed > remaining_possible_energy:
            return min(energy_needed, max_kWh_per_hour, battery_capacity_kWh - current_soc)
        return 0

    def decide_discharge(h, mode, current_soc, house_demand, hours_left):
        max_possible_recharge = (hours_left - 1) * max_kWh_per_hour
        soc_floor = max(target_soc_kWh - max_possible_recharge, min_soc_ratio * battery_capacity_kWh)
        discharge_margin = current_soc - soc_floor

        if discharge_margin <= 0.01:
            return 0

        if mode == "V2H":
            if house_demand <= 1:
                return 0
            return -min(house_demand, discharge_margin, max_kWh_per_hour)

        elif mode == "V2G":
            return -min(discharge_margin, max_kWh_per_hour)

        elif mode == "V2B":
            if house_demand <= 1:
                return 0
            building_demand = house_demand * 3
            return -min(building_demand, discharge_margin, max_kWh_per_hour)

        return 0

    soc_kWh[arrival_hour] = current_soc

    for h in connected_hours:
        if h == arrival_hour:
            continue

        demand = house_demand_profile[h]
        pv = pv_profile[h]
        remaining_hours = connected_hours[connected_hours.index(h)+1:]
        hours_left = len(remaining_hours)
        if pv >= demand:
            discharge_kWh = 0
        else:
            discharge_kWh = decide_discharge(h, mode, current_soc, demand, hours_left)

        if discharge_kWh < 0:
            battery_effect = discharge_kWh
        else:
            recharge_kWh = decide_recharge(h, current_soc, demand, pv, mode, tariff_blocks, tariff_rates)
            battery_effect = recharge_kWh

        battery_effect_total = battery_effect * num_vehicles
        current_soc += battery_effect
        current_soc = max(min(current_soc, battery_capacity_kWh), min_soc_ratio * battery_capacity_kWh)
        soc_kWh[h] = current_soc
        battery_flow[h] = round(battery_effect_total, 2)
        net_load[h] = round(max(demand - pv + battery_effect_total, 0), 2)

    if soc_kWh[departure_hour] is None:
        soc_kWh[departure_hour] = current_soc
    soc_kWh[h] = current_soc
    soc_percent = [round(100 * s / battery_capacity_kWh, 2) if s is not None else None for s in soc_kWh]
    hours_str = [f"{h:02d}:00" for h in range(24)]

    summary_df = pd.DataFrame({
        "hour": list(range(24)),
    
        "house_demand": house_demand_profile,
        "pv_generation": pv_profile,
        "battery_flow": battery_flow
    })

    ev_support = summary_df.apply(
        lambda row: min(max(row["house_demand"] - row["pv_generation"], 0), -row["battery_flow"]) if row["battery_flow"] < 0 else 0,
        axis=1
    )
    total_ev = ev_support.sum()
    ev_pct = round(100 * total_ev / summary_df["house_demand"].sum(), 2)

    pv_support = summary_df.apply(
        lambda row: min(row["house_demand"], row["pv_generation"]) if row["hour"] in connected_hours else 0,
        axis=1
    )
    total_pv = pv_support.sum()
    pv_pct = round(100 * total_pv / summary_df["house_demand"].sum(), 2)

    covered_total = summary_df.apply(
        lambda row: min(row["house_demand"], row["pv_generation"] + max(-row["battery_flow"], 0)),
        axis=1
    )
    self_suff_pct = round(100 * covered_total.sum() / summary_df["house_demand"].sum(), 2)

    energy_charged_kWh = summary_df[summary_df["battery_flow"] > 0]["battery_flow"].sum()
    ev_charge_pv = summary_df.apply(
        lambda row: min(row["pv_generation"], row["battery_flow"]) if row["battery_flow"] > 0 else 0,
        axis=1
    ).sum()
    ev_charge_grid = energy_charged_kWh - ev_charge_pv
    ev_charge_pv = round(ev_charge_pv, 2)
    ev_charge_grid = round(ev_charge_grid, 2)

    energy_discharged_kWh = summary_df[summary_df["battery_flow"] < 0]["battery_flow"].abs().sum()

    baseline_kWh_from_grid = [max(house_demand_profile[h] - pv_profile[h], 0) for h in connected_hours]
    actual_kWh_from_grid = [max(house_demand_profile[h] - pv_profile[h] - battery_flow[h], 0) for h in connected_hours]

    tariff_per_hour = []
    for h in connected_hours:
        if h in tariff_blocks["peak"]:
            tariff_per_hour.append(tariff_rates["peak"])
        elif h in tariff_blocks["mid_peak"]:
            tariff_per_hour.append(tariff_rates["mid_peak"])
        else:
            tariff_per_hour.append(tariff_rates["off_peak"])

    baseline_cost = sum([kwh * price for kwh, price in zip(baseline_kWh_from_grid, tariff_per_hour)])
    actual_cost = sum([kwh * price for kwh, price in zip(actual_kWh_from_grid, tariff_per_hour)])
    savings = round(baseline_cost - actual_cost, 2)

    fig = go.Figure()
    for hour in tariff_blocks["off_peak"]:
        fig.add_vrect(x0=hour, x1=hour + 1, fillcolor="lightgreen", opacity=0.2, layer="below", line_width=0)
    for hour in tariff_blocks["mid_peak"]:
        fig.add_vrect(x0=hour, x1=hour + 1, fillcolor="lightgray", opacity=0.2, layer="below", line_width=0)
    for hour in tariff_blocks["peak"]:
        fig.add_vrect(x0=hour, x1=hour + 1, fillcolor="lightcoral", opacity=0.2, layer="below", line_width=0)

    fig.add_trace(go.Scatter(x=hours_str, y=house_demand_profile, mode='lines+markers', name='House Demand (kW)', line=dict(color='gray')))
    fig.add_trace(go.Scatter(x=hours_str, y=pv_profile, mode='lines+markers', name='PV (kW)', line=dict(color='orange')))
    fig.add_trace(go.Scatter(x=hours_str, y=battery_flow, mode='lines+markers', name='Battery Flow (kWh)', line=dict(color='green', dash='dot')))
    fig.add_trace(go.Scatter(x=hours_str, y=soc_percent, mode='lines+markers', name='SoC (%)', line=dict(color='blue', dash='dash'), yaxis='y2'))
    fig.add_trace(go.Scatter(x=hours_str, y=net_load, mode='lines+markers', name='Net Load (kW)', line=dict(color='black')))
    fig.add_trace(go.Scatter(x=[hours_str[arrival_hour]], y=[soc_percent[arrival_hour]], mode='markers', name='Arrival', marker=dict(color='green', size=12), yaxis='y2'))
    if soc_percent[departure_hour] is not None:
        fig.add_trace(go.Scatter(x=[hours_str[departure_hour]], y=[soc_percent[departure_hour]], mode='markers', name='Departure', marker=dict(color='red', size=12), yaxis='y2'))

    max_y = max(max(pv_profile), max(house_demand_profile), max(net_load), max(abs(x) for x in battery_flow)) * 1.2
    max_y = min(max_y, 60)
    fig.update_layout(
   
    
    xaxis=dict(title='Heure'),
    yaxis=dict(title='kWh', range=[0, max_y]),
    yaxis2=dict(title='SoC (%)', overlaying='y', side='right', range=[0, 100]),
    width=900,
    height=500,
    margin=dict(t=40, b=40, l=40, r=40),
    legend=dict(orientation="h", yanchor="top", y=1.10, xanchor="center", x=0.5),
    template="plotly_white"
)



        
    
    
    summary = f"""
<span style='font-size:13px; line-height:1.4'>
<b>PV :</b> {round(total_pv_connected, 1)} kWh<br>
<b>VE :</b> {round(total_ev, 1)} kWh<br>
<b>Autonomie :</b> {self_suff_pct:.0f}%<br>
<b>Économies :</b> {abs(round(savings, 2))} €
</span>
"""


    return fig, total_pv_connected, total_ev, ev_pct, total_pv, pv_pct, self_suff_pct, ev_charge_pv, ev_charge_grid, energy_discharged_kWh, savings






# === Interface Streamlit ===



# LIGNE 1
# LIGNE 1 : sélection de contexte
row1 = st.columns(6)
with row1[0]:
    country = st.selectbox("Ville", list(pv_data_by_country.keys()))
with row1[1]:
    month = st.selectbox("Mois", list(pv_data_by_country[country].keys()))
with row1[2]:
    profile_name = st.selectbox("Profil", list(user_profiles.keys()))
with row1[3]:
    mode = st.selectbox("Mode", ["V2H", "V2G", "V2B"])
with row1[4]:
    vehicle_type = st.selectbox("Véhicule", list(vehicle_options.keys()))
with row1[5]:
    num_vehicles = st.slider("Nb véhicules", 1, 10, 1)

# LIGNE 2 : sliders techniques
row2 = st.columns(5)
with row2[0]:
    arrival_hour = st.slider("Arrivée", 0, 23, 8)
with row2[1]:
    departure_hour = st.slider("Départ", 0, 23, 19)
with row2[2]:
    initial_soc = st.slider("SoC init.", 0.2, 0.8, 0.4, 0.05)
with row2[3]:
    target_soc = st.slider("SoC cible", 0.3, 1.0, 0.8, 0.05)
with row2[4]:
    peak_power_kwp = st.slider("PV (kWp)", 0.5, 20.0, 1.0, 0.5)


# === Simulation + afficha
try:
    results = run_simulation(
        country=country,
        month=month,
        profile_name=profile_name,
        arrival_hour=arrival_hour,
        departure_hour=departure_hour,
        initial_soc=initial_soc,
        target_soc=target_soc,
        num_vehicles=num_vehicles,
        mode=mode,
        vehicle_type=vehicle_type,
        peak_power_kwp=peak_power_kwp
    )

    fig = results[0]
    (total_pv_connected, total_ev, ev_pct, total_pv, pv_pct,
     self_suff_pct, ev_charge_pv, ev_charge_grid,
     energy_discharged_kWh, savings) = results[1:]
col_left, col_right = st.columns([3, 1.2])

    with col_left:
      st.plotly_chart(fig, use_container_width=True)
  # graphique plus court

    
    with col_right:
        st.markdown(
            f"""
            <div style='text-align: right; font-size: 0.9em; line-height: 1.6;'>
            <h5>🔎 Résumé</h5>
            ☀️ <b>PV :</b> {round(total_pv_connected, 2)} kWh<br>
            🔋 <b>Véhicule :</b> {round(total_ev, 2)} kWh ({ev_pct}%)<br>
            🏡 <b>Autonomie :</b> {self_suff_pct}%<br>
            🔌 <b>Charge PV :</b> {ev_charge_pv} kWh<br>
            ⚡ <b>Charge Réseau :</b> {ev_charge_grid} kWh<br>
            🔻 <b>Décharge :</b> {round(energy_discharged_kWh, 2)} kWh<br>
            💰 <b>Économies :</b> {abs(savings)} €
            </div>
            """, unsafe_allow_html=True
        )

except Exception as e:
    st.error(f"Erreur lors de la simulation : {e}")
