import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import dash_table

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def fetch_financial_data(company='AMZN'):
    """
    This function fetch stock market quotations.
    """
    import pandas_datareader.data as web
    return web.DataReader(name=company, data_source='stooq')

df = fetch_financial_data()
df = df.reset_index()
df = df[:20]

app.layout = dash_table.DataTable(
    columns=[{'name': col, 'id': col} for col in df.columns],
    data=df.to_dict('records')
)

if __name__ == '__main__':
    app.run_server(debug=True)