from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Quantium Simulation Dashboard"),
    html.P("Setup complete!")
])

if __name__ == "__main__":
    app.run(debug=True)