from sklearn.linear_model import LogisticRegression
import numpy as np

# Data: hours studied vs pass/fail
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([0, 0, 0, 1, 1])  # 0 = fail, 1 = pass

model = LogisticRegression()
model.fit(X, y)

print(model.predict([[3.5]]))  # Predict pass/fail
