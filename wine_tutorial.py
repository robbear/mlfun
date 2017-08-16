#
# From https://elitedatascience.com/python-machine-learning-tutorial-scikit-learn
#

# Import libraries and modules
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.externals import joblib 
 
# Load red wine data and format with the semicolon separator
print('Downloading the data...')
dataset_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(dataset_url, sep=';')

# Mark the target variable: 'quality'
y = data.quality

# Remove the quality feature from the data (axis=1 means column)
X = data.drop('quality', axis=1)

# Split data, X, into training and test sets, specifying the target variable data, y
# We use 20% of the data for testing, with the remaining 80% for training
print('Splitting the data into training and test...')
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=123, 
                                                    stratify=y)
 
# Declare data preprocessing steps
print('Declaring the pipeline...')
pipeline = make_pipeline(preprocessing.StandardScaler(), 
                         RandomForestRegressor(n_estimators=100))
                         
# List tuneable hyperparameters
#print('hyperparameters:')
#print(pipeline.get_params())
 
# Declare hyperparameters to tune
hyperparameters = { 'randomforestregressor__max_features' : ['auto', 'sqrt', 'log2'],
                  'randomforestregressor__max_depth': [None, 5, 3, 1]}
 
# Tune model using cross-validation pipeline
print('Tuning the model using the CV pipeline...')
clf = GridSearchCV(pipeline, hyperparameters, cv=10)

print('Fitting the training data...')
clf.fit(X_train, y_train)

print('Best parameters based on GridSearchCV and clf.fit results:')
print(clf.best_params_)
 
 
# Refit on the entire training set
# No additional code needed if clf.refit == True (default is True)
 
# Evaluate model pipeline on test data
print('Evaluating the model pipeline on the test data...')
pred = clf.predict(X_test)
print ("\nr2_score:", r2_score(y_test, pred))
print ("mean_squared_error:", mean_squared_error(y_test, pred))
 
# Save model for future use
#joblib.dump(clf, 'rf_regressor.pkl')
# To load: clf2 = joblib.load('rf_regressor.pkl')
