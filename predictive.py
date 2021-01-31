import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

data_df = pd.DataFrame(pd.read_csv('data.csv', index_col = 0))

data_df = data_df.set_index('name')
X_train, X_test, y_train, y_test = train_test_split(data_df[['age', 'hits', 'potential']], data_df[['overall']], test_size=0.1)
model = sm.OLS(np.asarray(y_train), np.asarray(X_train))
results = model.fit()
# print(results.summary())

y_pred = results.predict(np.asarray(X_test))
mse = mean_squared_error(np.asarray(y_test), y_pred)
rmse = mse**0.5

print("Root mean square error ->", rmse)

plt.legend(loc='lower right')

plt.scatter(y_pred, np.asarray(y_test), 10, label='Prediction of Fifa player Score')
plt.title("Prediction of Fifa player Score'")
plt.xlabel('Predition')
plt.ylabel('Reality')
plt.show()