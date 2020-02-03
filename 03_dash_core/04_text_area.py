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

    dcc.Textarea(
        placeholder='Wprowadź wartość',
        style={'width': '100%'},
        value=''
    ),

    dcc.Textarea(
        placeholder='Wprowadź wartość',
        style={'width': '60%'}
    ),

])

if __name__ == '__main__':
    app.run_server(debug=True)