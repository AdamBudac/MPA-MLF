
# 1 - PCA through Singular Value Decomposition

import numpy as np
# Defined 3 points in 2D-space:
X=np.array([[2, 1, 0],[4, 3, 0]])
# Calculate the covariance matrix:
R=np.matmul(X,X.T)/3
# Calculate the SVD decomposition and new basis vectors:
[U,D,V]=np.linalg.svd(R)  # call SVD decomposition
u1=U[:,0] # new basis vectors
u2=U[:,1]

# Calculate the coordinates in new orthonormal basis:
Xi1=np.matmul(np.transpose(X),u1)
Xi2=np.matmul(np.transpose(X),u2)
print(Xi1)
print(Xi2)

Xaprox=np.matmul(u1[:,None],Xi1[None,:])#+np.matmul(u2[:,None],Xi2[None,:])
print(Xaprox)
Xaprox=np.matmul(u1[:,None],Xi1[None,:])+np.matmul(u2[:,None],Xi2[None,:])
print(Xaprox)



# 2 - PCA on Iris data

# Load Iris dataset as in the last PC lab:
from sklearn.datasets import load_iris
iris=load_iris()
iris.feature_names
print(iris.feature_names)
print(iris.data[0:5,:])
print(iris.target[:])

# We have 4 dimensions of data, plot the first three colums in 3D
X=iris.data
y=iris.target
import matplotlib.pyplot as plt
plt.figure(1)
axes1=plt.axes(projection='3d')
axes1.scatter3D(X[y==0,1],X[y==0,1],X[y==0,2],color='green')
axes1.scatter3D(X[y==1,1],X[y==1,1],X[y==1,2],color='blue')
axes1.scatter3D(X[y==2,1],X[y==2,1],X[y==2,2],color='magenta')
plt.show

# Pre-processing is an important step, you can try either StandardScaler (zero mean, unit variance of features)
# or MinMaxScaler (to interval from 0 to 1)
from sklearn.preprocessing import StandardScaler
Xscaler = StandardScaler()
Xpp=Xscaler.fit_transform(X)
print(np.mean(Xpp[:,0]))
print(np.std(Xpp[:,0]))
print(np.mean(X[:,0]))
print(np.std(X[:,0]))

from sklearn import decomposition
# define PCA object (three components), fit and transform the data
pca = decomposition.PCA(n_components=3)
pca.fit(Xpp)
Xpca = pca.transform(Xpp)
print(pca.get_covariance())
# you can plot the transformed feature space in 3D:
plt.figure(2)
axes2=plt.axes(projection='3d')
axes2.scatter3D(Xpca[y==0,0],Xpca[y==0,1],Xpca[y==0,2],color='green')
axes2.scatter3D(Xpca[y==1,0],Xpca[y==1,1],Xpca[y==1,2],color='blue')
axes2.scatter3D(Xpca[y==2,0],Xpca[y==2,1],Xpca[y==2,2],color='magenta')
plt.show

# Compute pca.explained_variance_ and pca.explained_cariance_ratio_values
pca.explained_variance_
print(pca.explained_variance_)
pca.explained_variance_ratio_
print(pca.explained_variance_ratio_)

# Plot the principal components in 2D, mark different targets in color
plt.figure(3)
plt.scatter(Xpca[y==0,0],Xpca[y==0,1],color='green')
plt.scatter(Xpca[y==1,0],Xpca[y==1,1],color='blue')
plt.scatter(Xpca[y==2,0],Xpca[y==1,1],color='magenta')
plt.show



# 3 - KNN classifier

# Import train_test_split as in last PC lab, split X (original) into train and test, train KNN classifier on full 4-dimensional X

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)
print(X_train.shape)
print(X_test.shape)
knn1=KNeighborsClassifier(n_neighbors = 3)
knn1.fit(X_train,y_train)
Ypred=knn1.predict(X_test)

# Import and show confusion matrix
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
confusion_matrix(y_test,Ypred)
ConfusionMatrixDisplay.from_predictions(y_test,Ypred)

# Now do the same (data set split, KNN, confusion matrix), but for PCA-transformed data (1st two principal components, i.e., first two columns). 
# Compare the results with full dataset
X_trainpca, X_testpca, y_trainpca, y_testpca = train_test_split(Xpca,y,test_size=0.3)
knn2=KNeighborsClassifier(n_neighbors = 3)
knn2.fit(X_trainpca,y_trainpca)
Ypredpca=knn2.predict(X_testpca)
confusion_matrix(y_testpca,Ypredpca)
ConfusionMatrixDisplay.from_predictions(y_testpca,Ypredpca)

# Now do the same, but use only 2-dimensional data of original X (first two columns)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X[:,0:1],y,test_size=0.3)
knn3=KNeighborsClassifier(n_neighbors = 3)
knn3.fit(X_train2,y_train2)
Ypred2=knn3.predict(X_test2)
confusion_matrix(y_test2,Ypred2)
ConfusionMatrixDisplay.from_predictions(y_test2,Ypred2)


