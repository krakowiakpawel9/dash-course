import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Tabs(
        id='tabs-1',
        children=[
            dcc.Tab(label='Python', value='py'),
            dcc.Tab(label='SQL', value='sql')
        ],
        value='py'
    ),

    html.Div(id='div-1')
])

@app.callback(
    Output('div-1', 'children'),
    [Input('tabs-1', 'value')]
)
def render_content(tab):
    if tab == 'py':
        return html.Div([
            dcc.Markdown("""
            ```
            print('Hello World')
            ```
            """)
        ])
    elif tab == 'sql':
        return html.Div([
            dcc.Markdown("""
            ```sql
            SELECT * FROM products;
            ```
            """)
        ])


if __name__ == '__main__':
    app.run_server(debug=True)