from sklearn.neighbors import KNeighborsClassifier

X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]

model = KNeighborsClassifier(n_neighbors=2)
model.fit(X, y)

print(model.predict([[1.5]]))
