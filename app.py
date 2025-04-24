# app.py
from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Welcome to My Data Product"),
    html.P("This is deployed on Render!")
])

# This is the magic for Render/Gunicorn
server = app.server

if __name__ == "__main__":
    app.run_server(debug=True)
