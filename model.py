import pandas as pd
from sklearn.linear_model import LinearRegression

# Load train/val/test sets
X_train = pd.read_csv('X_train.csv')
X_val = pd.read_csv('X_val.csv')
X_test = pd.read_csv('X_test.csv')

y_train = pd.read_csv('y_train.csv')
y_val = pd.read_csv('y_val.csv')
y_test = pd.read_csv('y_test.csv')

#created model
reg_model = LinearRegression()

#trained model
reg_model.fit(X_train, y_train)

#predictions
reg_model_predictions = reg_model.predict(X_val)