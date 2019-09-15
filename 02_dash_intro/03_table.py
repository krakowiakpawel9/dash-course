import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.H4('Notowania spółki Amazon'),

    html.Table([

        html.Tr([
            html.Th('Date'),
            html.Th('Open'),
            html.Th('High'),
            html.Th('Low'),
            html.Th('Close'),
            html.Th('Volume')
        ]),

        html.Tr([
            html.Td('2019-09-01'),
            html.Td('100'),
            html.Td('102'),
            html.Td('98'),
            html.Td('100'),
            html.Td('150000')
        ]),

        html.Tr([
            html.Td('2019-09-02'),
            html.Td('101'),
            html.Td('103'),
            html.Td('98'),
            html.Td('100'),
            html.Td('140000')
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)