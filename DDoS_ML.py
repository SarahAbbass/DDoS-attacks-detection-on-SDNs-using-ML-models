# -*- coding: utf-8 -*-
"""EECE 490-M3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1amfBeMoL-SOQ6pTMd8Sdc2hETtFsJkHE

SVM

# SVM
"""

import numpy as np
import pandas as pd
import pickle
import joblib
import matplotlib.pyplot as plt
from numpy import loadtxt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from tqdm import tqdm
from xgboost import plot_importance
from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score

#run this if you want to upload the dataset from your google drive 
from google.colab import drive
drive.mount("/content/gdrive")

df= pd.concat(map(pd.read_csv, ['/content/gdrive/My Drive/metasploitable-2.csv', '/content/gdrive/My Drive/Normal_data.csv']), ignore_index=True)
df["Src IP"] = [float(str(i).replace(".", "")) for i in df["Src IP"]]
df["Dst IP"] = [float(str(i).replace(".", "")) for i in df["Dst IP"]]
df["Flow ID"] = [float(str(i).replace(".", "").replace("-", "")) for i in df["Flow ID"]]
df["Timestamp"] = [float(str(i).replace("/", "").replace(":", "").replace(" ","").replace("PM","")) for i in df["Timestamp"]]
print(df)

#run this if you want to upload dataset from local device
from google.colab import files
uploaded=files.upload()

# Import the dataset
df = pd.concact(map(pd.read_csv, ['metasploitable-2.csv','Normal_data.csv']), ignore_index=True)
df["Src IP"] = [float(str(i).replace(".", "")) for i in df["Src IP"]]
df["Dst IP"] = [float(str(i).replace(".", "")) for i in df["Dst IP"]]
df["Flow ID"] = [float(str(i).replace(".", "").replace("-", "")) for i in df["Flow ID"]]
df["Timestamp"] = [float(str(i).replace("/", "").replace(":", "").replace(" ","").replace("PM","")) for i in df["Timestamp"]]
print(df)

# Splitting dataset into features and label
X = df.drop('Label', axis=1)
y = df['Label']

# Splitting the dataset into the training set and the test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Feature scaling 
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Fitting SVM with the training set
SVM = SVC(kernel='linear', random_state=0)
SVM.fit(X_train, y_train)

# Testing the model by classifying the test set
y_pred = SVM.predict(X_test)

# Creating confusion matrix for evaluation
cm = confusion_matrix(y_test, y_pred)
cr = classification_report(y_test, y_pred)

# Print out confusion matrix and report
print(cm)
print(cr)

"""NB

# NB
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from xgboost import plot_importance
from numpy import loadtxt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
import pickle
from tqdm import tqdm
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import recall_score
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler

#run this if you want to upload the dataset from your google drive 
from google.colab import drive
drive.mount("/content/gdrive")

train= pd.concat(map(pd.read_csv, ['/content/gdrive/My Drive/metasploitable-2.csv', '/content/gdrive/My Drive/Normal_data.csv']))
train["Src IP"] = [float(str(i).replace(".", "")) for i in train["Src IP"]]
train["Dst IP"] = [float(str(i).replace(".", "")) for i in train["Dst IP"]]
train["Flow ID"] = [float(str(i).replace(".", "").replace("-", "")) for i in train["Flow ID"]]
train["Timestamp"] = [float(str(i).replace("/", "").replace(":", "").replace(" ","").replace("PM","")) for i in train["Timestamp"]]
print(train)

from sklearn import preprocessing 
for f in train.columns: 
  if train[f].dtype=='object': 
    label = preprocessing.LabelEncoder() 
    label.fit(list(train[f].values)) 
    train[f] = label.transform(list(train[f].values))
train.fillna((-999), inplace=True) 
train=np.array(train) 
train = train.astype(float)

train = pd.DataFrame(train)
#print(train)

X = train.drop(train.columns[[81]], axis=1)
y=train[train.columns[[81]]]

# split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7)

X_train = StandardScaler().fit_transform(X_train)
X_test = StandardScaler().fit_transform(X_test)

NB=GaussianNB()
NB.fit(X_train, y_train)

y_pred = NB.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("accuracy:",accuracy)

f1score=f1_score(y_test, y_pred, average='micro')
print("f1-acore:",f1score)

cm=confusion_matrix(y_test, y_pred)
print("confusion matrix:",cm)

print(classification_report(y_test, y_pred))

pr=precision_score(y_test,y_pred, average='micro')
print("Precision:",pr)

"""KNN

# KNN
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

#run this if you want to upload the dataset from your google drive 
from google.colab import drive
drive.mount("/content/gdrive")

#import the dataset 
df= pd.concat(map(pd.read_csv, ['/content/gdrive/My Drive/metasploitable-2.csv', '/content/gdrive/My Drive/Normal_data.csv']), ignore_index=True)
df["Src IP"] = [float(str(i).replace(".", "")) for i in df["Src IP"]]
df["Dst IP"] = [float(str(i).replace(".", "")) for i in df["Dst IP"]]
df["Flow ID"] = [float(str(i).replace(".", "").replace("-", "")) for i in df["Flow ID"]]
df["Timestamp"] = [float(str(i).replace("/", "").replace(":", "").replace(" ","").replace("PM","")) for i in df["Timestamp"]]

print(df)

#here we are preprocessing 

X=df.drop('Label',1)
y = df['Label'].values

#Split the training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

#feature Scaling
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#here we train the KNN algorithm to make predictions with it

KNN = KNeighborsClassifier(n_neighbors=5)
KNN.fit(X_train, y_train)

#make predictions on the test data 
y_pred = KNN.predict(X_test)

print(confusion_matrix(y_test, y_pred))

print(classification_report(y_test, y_pred))

"""RF

# RF
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report

#run this if you want to upload the dataset from your google drive 
from google.colab import drive
drive.mount("/content/gdrive")

#import the dataset 
df = pd.concat(map(pd.read_csv, ['/content/gdrive/My Drive/metasploitable-2.csv', '/content/gdrive/My Drive/Normal_data.csv']), ignore_index=True)
df["Src IP"] = [float(str(i).replace(".", "")) for i in df["Src IP"]]
df["Dst IP"] = [float(str(i).replace(".", "")) for i in df["Dst IP"]]
df["Flow ID"] = [float(str(i).replace(".", "").replace("-", "")) for i in df["Flow ID"]]
df["Timestamp"] = [float(str(i).replace("/", "").replace(":", "").replace(" ","").replace("PM","")) for i in df["Timestamp"]]

print(df)

#here we are preprocessing 
X = df.drop('Label',1)
y = df['Label'].values

# Splitting the dataset into the Training set and Test set
X_Train, X_Test, y_Train, y_Test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
X_Train = StandardScaler().fit_transform(X_Train)
X_Test = StandardScaler().fit_transform(X_Test)

# Fitting the classifier into the Training set
RF = RandomForestClassifier(n_estimators = 200, criterion = 'entropy', random_state = 0)
RF.fit(X_Train,y_Train)

# Predicting the test set results
y_Pred = RF.predict(X_Test)

# Making the Confusion Matrix 
cm = confusion_matrix(y_Test, y_Pred)
print(cm)

print(classification_report(y_Test, y_Pred))

"""DT

# DT
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier

#run this if you want to upload the dataset from your google drive 
from google.colab import drive
drive.mount("/content/gdrive")

#import the dataset 
df = pd.concat(map(pd.read_csv, ['/content/gdrive/My Drive/metasploitable-2.csv', '/content/gdrive/My Drive/Normal_data.csv']), ignore_index=True)
df["Src IP"] = [float(str(i).replace(".", "")) for i in df["Src IP"]]
df["Dst IP"] = [float(str(i).replace(".", "")) for i in df["Dst IP"]]
df["Flow ID"] = [float(str(i).replace(".", "").replace("-", "")) for i in df["Flow ID"]]
df["Timestamp"] = [float(str(i).replace("/", "").replace(":", "").replace(" ","").replace("PM","")) for i in df["Timestamp"]]

print(df)

#here we are preprocessing 
X = df.drop('Label',1)
y = df['Label'].values

# Splitting the dataset into the Training set and Test set
X_Train, X_Test, y_Train, y_Test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
X_Train = StandardScaler().fit_transform(X_Train)
X_Test = StandardScaler().fit_transform(X_Test)

# Fitting the classifier into the Training set
DT = DecisionTreeClassifier(max_depth=6, random_state=1)
DT.fit(X_Train, y_Train)

# Predicting the test set results
y_Pred = DT.predict(X_Test)

# Making the Confusion Matrix 
cm = confusion_matrix(y_Test, y_Pred)
print(cm)

print(classification_report(y_Test, y_Pred))

"""Stacked Model

# Stacked Model
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix, classification_report

#run this if you want to upload the dataset from your google drive 
from google.colab import drive
drive.mount("/content/gdrive")

#import the dataset 
df = pd.concat(map(pd.read_csv, ['/content/gdrive/My Drive/metasploitable-2.csv', '/content/gdrive/My Drive/Normal_data.csv']), ignore_index=True)
df["Src IP"] = [float(str(i).replace(".", "")) for i in df["Src IP"]]
df["Dst IP"] = [float(str(i).replace(".", "")) for i in df["Dst IP"]]
df["Flow ID"] = [float(str(i).replace(".", "").replace("-", "")) for i in df["Flow ID"]]
df["Timestamp"] = [float(str(i).replace("/", "").replace(":", "").replace(" ","").replace("PM","")) for i in df["Timestamp"]]

#here we are preprocessing 
X = df.drop('Label',1)
y = df['Label'].values

# Splitting the dataset into the Training set and Test set
X_Train, X_Test, y_Train, y_Test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
X_Train = StandardScaler().fit_transform(X_Train)
X_Test = StandardScaler().fit_transform(X_Test)

estimator_list = [
    ('SVM',SVM),
    ('NB',NB),
    ('KNN',KNN),
    ('RF',RF),
    ('DT',DT)
    ]

# Build and fit stack model
stack_model = StackingClassifier(
    estimators=estimator_list, final_estimator=LogisticRegression())
stack_model.fit(X_train, y_train)

# Make predictions
y_train_pred = stack_model.predict(X_train)
y_test_pred = stack_model.predict(X_test)

# Training set model performance
train_acc = accuracy_score(y_train, y_train_pred)  
train_f1 = f1_score(y_train, y_train_pred, average='weighted') 
train_pr=precision_score(y_train,y_train_pred, average='micro')


print('Model performance for Training set')
print('Accuracy: %s' % train_acc)
print('F1 score: %s' % train_f1)
print("Precision:%s",train_pr)

# Test set model performance
test_acc = accuracy_score(y_test, y_test_pred)  
test_f1 = f1_score(y_test, y_test_pred, average='weighted') 
test_pr=precision_score(y_test,y_test_pred, average='micro')

print('Model performance for Test set')
print('Accuracy: %s' % test_acc)
print('F1 score: %s' % test_f1)
print("Precision:%s",test_pr)

cm=confusion_matrix(y_test, y_test_pred)
print(cm)

print(classification_report(y_test, y_test_pred))

"""References

[1] 	icesonata, "DDoSDN," GitHub, January 6, 2021.
[2] 	devendra416, "ML-DDoS-Detection-SGB," GitHub, April 30, 2019.
[3] 	mahesh147, "Random-Forest-Classifier," GitHub, January 22, 2018.
[4] 	dataprofessor, "Stacking_Classifier," GitHub, April 11, 2021.
"""