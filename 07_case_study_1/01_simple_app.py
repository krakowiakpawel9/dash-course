import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import base64

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

index_page = html.Div([
    html.H3('MENU:'),
    html.Hr(),
    html.Div([
        dcc.Link('Wybierz technologię', href='/tech'),
        html.Br(),
        dcc.Link('Wyświetl logo', href='/logo'),
        html.Hr()
    ]),
    html.H6('Korzystasz z aplikacji w fazie developmentu.')
])

tech_layout = html.Div([
    html.Div([
        html.H4('Wybierz technologię z podanych poniżej'),
        html.Hr(),
        dcc.Tabs(
            id='tech-1-tabs',
            children=[
                dcc.Tab(label='Python', value='tab-1'),
                dcc.Tab(label='SQL', value='tab-2'),
                dcc.Tab(label='Java', value='tab-3')
            ],
            value='tab-1'
        )
    ]),
    html.Div(id='tech-1-div'),
    html.Hr(),
    html.Div([
        dcc.Link('Wróć do MENU', href='/')
    ])
])

logo_layout = html.Div([
    html.Div([
        html.H4('Wybierz technologię, aby wyświetlić logo')
    ]),
    html.Hr(),
    dcc.RadioItems(
        id='logo-1-radio',
        options=[{'label': i, 'value': i} for i in ['Python', 'SQL', 'Java']]
    ),
    html.Hr(),
    html.Div(id='logo-1-div'),
    html.Hr(),
    dcc.Link('Wróć do MENU', href='/')
])

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/tech':
        return tech_layout
    elif pathname == '/logo':
        return logo_layout
    else:
        return index_page

@app.callback(
    Output('tech-1-div', 'children'),
    [Input('tech-1-tabs', 'value')]
)
def tech_1_tabs(value):
    if value == 'tab-1':
        return html.Div([
            dcc.Markdown('''
            ```
            def fetch_financial_data(company='AMZN'):
                """
                This function fetch stock market quotations.
                """
                import pandas_datareader.data as web
                return web.DataReader(name=company, data_source='stooq')
            ```
            ''')
        ])
    elif value == 'tab-2':
        return html.Div([
            dcc.Markdown('''
            ```sql
            CREATE TABLE Persons (
                PersonID int,
                LastName varchar(255),
                FirstName varchar(255),
                Address varchar(255),
                City varchar(255)
            );
            ```
            ''')
        ])
    elif value == 'tab-3':
        return html.Div([
            dcc.Markdown('''
            ```
            public class Hello {
              public static void main(String[] args){
                System.out.print("Hello World");
              }
            }       
            ```
            ''')
        ])

img_python = '/home/kranczers/PycharmProjects/dash-tut/07_case_study_1/python-logo.png'
img_db = '/home/kranczers/PycharmProjects/dash-tut/07_case_study_1/db-logo.png'
img_java = '/home/kranczers/PycharmProjects/dash-tut/07_case_study_1/java-logo.png'

encoded_img_python = base64.b64encode(open(img_python, 'rb').read())
encoded_img_db = base64.b64encode(open(img_db, 'rb').read())
encoded_img_java = base64.b64encode(open(img_java, 'rb').read())


@app.callback(
    Output('logo-1-div', 'children'),
    [Input('logo-1-radio', 'value')]
)
def logo_1_radio(value):
    if value is None:
        return html.Div([
            html.H6('Wybierz jedną z opcji, aby wyświetlić logo!')
        ])
    elif value == 'Python':
        return html.Div([
            html.Img(src=f'data:image/png;base64,{encoded_img_python.decode()}',
                     style={'width': '300px'})
        ])
    elif value == 'SQL':
        return html.Div([
            html.Img(src=f'data:image/png;base64,{encoded_img_db.decode()}',
                     style={'width': '300px'})
        ])
    elif value == 'Java':
        return html.Div([
            html.Img(src=f'data:image/png;base64,{encoded_img_java.decode()}',
                     style={'width': '300px'})
        ])


if __name__ == '__main__':
    app.run_server(debug=True, port=8051)