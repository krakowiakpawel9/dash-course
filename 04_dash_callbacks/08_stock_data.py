"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

def fetch_financial_data(company='AMZN'):
    """
    This function fetch stock market quotations.
    """
    import pandas_datareader.data as web
    return web.DataReader(name=company, data_source='stooq')

df = fetch_financial_data()
df = df.reset_index()
df = df[df.Date > '2019-01-01']

df.to_csv('AMZN.csv')

print()