import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def fetch_financial_data(company='AMZN'):
    """
    This function fetch stock market quotations.
    """
    import pandas_datareader.data as web
    return web.DataReader(name=company, data_source='stooq')

df = fetch_financial_data()
df.reset_index(inplace=True)
df = df[:30]
min_val = min(len(df), 30)

app.layout = html.Div([

    html.H4('Notowania spółki Amazon'),

    html.Table([
        html.Tr([html.Th(col) for col in df.columns])] +

        [html.Tr([html.Td(df.iloc[i][col]) for col in df.columns]) for i in range(min_val)]
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)