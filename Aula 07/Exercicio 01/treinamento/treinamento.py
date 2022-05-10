import pickle
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

iris = datasets.load_iris()
X = iris.data[:, :2]
y = iris.target

estimator = RandomForestClassifier()
estimator.fit(X, y)

with open('model.pickle', 'wb') as files:
    pickle.dump(estimator, files)

print('terminado!')