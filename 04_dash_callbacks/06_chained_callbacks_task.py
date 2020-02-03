"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.RadioItems(
        id='radio-1',
        options=[
            {'label': 'Polska', 'value': 'Polska'},
            {'label': 'Stany Zjednoczone', 'value': 'Stany Zjednoczone'}
        ],
        value='Polska'
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
def set_radio_2_options(selected_country):
    if selected_country == 'Polska':
        return [{'label': 'Warszawa', 'value': 'Warszawa'},
                {'label': 'Kraków', 'value': 'Kraków'},
                {'label': 'Wrocław', 'value': 'Wrocław'}]
    elif selected_country == 'Stany Zjednoczone':
        return [{'label': 'New York', 'value': 'New York'},
                {'label': 'Los Angeles', 'value': 'Los Angeles'}]
    else:
        raise ValueError('Niepoprawna wartosc!')

@app.callback(
    Output(component_id='radio-2', component_property='value'),
    [Input(component_id='radio-1', component_property='value')]
)
def set_city(selected_country):
    if selected_country == 'Polska':
        return 'Warszawa'
    elif selected_country == 'Stany Zjednoczone':
        return 'New York'
    else:
        raise ValueError('Niepoprawna Wartosc')

@app.callback(
    Output(component_id='div-1', component_property='children'),
    [Input(component_id='radio-1', component_property='value'),
     Input(component_id='radio-2', component_property='value')]
)
def set_div(input1, input2):
    if input2 is None:
        return ''
    return f'Podałeś {input1} oraz {input2}'

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)