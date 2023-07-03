
# 1 - SVM for classification

# Load IRIS dataset, check its contents
from sklearn.datasets import load_iris
iris=load_iris()
iris.feature_names
print(iris.feature_names)
print(iris.data[0:5,:])
print(iris.target[0:5])
# print(iris.data)

# Split data into training and testing parts
from sklearn.model_selection import train_test_split
X=iris.data
y=iris.target
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
print(X_train.shape)
print(X_test.shape)
print(X.shape)

# Plot scatterplots of targets and check the separability of the classes
import matplotlib.pyplot as plt
plt.figure(1)
plt.scatter(X[y==0,0],X[y==0,1],color='green')
plt.scatter(X[y==1,0],X[y==1,1],color='blue')
plt.scatter(X[y==2,0],X[y==2,1],color='cyan')

# Use a Support Vector Machine for classification
from sklearn.svm import SVC
SVMmodel=SVC(kernel='linear')
SVMmodel.fit(X_train,y_train)
SVMmodel.get_params()
SVMmodel.score(X_test,y_test)
print(SVMmodel.score(X_test,y_test))

# Choose only first two features (columns) of iris.data
# SVM is in its basic form a 2-class classifier, so eliminate iris.target =2 from the data
X=iris.data[iris.target!=2,0:2]
y=iris.target[iris.target!=2]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
print(X_train.shape)
print(X_test.shape)
print(X.shape)

# Plot scatterplots of targets 0 and 1 and check the separability of the classes
plt.figure(2)
plt.scatter(X[y==0,0],X[y==0,1],color='green')
plt.scatter(X[y==1,0],X[y==1,1],color='blue')

# Train and test the SVM classifier, play with regularization parameter C (either use the default value or try e.g. 200)
SVMmodel=SVC(kernel='linear')
SVMmodel.fit(X_train,y_train)
SVMmodel.get_params()
SVMmodel.score(X_test,y_test)
print(SVMmodel.score(X_test,y_test))

# Show support vectors in the 2D plot, plot the decision line from equation [w0 w1]*[x0 x1] + b = 0
supvectors=SVMmodel.support_vectors_
# Plot the support vectors here
plt.figure(3)
plt.scatter(X[y==0,0],X[y==0,1],color='green')
plt.scatter(X[y==1,0],X[y==1,1],color='blue')
plt.scatter(supvectors[:,0],supvectors[:,1],color='red')

#Separating line coefficients
W=SVMmodel.coef_
b=SVMmodel.intercept_
print(W)
print(b)
import numpy as np
x0 = np.linspace(min(X[:,0]),max(X[:,0]),101)
print(x0)
x1 = -W[:,0]/W[:,1]*x0 - b/W[:,1]
plt.scatter(x0,x1,s=5)

# 2 - Anomaly detection via SVM

# Import one-class SVM and generate data (Gaussian blobs in 2D-plane)
from sklearn.svm import OneClassSVM
from sklearn.datasets import make_blobs
from numpy import quantile, where, random
random.seed(11)
x, _ = make_blobs(n_samples=300, centers=1, cluster_std=.3, center_box=(4, 4))
plt.figure(4)
plt.scatter(x[:,0], x[:,1])
plt.axis('equal')
plt.show()

# Train one-class SVM and plot the outliers (outputs of prediction being equal to -1)
SVMmodelOne = OneClassSVM(kernel='rbf', gamma=0.001, nu=0.03)
SVMmodelOne.fit(x)
pred = SVMmodelOne.predict(x)
anom_index = where(pred==-1)
values = x[anom_index]
plt.figure(5)
plt.scatter(x[:,0], x[:,1])
plt.scatter(values[:,0], values[:,1], color='red')
plt.axis('equal')
plt.show()

# Plot the support vectors
supvectors2=SVMmodelOne.support_vectors_
plt.figure(6)
plt.scatter(x[:,0], x[:,1])
plt.scatter(values[:,0], values[:,1], color='red')
plt.scatter(supvectors2[:,0],supvectors2[:,1],color='magenta')
plt.axis('equal')
plt.show()

# What if we want to have a control what is outlier? Use e.g. 5% "quantile" to mark the outliers. Every point with lower score than threshold will be an outlier.
scores = SVMmodelOne.score_samples(x)
thresh = quantile(scores, 0.05) # 5% quantile
print(thresh)
index = where(scores<=thresh)
values = x[index]
plt.figure(7)
plt.scatter(x[:,0], x[:,1])
plt.scatter(values[:,0], values[:,1], color='red')
plt.axis('equal')
plt.show()

