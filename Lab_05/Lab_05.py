
# Exercise 1 - XOR problem

# 0. First import libraries
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import tensorflow as tf
import matplotlib.pyplot as plt

# 1. prepare data
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 1, 1, 0]

# 2. Creating the model
model = Sequential()
model.add(Dense(2, input_dim=2, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))

# 3. Compile the model
optimizer = tf.keras.optimizers.SGD(learning_rate=0.5)
model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])

# 4. Model training
history = model.fit(X, y, epochs=700, batch_size=1, verbose=1)

# 5. Model evaluation
loss, accuracy = model.evaluate(X, y, verbose=1)
print('Accuracy: {:.2f}'.format(accuracy*100))

# 6. Model predictions
for id_x, data_sample in enumerate(X):
    prediction = model.predict([data_sample])
    print(f"Data sample is {data_sample}, prediction from model {prediction}, ground_truth {y[id_x]}")
  
# 7. Display loss function during the training process and acuracy
plt.figure(1)
plt.plot(history.history['loss'])
plt.xlabel('n epochs')
plt.ylabel('loss')
plt.show()



# Exercise 2 - Congressional Voting Data
import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import tensorflow as tf
import matplotlib.pyplot as plt

# 1. Loading dataset
path_to_dataset = 'D:\Temp\Práca\Python\MPA-MLF\Lab_05\\voting_complete.csv' # change the PATH
pd_dataset = pd.read_csv(path_to_dataset)

# 2. Train/Test Split

# define a function for train and test split
def train_test_split(pd_data: pd.DataFrame, test_ratio: float = 0.2) -> tuple:
    pd_dataset = pd_data.copy()
    pd_dataset = pd_dataset[pd_dataset.columns[1:]]
    index = np.arange(len(pd_dataset))
    index = np.random.permutation(index)
    train_ammount = int(len(index)*test_ratio)
    train_ids = index[train_ammount:]
    test_ids = index[:train_ammount]

    train_dataset = pd_dataset[pd_dataset.index.isin(train_ids)].reset_index()
    test_dataset = pd_dataset[pd_dataset.index.isin(test_ids)].reset_index()
    
    train_dataset = train_dataset[train_dataset.columns[1:]]
    test_dataset = test_dataset[test_dataset.columns[1:]]

    return train_dataset[train_dataset.columns[1:]], train_dataset[train_dataset.columns[0]], test_dataset[test_dataset.columns[1:]], test_dataset[test_dataset.columns[0]]

x_train, y_train, x_test, y_test = train_test_split(pd_dataset)

# 3. Data examination
print(x_train)

# 4. Data preprocessing
pd_dataset.replace('?', np.nan, inplace=True)
pd_dataset.replace('y', 1, inplace=True)
pd_dataset.replace('n', 0, inplace=True)
pd_dataset.replace('republican', 1, inplace=True)
pd_dataset.replace('democrat', 0, inplace=True)
pd_dataset = pd_dataset.drop(columns=['export-administration-act-south-africa'])

x_train, y_train, x_test, y_test = train_test_split(pd_dataset)
print(pd_dataset)

columns = x_train.columns
for column in columns:
    pd_dataset[column] = pd_dataset[column].fillna(x_train[column].value_counts().argmax())
    pd_dataset[column] = pd_dataset[column].astype('int')

x_train, y_train, x_test, y_test = train_test_split(pd_dataset)

# 5. Creating the model
# 5.1 Create your model using alteast one hidden layer
model = Sequential()
model.add(Dense(4, input_dim=len(columns), activation='relu'))
model.add(Dense(2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 5.2 Check what model.summary() does
model.summary()

# 5.3 Compile the model, choose a suitable loss function, choose gradient to descend optimizer and specify the learning rate, and choose accuracy as our metric
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)
model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])
history = model.fit(x_train, y_train, validation_split=0.33, epochs=1000, batch_size=32, verbose=1)

# 5.4 Train the model. Specify the number of epochs and batch size. Now is the time to create a validation dataset. Set 20% of dataset to be a validation dataset
loss, accuracy = model.evaluate(x_train, y_train, verbose=1)
print('Accuracy: {:.2f}'.format(accuracy*100))

# 6. Model Evaluation
# 6.1 Evaluate the model, print final accuracy and loss
loss, accuracy = model.evaluate(x_test, y_test, verbose=1)
print('Accuracy: {:.2f}'.format(accuracy*100))

# 6.2 Plot loss and validation loss depending on the training epochs into one graph. In another graph, plot accuracy and validation accuracy
print(history.history.keys())

plt.figure(2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('n epochs')
plt.ylabel('loss & validation loss')
plt.show()
plt.figure(3)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.xlabel('n epochs')
plt.ylabel('accuracy & validation accuracy')
plt.show()


