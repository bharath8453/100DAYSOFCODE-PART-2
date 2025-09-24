from sklearn.ensemble import RandomForestClassifier

X = [[0, 0], [1, 1], [0, 1], [1, 0]]
y = [0, 1, 1, 0]

model = RandomForestClassifier(n_estimators=10)
model.fit(X, y)

print(model.predict([[1, 0]]))
