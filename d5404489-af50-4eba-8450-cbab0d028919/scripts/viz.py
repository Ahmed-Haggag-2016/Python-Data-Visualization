import os
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# --- Setup paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '..', 'data')
OUTPUT_DIR = os.path.join(BASE_DIR, '..', 'outputs')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- Load Data ---
composition_df = pd.read_csv(os.path.join(DATA_DIR, 'force_composition.csv'))
army_map_df = pd.read_csv(os.path.join(DATA_DIR, 'army_size_map.csv'))
budget_df = pd.read_csv(os.path.join(DATA_DIR, 'budget_allocation.csv'))

# --- 1. Choropleth Map: Army Size by Country ---
map_fig = px.choropleth(
    army_map_df,
    locations='Country',
    locationmode='country names',
    color='Army_Size',
    color_continuous_scale='Reds',
    title='Largest Ground Armies by Country',
    labels={'Army_Size': 'Troops'}
)
map_trace = map_fig.data[0]

# --- 2. Pie Chart: Global Force Composition ---
total_air = composition_df['Air_Units'].sum()
total_navy = composition_df['Navy_Units'].sum()
total_ground = composition_df['Ground_Units'].sum()

pie_trace = go.Pie(
    labels=['Air Units', 'Navy Units', 'Ground Units'],
    values=[total_air, total_navy, total_ground],
    marker=dict(colors=['#1f77b4', '#2ca02c', '#d62728']),
    hole=0.4,
    name='Force Composition'
)

# --- 3. Sankey Diagram: Budget Allocation ---
labels = budget_df['Force_Type'].tolist()
values = budget_df['Budget_USD_Billions'].tolist()

sankey_trace = go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color="lightblue"
    ),
    link=dict(
        source=[0]*len(labels),  # Dummy source node
        target=list(range(len(labels))),
        value=values
    )
)

# --- Create Subplots Layout ---
fig = make_subplots(
    rows=2, cols=2,
    specs=[
        [{"type": "choropleth"}, {"type": "domain"}],
        [{"type": "domain", "colspan": 2}, None]
    ],
    subplot_titles=[
        "<b>Army Size by Country</b>",
        "",  # Leave pie chart title blank
        "<b>Budget Allocation</b>"
    ],
    vertical_spacing=0.15,
    horizontal_spacing=0.05
)

# Add traces
fig.add_trace(map_trace, row=1, col=1)
fig.add_trace(pie_trace, row=1, col=2)
fig.add_trace(sankey_trace, row=2, col=1)

# Add custom title below pie chart
fig.add_annotation(
    text="<b>Force Composition</b>",
    x=0.78, y=0.48,
    xref="paper", yref="paper",
    showarrow=False,
    font=dict(size=14, color="#333"),
    align="center"
)

# --- Layout Styling ---
fig.update_layout(
    height=800,
    width=1200,
    title="<b>Global Military Forces Dashboard</b>",
    title_font=dict(size=22, family='Arial'),
    paper_bgcolor='#F9F9F9',
    plot_bgcolor='#FFFFFF',
    font=dict(family='Arial', size=12, color='#333'),
    margin=dict(t=80, b=40, l=40, r=40),
    legend=dict(
        orientation="h",
        yanchor="bottom", y=-0.2,
        xanchor="center", x=0.5,
        bgcolor='rgba(0,0,0,0)',
        bordercolor='gray',
        borderwidth=1
    )
)

# --- Export ---
fig.write_html(os.path.join(OUTPUT_DIR, 'dashboard.html'))
fig.write_image(os.path.join(OUTPUT_DIR, 'screenshot.png'))

print("✅ Dashboard exported to /outputs/Dashboard.html and screenshot.png")