import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load data
df = pd.read_csv("output.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Create line graph of sales over time
fig = px.line(
    df,
    x="date",
    y="sales",
    labels={"sales": "Sales", "date": "Date"}
)

fig.update_layout(
    plot_bgcolor="#0f2747",
    paper_bgcolor="#0f2747",
    font=dict(color="white"),
    margin=dict(l=20, r=20, t=40, b=20),
)
fig.update_xaxes(showgrid=True, gridcolor="#1f3b63")
fig.update_yaxes(showgrid=True, gridcolor="#1f3b63")
fig.update_traces(line=dict(color="#4cc9f0", width=2))

# Add vertical line for price increase
fig.add_vline(
    x=pd.to_datetime("2021-01-15"),
    line_dash="dash",
    line_color="#f72585"
)

fig.add_annotation(
    x=pd.to_datetime("2021-01-15"),
    y=df["sales"].max(),
    text="Price Increase",
    showarrow=True,
    arrowhead=1,
    ax=50,
    ay=-40,
    font=dict(color="#cbd5e0")
)

app = Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#0b1e3c",
        "padding": "30px",
        "fontFamily": "Arial"
    },
    children=[

        html.Div([
            html.H1(
                "PINK MORSEL SALES DASHBOARD",
                style={
                    "color": "white",
                    "letterSpacing": "2px",
                    "fontSize": "28px"
                }
            ),
            html.P(
                "Analysis of sales before and after price increase (Jan 15, 2021)",
                style={"color": "#a0aec0"}
            ),
        ], style={"marginBottom": "25px"}),

        # sales over time graph
        html.Div(
            children=[
                html.H3(
                    "SALES OVER TIME",
                    style={"color": "#cbd5e0", "marginBottom": "15px"}
                ),
                dcc.Graph(figure=fig)
            ],
            style={
                "backgroundColor": "#112d57",
                "padding": "20px",
                "borderRadius": "10px",
                "boxShadow": "0 4px 20px rgba(0,0,0,0.3)"
            }
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
