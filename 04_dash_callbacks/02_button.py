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

    html.Div([
        dcc.Input(id='input-1', type='text', value='Przykładowy tekst...')
    ]),

    html.Button(id='button-1', children='Submit', n_clicks=0),
    html.Div(id='div-1', children='Wprowadź tekst i przyciśnij Submit')
])

@app.callback(
    Output(component_id='div-1', component_property='children'),
    [Input(component_id='input-1', component_property='value'),
     Input(component_id='button-1', component_property='n_clicks')]
)
def update_output(value, n_clicks):
    return f'Wprowadziłeś {value} i nacisnąłeś przycisk {n_clicks} razy'

if __name__ == '__main__':
    app.run_server(debug=True)