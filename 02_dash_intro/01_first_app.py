"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[

    html.H2(children='Hello Dash'),

    html.Div(children='To moja pierwsza aplikacja w Pythonie!'),

    dcc.Graph(
        figure=go.Figure([
            go.Bar(
                x=[1, 2, 3],
                y=[2, 1, 3]
            )
        ])
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)