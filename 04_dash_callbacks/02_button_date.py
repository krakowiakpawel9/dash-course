import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from datetime import datetime

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Button(id='btn-1', children='Button1', n_clicks_timestamp=0),
    html.Button(id='btn-2', children='Button2', n_clicks_timestamp=0),
    html.Button(id='btn-3', children='Button3', n_clicks_timestamp=0),
    html.Div(id='div-1')
])

@app.callback(
    Output('div-1', 'children'),
    [Input('btn-1', 'n_clicks_timestamp'),
     Input('btn-2', 'n_clicks_timestamp'),
     Input('btn-3', 'n_clicks_timestamp')]
)
def displayClick(btn1, btn2, btn3):
    if int(btn1) > int(btn2) and int(btn1) > int(btn3):
        msg = 'Button1 został wciśnięty jako ostatni'
    elif int(btn2) > int(btn1) and int(btn2) > int(btn3):
        msg = 'Button2 został wciśnięty jako ostatni'
    elif int(btn3) > int(btn1) and int(btn3) > int(btn2):
        msg = 'Button3 został wciśnięty jako ostatni'
    else:
        msg = 'Żaden przycisk nie został wciśnięty'
    return html.Div([
        html.Div(f'btn1: {datetime.fromtimestamp(btn1 / 1000)}'),
        html.Div(f'btn2: {datetime.fromtimestamp(btn2 / 1000)}'),
        html.Div(f'btn3: {datetime.fromtimestamp(btn3 / 1000)}'),
        html.Div(msg)
    ])

if __name__ == '__main__':
    app.run_server(debug=True)