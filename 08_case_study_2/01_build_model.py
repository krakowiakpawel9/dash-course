import pandas as pd
import numpy as np

df_train_raw = pd.read_csv('./datasets/train.csv', index_col=0)
df_test_raw = pd.read_csv('./datasets/test.csv', index_col=0)

# %%
df_train_num = df_train_raw.describe()
df_train_cat = df_train_raw.describe(include=['object'])
# %%
cols = ['Year', 'Kilometers_Driven', 'Fuel_Type', 'Transmission', 'Owner_Type',
        'Mileage', 'Engine', 'Power', 'Seats']

X_train = df_train_raw.copy()
X_train = X_train[cols + ['Price']]

X_test = df_test_raw.copy()
X_test = X_test[cols]
# %%
def preprocess(df):
    df.Mileage = df.Mileage.str.split(' ').str[0]
    df.Engine = df.Engine.str.split(' ').str[0]
    df.Power = df.Power.str.split(' ').str[0].replace('null', np.nan)
    
    df = df.dropna()
    
    df.Mileage = df.Mileage.astype('float32')
    df.Engine = df.Engine.astype('float32')
    df.Power = df.Power.astype('float32')
    df.Seats = df.Seats.astype('float32')

    df = pd.get_dummies(df, drop_first=True)
    return df

# %%
X_train = preprocess(X_train)
X_test = preprocess(X_test)    
y_train = X_train.pop('Price')
# %%
from sklearn.ensemble import RandomForestRegressor

reg = RandomForestRegressor()
reg.fit(X_train, y_train)

reg.predict(X_test)

