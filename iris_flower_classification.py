# -*- coding: utf-8 -*-
"""iris_flower_classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k-spLRZxDCm9LvrU-A044ifh7g4JHxbC

Name:-**Yusuf-Harun-Shaikh**



**Iris Flowers Classification ML Project**
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
!pip install scikit-plot
from scikitplot.estimators import plot_feature_importances
from scikitplot.metrics import plot_confusion_matrix, plot_roc
import scikitplot as skplt 
import os
import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd

np.random.seed(0)
import random


import tensorflow.keras as keras
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense,Dropout,Flatten
from tensorflow.keras.layers import Conv2D,MaxPool2D,BatchNormalization
from tensorflow.keras import backend as keras
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping,ReduceLROnPlateau,ModelCheckpoint
from keras.models import model_from_json


from keras.utils.vis_utils import plot_model


from sklearn.model_selection import train_test_split
from sklearn.model_selection import validation_curve
from sklearn.model_selection import learning_curve
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import scipy as sp
import warnings
warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree


import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

df = pd.read_csv('Iris.csv')

df.head()

df.tail()

df.shape

df.isnull()

df.isnull().sum()

df.describe()

df.columns

df.nunique()

df.Species.nunique()

df.Species.value_counts()

df.max()

df.min()

df.drop('Id' , axis=1, inplace=True)
df.head()

sns.boxplot(x='Species', y='PetalLengthCm', data=df)
plt.show()

sns.boxplot(x='Species', y='SepalWidthCm', data = df)

sns.boxplot(x='Species', y='SepalLengthCm', data=df)

sns.boxplot(x='Species', y='PetalWidthCm', data=df)

sns.boxplot(y='SepalLengthCm',data=df);
plt.show()

sns.boxplot(y='SepalWidthCm', data=df);
plt.show()

sns.boxplot(y='PetalLengthCm' , data=df);
plt.show()

sns.boxplot(y='PetalWidthCm' , data=df);
plt.show()

sns.pairplot(df, hue = 'Species')

plt.figure(figsize=(10,7))
sns.heatmap(df.corr(),annot=True,cmap="seismic")
plt.show()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

df['Species'] = le.fit_transform(df['Species'])
df.head()

x = df.drop(columns=['Species'])
y=df["Species"]
x[:5]

y[:5]

from sklearn.model_selection import  train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state = 1)

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB

lr = LogisticRegression()
knn = KNeighborsClassifier()
svm = SVC()
nb = GaussianNB()
dt = DecisionTreeClassifier()
rf = RandomForestClassifier()

from keras.models import load_model
from keras.models import Model
import os
import itertools
import codecs
import re
import datetime
import numpy as np
from scipy import ndimage
import pylab
from keras import backend as K
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers import Input, Dense, Activation
from keras.layers import Reshape, Lambda
from keras.layers.merge import add, concatenate
from keras.layers.recurrent import GRU
from keras.utils.data_utils import get_file
from keras.preprocessing import image
import keras.callbacks


models = [lr,knn,svm,nb,dt,rf]
scores = []
for model in models:
  model.fit(x_train, y_train)
  y_pred = model.predict(x_test)
  scores.append(accuracy_score(y_test,y_pred))
  print("Accuracy of " + type(model).__name__ + "is", accuracy_score(y_test,y_pred))

results = pd.DataFrame({
'Models':['Logistic Regression' , 'K-Nearest Neighbors', 'Support Vector Machine', 'Naive Bayes', 'Decission Tree', 'Random Forest'], 'Accuracy':scores})

results = results.sort_values(by="Accuracy", ascending=False)
print(results)

