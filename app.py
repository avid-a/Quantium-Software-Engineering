import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("output.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Create app
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

        # Main content
        html.Div(
            children=[

                html.H3(
                    "SALES OVER TIME",
                    style={"color": "#cbd5e0", "marginBottom": "15px"}
                ),

                # region filter
                html.Div(
                    children=[
                        html.P(
                            "Filter by Region:",
                            style={"color": "#a0aec0", "marginBottom": "8px"}
                        ),
                        dcc.RadioItems(
                            id="region-filter",
                            options=[
                                {"label": "All", "value": "all"},
                                {"label": "North", "value": "north"},
                                {"label": "East", "value": "east"},
                                {"label": "South", "value": "south"},
                                {"label": "West", "value": "west"},
                            ],
                            value="all",
                            labelStyle={
                                "display": "inline-block",
                                "marginRight": "15px",
                                "color": "#cbd5e0"
                            },
                            inputStyle={"marginRight": "5px"}
                        )
                    ],
                    style={"marginBottom": "20px"}
                ),

                dcc.Graph(id="sales-graph")

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

# Callback to update graph based on region filter
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    # Filter data based on selected region
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"].str.lower() == selected_region]

    # Create line chart
    fig = px.line(
        filtered_df,
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

    fig.update_traces(line=dict(color="#4cc9f0", width=2))

    fig.update_xaxes(showgrid=True, gridcolor="#1f3b63")
    fig.update_yaxes(showgrid=True, gridcolor="#1f3b63")

    # Add vertical line for price increase date
    fig.add_vline(
        x=pd.to_datetime("2021-01-15"),
        line_dash="dash",
        line_color="#f72585"
    )

    # Annotation for price increase
    fig.add_annotation(
        x=pd.to_datetime("2021-01-15"),
        y=filtered_df["sales"].max(),
        text="Price Increase",
        showarrow=True,
        arrowhead=1,
        ax=50,
        ay=-40,
        font=dict(color="#cbd5e0")
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)