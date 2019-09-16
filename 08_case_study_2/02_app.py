import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pickle
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


with open('model.pickle', 'rb') as file:
    model = pickle.load(file)

df = pd.read_csv('./datasets/data_cleaned.csv', index_col=0)

# dfp = pd.DataFrame(
#     data=[
#         [2008, 2982, 171, 7, 'Diesel', 'Manual']
#     ],
#     columns=['Year', 'Engine', 'Power', 'Seats', 'Fuel_Type_Diesel',
#        'Fuel_Type_Electric', 'Fuel_Type_LPG', 'Fuel_Type_Petrol',
#        'Transmission_Manual']
# )
X = df.copy()
y = X.pop('Price')

print(model.predict(X.iloc[:1, :]))

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
        html.H3('Model Uczenia Maszynowego - Regresyjny Model Przewidywania Ceny Samochodów Używanych'),
        html.H6('Model Lasów Losowych (biblioteka scikit-learn)')
    ], style={'textAlign': 'center'}),
    html.Hr(),
    html.Div([
        html.Label('Podaj rok produkcji samochodu:'),
        dcc.Slider(
            id='slider-1',
            min=df.Year.min(),
            max=df.Year.max(),
            step=1,
            marks={i: str(i) for i in range(df.Year.min(), df.Year.max() + 1)},
            tooltip={'placement': 'bottom'}
        ),
        html.Br(),
        html.Label('Podaj rozmiar silnika:'),
        dcc.Slider(
            id='slider-2',
            min=0,
            max=6000,
            step=1,
            marks={i: str(i) for i in range(0, 6001, 500)},
            tooltip={'placement': 'bottom'}
        ),
        html.Br(),
        html.Label('Podaj moc samochodu:'),
        dcc.Slider(
            id='slider-3',
            min=30,
            max=580,
            step=1,
            marks={i: str(i) for i in range(30, 581, 50)},
            tooltip={'placement': 'bottom'}
        ),
        html.Br(),
        html.Label('Podaj liczbę pasażerów:'),
        html.Div([
            dcc.Dropdown(
                id='dropdown-1',
                options=[
                    {'label': i, 'value': i} for i in [2, 4, 5, 6, 7, 8, 9, 10]
                ]
            )
        ], style={'width': '20%', 'textAlign': 'left'}),
        html.Br(),
        html.Label('Podaj typ paliwa:'),
        html.Div([
            dcc.Dropdown(
                id='dropdown-2',
                options=[
                    {'label': i, 'value': j} for i, j in zip(['Diesel', 'Benzyna', 'CNG', 'LPG', 'Elektryczny'],
                                                             ['Diesel', 'Petrol', 'CNG', 'LPG', 'Electric'])
                ]
            )
        ], style={'width': '20%', 'textAlign': 'left'}),
        html.Br(),
        html.Label('Podaj typ przekładni:'),
        html.Div([
            dcc.RadioItems(
                id='radio-1',
                options=[{'label': i, 'value': j} for i, j in zip(['Manualna', 'Automatyczna'],
                                                                  ['Manual', 'Automatic'])]
            )
        ]),
        html.Div([
            html.Hr(),
            html.H3('Predykcja na podstawie modelu'),
            html.Hr(),
            html.H4('Podałeś następujące parametry:'),
            html.Div(id='div-1'),
            html.Div(id='div-2'),
            html.Hr()
        ], style={'margin': '0 auto', 'textAlign': 'center'})
    ], style={'width': '80%', 'textAlign': 'left', 'margin': '0 auto', 'fontSize': 22})
])

fuel_type = {'Diesel': 'Diesel', 'Petrol': 'Benzyna', 'CNG': 'CNG',
             'LPG': 'LPG', 'Electric': 'Elektryczny'}
transmission = {'Manual': 'Manualna', 'Automatic': 'Automatyczna'}


@app.callback(
    Output('div-1', 'children'),
    [Input('slider-1', 'value'),
     Input('slider-2', 'value'),
     Input('slider-3', 'value'),
     Input('dropdown-1', 'value'),
     Input('dropdown-2', 'value'),
     Input('radio-1', 'value')]
)
def display_parameters(val1, val2, val3, val4, val5, val6):
    if val1 and val2 and val3 and val4 and val5 and val6:
        val5 = fuel_type[val5]
        val6 = transmission[val6]
        return html.Div([
            html.H6(f'Rok produkcji: {val1}'),
            html.H6(dcc.Markdown(f'Pojemność silnika: {val2} cm<sup>3</sup>',
                                 dangerously_allow_html=True)),
            html.H6(f'Moc silnika: {val3} KM'),
            html.H6(f'Liczba pasażerów: {val4}'),
            html.H6(f'Typ paliwa: {val5}'),
            html.H6(f'Typ przekładni: {val6}')
        ], style={'textAlign': 'left'})
    else:
        return html.Div([
            html.H6('Podaj wszystkie parametry!')
        ])

@app.callback(
    Output('div-2', 'children'),
    [Input('slider-1', 'value'),
     Input('slider-2', 'value'),
     Input('slider-3', 'value'),
     Input('dropdown-1', 'value'),
     Input('dropdown-2', 'value'),
     Input('radio-1', 'value')]
)
def predict_value(val1, val2, val3, val4, val5, val6):
    if val1 and val2 and val3 and val4 and val5 and val6:

        val5_1, val5_2, val5_3, val5_4 = 0, 0, 0, 0

        if val5 == 'Diesel':
            val5_1 = 1
        elif val5 == 'Electric':
            val5_2 = 1
        elif val5 == 'LPG':
            val5_3 = 1
        elif val5 == 'Petrol':
            val5_4 = 1

        if val6 == 'Manual':
            val6 = 1
        else:
            val6 = 0


        df = pd.DataFrame(
            data=[
                [val1, val2, val3, val4, val5_1, val5_2, val5_3, val5_4, val6]
            ],
            columns=['Year', 'Engine', 'Power', 'Seats', 'Fuel_Type_Diesel',
                     'Fuel_Type_Electric', 'Fuel_Type_LPG', 'Fuel_Type_Petrol',
                     'Transmission_Manual']
        )
        print(df)

        price = model.predict(df)[0]
        price = round(price * 1000, 2)
        return html.Div([
            html.H4(f'Sugerowana cena ${price}')
        ])


if __name__ == '__main__':
    app.run_server(debug=True)
