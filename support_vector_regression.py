# -*- coding: utf-8 -*-
"""support_vector_regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JMzA2kCSIJ_l238Dnb0gfwNw9Fn013eV

# Support Vector Regression (SVR)

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

print(X)

print(y)# result is in 1d we need to change to 2D then only we can do feature scale usind standardscalar class

y = y.reshape(len(y),1)# conversion into 2d array

print(y)# now its 2D

"""## Feature Scaling"""

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)# level column
y = sc_y.fit_transform(y) # salary column

print(X)  #-3 to 3 it will be the range after feature scaling

print(y) #-3 to 3 it will be the range after feature scaling

"""## Training the SVR model on the whole dataset"""

from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf') #non linear kernel is rbf
regressor.fit(X, y)

"""## Predicting a new result"""

sc_y.inverse_transform(regressor.predict(sc_X.transform([[6.5]])).reshape(-1,1)) #we apply reverse scale to get output y which is salary in original form we use inverse_transform

"""## Visualising the SVR results"""

plt.scatter(sc_X.inverse_transform(X), sc_y.inverse_transform(y), color = 'red')
plt.plot(sc_X.inverse_transform(X), sc_y.inverse_transform(regressor.predict(X).reshape(-1,1)), color = 'blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

"""## Visualising the SVR results (for higher resolution and smoother curve)"""

X_grid = np.arange(min(sc_X.inverse_transform(X)), max(sc_X.inverse_transform(X)), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(sc_X.inverse_transform(X), sc_y.inverse_transform(y), color = 'red')
plt.plot(X_grid, sc_y.inverse_transform(regressor.predict(sc_X.transform(X_grid)).reshape(-1,1)), color = 'blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()