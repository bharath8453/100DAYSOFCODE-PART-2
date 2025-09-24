from sklearn.svm import SVC

X = [[0, 0], [1, 1], [0, 1], [1, 0]]
y = [0, 1, 1, 0]

model = SVC(kernel='linear')
model.fit(X, y)

print(model.predict([[1, 0]]))
