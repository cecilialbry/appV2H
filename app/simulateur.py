import pandas as pd
import plotly.graph_objects as go

def lancer_simulation():
    heures = list(range(24))
    soc = [50 + i for i in heures]  # Juste un exemple simple
    maison = [1.5 + (i % 4) for i in heures]
    pv = [0.2*i if 6 <= i <= 18 else 0 for i in heures]

    df = pd.DataFrame({
        'Hour': heures,
        'SoC': soc,
        'HouseDemand': maison,
        'PV': pv
    })

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Hour'], y=df['SoC'], name='SoC (%)'))
    fig.add_trace(go.Scatter(x=df['Hour'], y=df['HouseDemand'], name='House Demand (kWh)'))
    fig.add_trace(go.Scatter(x=df['Hour'], y=df['PV'], name='PV Production (kWh)'))

    fig.update_layout(title="V2H Simulation", xaxis_title="Hour", yaxis_title="kWh / %")

    return df, fig
