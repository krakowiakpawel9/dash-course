import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Input(id='input-1', value='', type='text'),
    html.Div(id='div-1', children='')

])

@app.callback(
    Output(component_id='div-1', component_property='children'),
    [Input(component_id='input-1', component_property='value')]
)
def update_div(input):
    return f'Wprowadzono: {input}'

if __name__ == '__main__':
    app.run_server(debug=True)