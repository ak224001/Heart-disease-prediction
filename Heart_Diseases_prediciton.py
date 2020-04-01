# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 22:58:40 2020

@author: Aditya
"""

import pandas as pd
import numpy as np

# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category = FutureWarning)
# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category = FutureWarning)
from sklearn.metrics import accuracy_score

#read data file
df = pd.read_csv('heart.csv')

### 1 = male, 0 = female
df.isnull().sum()


import matplotlib.pyplot as plt
import seaborn as sns

# distribution of target vs age 
sns.set_context("paper", font_scale = 2, rc = {"font.size": 20,"axes.titlesize": 25,"axes.labelsize": 20}) 
sns.catplot(kind = 'count', data = df, x = 'age', hue = 'target', order = df['age'].sort_values().unique())
plt.title('Variation of Age for each target class')
plt.show()


###### data preprocessing
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

#split data into training and test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.preprocessing import StandardScaler as ss
sc = ss()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)



#########################################   SVM   #############################
from sklearn.svm import SVC
model = SVC(kernel = 'rbf')
model.fit(X_train, y_train)

# Predicting the Test set results
y_pred = model.predict(X_test)

from sklearn.metrics import confusion_matrix
cm_test = confusion_matrix(y_pred, y_test)

y_pred_train = model.predict(X_train)
cm_train = confusion_matrix(y_pred_train, y_train)


print()
print('Accuracy for training set for svm = {}'.format((cm_train[0][0] + cm_train[1][1])/len(y_train)))
print('Accuracy for test set for svm = {}'.format((cm_test[0][0] + cm_test[1][1])/len(y_test)))


######Saving model to disk
import pickle
pickle.dump(model,open('model.pkl','wb'),protocol=2)
#######save the scaler
pickle.dump(sc, open('scaler.pkl', 'wb'),protocol=2)


#Loading model to get the result
model= pickle.load(open('model.pkl','rb'))

# load the scaler
scaler = pickle.load(open('scaler.pkl', 'rb'))
_, X_test, _, y_test = train_test_split(X, y, test_size=0.33, random_state=1)
data_ex_scaled = scaler.transform(X_test)
#print(data_ex_scaled)
yhat = (model.predict(data_ex_scaled))
#print(model.predict(np.array([64,	1	,3	,170	,227	,0	,0	,155,	0	,0.6,	1,	0,	3])))

# evaluate accuracy
acc = accuracy_score(y_test, yhat)
x2 = scaler.transform(np.array([[64,1,3,170,227,0,0,155,0,0.6,1,0,3]]))
print(model.predict(x2))