import pandas as pd
import numpy as np

np.random.seed(10)
url = 'https://ml-repository-krakers.s3-eu-west-1.amazonaws.com/dash_course/data.csv'
df_raw = pd.read_csv(url, index_col=0)

# %%
cols = ['Year', 'Fuel_Type', 'Transmission', 'Engine', 'Power', 'Seats', 'Price']

df = df_raw.copy()
df = df[cols]

# %%

df.Engine = df.Engine.str.split(' ').str[0]
df.Power = df.Power.str.split(' ').str[0].replace('null', np.nan)

df = df.dropna()

df.Engine = df.Engine.astype('float32')
df.Power = df.Power.astype('float32')
df.Seats = df.Seats.astype('float32')

df = pd.get_dummies(df, drop_first=True)
df.to_csv('./datasets/data_cleaned.csv')
# %%
X = df.copy()
y = X.pop('Price')

# %%
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y)
# %%
from sklearn.ensemble import RandomForestRegressor

reg = RandomForestRegressor()
reg.fit(X_train, y_train)
print(reg.score(X_test, y_test))

# %%
from sklearn.model_selection import GridSearchCV

param_grid = [{'max_depth': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30],
               'min_samples_leaf': [3, 4, 5, 10, 15]}]

model = RandomForestRegressor()

gs = GridSearchCV(model, param_grid=param_grid, scoring='r2', n_jobs=-1)
gs.fit(X_train, y_train)

model = gs.best_estimator_
print(model.score(X_test, y_test))

# %%
import pickle

with open('model.pickle', 'wb') as file:
    pickle.dump(model, file)

# %%
X_train.iloc[0]



















