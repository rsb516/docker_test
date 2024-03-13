

# Load Libraries
from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score


# Load Data
iris = load_iris()

X = iris.data 

y = iris.target


# Split data

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)



# train a logistic regression 

clf = LogisticRegression()

clf.fit(X_train, y_train)



# Make Predictions

y_pred = clf.predict(X_test)


# Print the Accuray of the model

accuracy_score = accuracy_score(y_test, y_pred)

print(f'Accuracy: {accuracy_score}')