"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H2('Dash Tab Template'),
    dcc.Tabs(
        id='tabs-1',
        children=[
            dcc.Tab(label='Bar Plot', value='tab-1'),
            dcc.Tab(label='Line Plot', value='tab-2'),
            dcc.Tab(label='Scatter Plot', value='tab-3')
        ],
        value='tab-1'
    ),

    html.Div(id='div-1')
])

@app.callback(
    Output('div-1', 'children'),
    [Input('tabs-1', 'value')]
)
def render_content(tab):
    print(tab)
    if tab == 'tab-1':
        return html.Div([
            html.H3('Bar Plot Content'),
            dcc.Graph(
                figure={
                    'data': [
                        {'x': [1, 2, 3],
                         'y': [2, 1, 3],
                         'type': 'bar'}
                    ]
                }
            )
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Line Plot Content'),
            dcc.Graph(
                figure={
                    'data': [
                        {'x': [1, 2, 3, 4, 5],
                         'y': [2, 1, 3, 4, 2],
                         'type': 'line'}
                    ]
                }
            )
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Scatter Plot Content'),
            dcc.Graph(
                figure={
                    'data': [
                        {'x': [1, 2, 3, 4, 5],
                         'y': [2, 1, 3, 3, 2],
                         'mode': 'markers'}
                    ]
                }
            )
        ])


if __name__ == '__main__':
    app.run_server(debug=True)