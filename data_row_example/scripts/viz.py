import os
import pandas as pd
import json
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# --- Define Relative Paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '..', 'data')
OUTPUT_DIR = os.path.join(BASE_DIR, '..', 'outputs')

# --- Load Data ---
with open(os.path.join(DATA_DIR, 'retention_kpi.json'), 'r') as f:
    retention_kpi = json.load(f)

student_composition_df = pd.read_csv(os.path.join(DATA_DIR, 'student_composition.csv'))
retention_by_school_df = pd.read_csv(os.path.join(DATA_DIR, 'retention_by_school.csv'))
district_withdrawals_df = pd.read_csv(os.path.join(DATA_DIR, 'district_withdrawals.csv'))
withdrawal_reasons_df = pd.read_csv(os.path.join(DATA_DIR, 'withdrawal_reasons.csv'))

# --- Style Definitions ---
BACKGROUND_COLOR = '#F8F9FA'
PLOT_BACKGROUND_COLOR = '#FFFFFF'
FONT_FAMILY = "Arial, sans-serif"
FONT_COLOR = "#555"
TITLE_FONT_COLOR = "#222"
MAIN_BLUE = 'rgb(42, 175, 221)'

REASON_COLORS = {
    'Elementary With': '#014B86',
    'EXP CAN\'T RET': '#F77E24',
    'OTHER (UNKNOWN)': '#8DC63F',
    'Enroll In Other': '#62C0DD',
    'Transferred to': '#522D80',
    'ADMIN WITHDRAW': '#ADD8E6',
    'HOME SCHOOLING': '#BACB1F'
}

# --- Create Subplots Layout ---
fig = make_subplots(
    rows=2, cols=2,
    specs=[[{"type": "xy"}, {"type": "bar"}], [{"type": "domain"}, {"type": "bar"}]],
    subplot_titles=[
        "<b>STUDENT RETENTION</b>",
        "<b>RETENTION BY SCHOOL</b>",
        "<b>TOP WITHDRAWAL REASONS</b>",
        "<b>DISTRICT WITHDRAWALS</b>"
    ],
    vertical_spacing=0.15,
    horizontal_spacing=0.05
)

# --- Plot 1: Student Retention Composition ---
fig.add_trace(go.Bar(
    y=student_composition_df['Category'],
    x=student_composition_df['Count'],
    orientation='h',
    marker_color=MAIN_BLUE,
    text=[f"{x/1000:.1f}K" for x in student_composition_df['Count']],
    textposition='outside',
    width=0.4,
    showlegend=False
), row=1, col=1)

fig.add_annotation(
    text=f"<b>{retention_kpi['retention_rate']}%</b>",
    x=0.05, y=0.8, xref="paper", yref="paper",
    showarrow=False, font=dict(size=48, color=MAIN_BLUE)
)
fig.add_annotation(
    text="Retention",
    x=0.05, y=0.7, xref="paper", yref="paper",
    showarrow=False, font=dict(size=16, color=FONT_COLOR)
)

# --- Plot 2: Retention by School ---
fig.add_trace(go.Bar(
    x=retention_by_school_df['Campus'],
    y=retention_by_school_df['RetentionRate'],
    marker_color=MAIN_BLUE,
    text=[f"{r}%" for r in retention_by_school_df['RetentionRate']],
    textposition='auto',
    showlegend=False
), row=1, col=2)

# --- Plot 3: Withdrawal Reasons Pie ---
pie_data = withdrawal_reasons_df[withdrawal_reasons_df['Percentage'] > 0].copy()
pie_data['LegendLabel'] = pie_data['Reason'].replace({
    'Elementary With': 'Elementar...',
    'EXP CAN\'T RET': 'CAN\'...',
    'OTHER (UNKNOWN)': 'Other...'
})

fig.add_trace(go.Pie(
    labels=pie_data['LegendLabel'],
    values=pie_data['Percentage'],
    hole=0.4,
    marker_colors=[REASON_COLORS.get(r, '#ccc') for r in pie_data['Reason']],
    textinfo='percent',
    hoverinfo='label+percent',
    showlegend=True
), row=2, col=1)

# --- Plot 4: Monthly Withdrawals Stacked Bar ---
months_order = ['August', 'September', 'October', 'November', 'December', 'January', 'February', 'March', 'April']
pivot_df = district_withdrawals_df.pivot_table(
    index='Month', columns='Reason', values='Count', aggfunc='sum'
).fillna(0).reindex(months_order)

for reason, color in REASON_COLORS.items():
    if reason in pivot_df.columns:
        fig.add_trace(go.Bar(
            name=reason,
            x=pivot_df.index,
            y=pivot_df[reason],
            marker_color=color
        ), row=2, col=2)

# Add total labels
totals = pivot_df.sum(axis=1)
fig.add_trace(go.Scatter(
    x=totals.index,
    y=totals,
    text=totals.astype(int),
    mode='text',
    textposition='top center',
    textfont=dict(color=FONT_COLOR, size=11),
    showlegend=False
), row=2, col=2)

# --- Layout Styling ---
fig.update_layout(
    height=750,
    width=1200,
    paper_bgcolor=BACKGROUND_COLOR,
    plot_bgcolor=PLOT_BACKGROUND_COLOR,
    font=dict(family=FONT_FAMILY, size=12, color=FONT_COLOR),
    barmode='stack',
    margin=dict(l=20, r=20, t=180, b=80),
    legend=dict(
        orientation="h",
        yanchor="bottom", y=-0.2,
        xanchor="center", x=0.5,
        bgcolor='rgba(0,0,0,0)',
        bordercolor='gray',
        borderwidth=1,
        font=dict(size=11)
    ),
    annotations=[
        go.layout.Annotation(
            text="<b>SchoolAnalytix®</b>",
            xref="paper", yref="paper",
            x=0.01, y=0.99, xanchor='left', yanchor='top',
            showarrow=False, font=dict(size=24, color=TITLE_FONT_COLOR)
        ),
        go.layout.Annotation(
            text="<span style='font-size: 24px;'><b>Student Retention</b></span><br><span style='color:#888'>Data Last Updated: 4/3/2023</span>",
            xref="paper", yref="paper",
            x=0.01, y=0.90, xanchor='left', yanchor='top',
            align='left', showarrow=False, font=dict(size=14, color=TITLE_FONT_COLOR)
        )
    ]
)

# --- Export Outputs ---
os.makedirs(OUTPUT_DIR, exist_ok=True)
fig.write_html(os.path.join(OUTPUT_DIR, "golden_image.html"))
fig.write_image(os.path.join(OUTPUT_DIR, "screenshot.png"))

print("✅ Dashboard exported to outputs/golden_image.html and screenshot.png")