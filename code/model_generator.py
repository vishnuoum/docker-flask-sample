from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier as DT
import pickle

data = datasets.load_iris()
val_size = 0.2
seed = 42

x_train, y_train = data.data, data.target

model = DT()
model.fit(x_train,y_train)

with open("models/model.pk", "wb") as file:
    pickle.dump(model, file)