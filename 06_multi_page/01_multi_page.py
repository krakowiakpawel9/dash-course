import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Link('Przejdź do /', href='/'),
    html.Hr(),
    dcc.Link('Przejdź do /page-2', href='/page-2'),
    html.Hr(),

    html.Div(id='div-1')
])

@app.callback(
    Output('div-1', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    print(pathname)
    return html.Div([
        html.H3(f'Jesteś na stronie {pathname}')
    ])

if __name__ == '__main__':
    app.run_server(debug=True)