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

all_options = {
    'Language': ['Python', 'SQL', 'Java'],
    'Technology': ['Hadoop', 'Spark', 'Kafka']
}

app.layout = html.Div([

    dcc.RadioItems(
        id='radio-1',
        options=[{'label': key, 'value': key} for key in all_options.keys()],
        value='Language'
    ),

    html.Hr(),

    dcc.RadioItems(
        id='radio-2'
    ),

    html.Hr(),

    html.Div(id='div-1')
])

@app.callback(
    Output(component_id='radio-2', component_property='options'),
    [Input(component_id='radio-1', component_property='value')]
)
def set_options(selected_value):
    return [{'label': i, 'value': i} for i in all_options[selected_value]]

@app.callback(
    Output(component_id='div-1', component_property='children'),
    [Input(component_id='radio-1', component_property='value'),
     Input(component_id='radio-2', component_property='value')]
)
def update_div(selected1, selected2):
    return f'Wybrałeś {selected1} oraz {selected2}'

if __name__ == '__main__':
    app.run_server(debug=True)