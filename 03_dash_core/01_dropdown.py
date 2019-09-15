import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.Label('Wybierz preferowaną technologię:'),

    dcc.Dropdown(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'Java', 'value': 'jar'}
        ]
    ),

    dcc.Dropdown(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'Java', 'value': 'jar'}
        ],
        value='py'
    ),

    dcc.Dropdown(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'Java', 'value': 'jar'}
        ],
        value='py',
        multi=True
    ),

    dcc.Dropdown(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'Java', 'value': 'jar'}
        ],
        searchable=False
    ),

    dcc.Dropdown(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'Java', 'value': 'jar'}
        ],
        placeholder='Wybierz technologię...'
    ),

    dcc.Dropdown(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'Java', 'value': 'jar'}
        ],
        disabled=True
    )


])

if __name__ == '__main__':
    app.run_server(debug=True)