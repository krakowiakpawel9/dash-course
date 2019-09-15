import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State
from datetime import datetime

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Upload(
        id='upload-1',
        children=html.Div([
            'Drag and drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'textAlign': 'center',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'lineHeight': '60px'
        },
        multiple=True
    ),

    html.Div(id='div-1')
])

def parse_contents(content, name, date):
    return html.Div([
        html.H5(name),
        html.H6(datetime.fromtimestamp(date)),
        html.Hr(),
        html.Img(src=content)
    ])

@app.callback(
    Output('div-1', 'children'),
    [Input('upload-1', 'contents')],
    [State('upload-1', 'filename'),
     State('upload-1', 'last_modified')]
)
def update_output(list_of_contents, list_of_names, list_of_dates):
    print(list_of_contents)
    print(list_of_names)
    print(list_of_dates)
    if list_of_contents is not None:
        children = [
            parse_contents(content, name, date) for content, name, date in zip(list_of_contents,
                                                                               list_of_names,
                                                                               list_of_dates)
        ]
        return children

if __name__ == '__main__':
    app.run_server(debug=True)