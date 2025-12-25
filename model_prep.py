import pandas as pd

df = pd.read_csv('features_scaled.csv')
print(df.columns)

#defined target variable
df['target'] = df['next_day_change']

#creating feature matrix X
#starting by dropping columns that are not needed for the prediction

matrix_x = df.drop(columns = ['ticker', 'date', 'date_dt', 'target', 'next_day_change'])

matrix_y = df['target']

#splitting data
#train 70%, validation 15% and then test 15% (old, middle, new)

n = len(df)

train_end = int(n * 0.70)

val_end = int(n * 0.85) #NOTE: where it ends/automatically goes to test end

#first 70%
X_train = matrix_x[:train_end]

#next 15%
X_val = matrix_x[train_end:val_end]

#final 15%
X_test = matrix_x[val_end:]