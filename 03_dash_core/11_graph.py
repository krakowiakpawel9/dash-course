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

app.layout = html.Div([

    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Bar(
                    x=[2017, 2018, 2019],
                    y=[219, 146, 167],
                    name='Sprzedaż USA',
                    marker=go.bar.Marker(
                        color='rgb(55, 83, 109)'
                    )
                ),
                go.Bar(
                    x=[2017, 2018, 2019],
                    y=[230, 180, 260],
                    name='Sprzedaż Europa',
                    marker=go.bar.Marker(
                        color='rgb(26, 118, 255)'
                    )
                )
            ],
            layout=go.Layout(
                title='Sprzedaż',
                showlegend=True
            )
        )
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)