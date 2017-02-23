from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

iris = load_iris()

X = iris.data
y = iris.target

knn = KNeighborsClassifier(n_neighbors=5)
lr = LogisticRegression()

knn.fit(X, y)

label = knn.predict([[3, 5, 4, 2]])

print("knn: ", end="")
print(label)

lr.fit(X, y)

label = lr.predict([[3, 5, 4, 2]])
print("lr: ", end="")
print(label)