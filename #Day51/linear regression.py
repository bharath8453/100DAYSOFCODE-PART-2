from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Train
model = LinearRegression()
model.fit(X, y)

# Predict
print(model.predict([[6]]))  # ~12
