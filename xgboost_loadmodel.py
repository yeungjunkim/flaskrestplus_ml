# Train XGBoost model, save to file using joblib, load and make predictions
from numpy import loadtxt
import xgboost
from sklearn.externals import joblib
from sklearn import model_selection


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# load data
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=",")
# split data into X and y
X = dataset[:,0:8]
Y = dataset[:,8]
# split data into train and test sets
seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)


# # fit model no training data
# model = xgboost.XGBClassifier()
# model.fit(X_train, y_train)
# # save model to file
# joblib.dump(model, "xgboost_model.joblib.dat")

# y_pred = model.predict(X_test)
# predictions = [round(value) for value in y_pred]
# accuracy = accuracy_score(y_test, predictions)
# print("Accuracy: %.2f%%" % (accuracy * 100.0))
# some time later...

# load model from file
loaded_model = joblib.load("xgboost_model.joblib.dat")
# make predictions for test data
y_pred = loaded_model.predict(X_test)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))