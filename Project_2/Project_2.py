
# Project 2 - Classification of room occupancy


# 0. Import libraries
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout, Conv2D, MaxPooling2D
from keras.callbacks import EarlyStopping
from keras.optimizers import Adam
from keras.utils import to_categorical
from keras.utils.vis_utils import plot_model
from tensorflow.keras.regularizers import L1, L2
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import image as mpimg

#%%

# 1. Load the Dataset and 2. Data Examination

# x_train

length_train = 8279 #8279

x_train_data=np.empty([length_train, 45, 51]).astype('float32')

for counter_load_x_train in range(0, length_train, 1):
    x_train_data_load = pd.read_csv('Train/CSV/img_' + str(counter_load_x_train) + '.csv', header=None).drop(columns=0).apply(pd.to_numeric, errors='coerce').fillna(0)
    x_train_data[counter_load_x_train,:,:] = x_train_data_load

# x_test

length_test = 3549 #3549

x_test_data=np.empty([length_test, 45, 51]).astype('float32')

for counter_load_x_test in range(0, length_test, 1):
    x_test_data_load = pd.read_csv('Test/CSV/img_' + str(counter_load_x_test) + '.csv', header=None).drop(columns=0).apply(pd.to_numeric, errors='coerce').fillna(0)
    x_test_data[counter_load_x_test,:,:] = x_test_data_load

# y_train

y_train_data = pd.read_csv('y_train.csv')

#%%

# 3. Data preprocessing

# Scaling

print(x_train_data.max())
x_train_scaled = x_train_data/x_train_data.max()
print(x_train_scaled.max())

print(x_test_data.max())
x_test_scaled = x_test_data/x_test_data.max()
print(x_test_scaled.max())

# One hot encoding

y_train_clear = y_train_data.drop(columns=['id'])
#print(y_train_clear)
y_train_nonencoded=y_train_clear - 1
#print(y_train_nonencoded)
y_train_encoded = to_categorical(y_train_nonencoded, num_classes=3)
#print(y_train_encoded)

#%%

# 4. Model building training

"""
# CNN
model = Sequential()
model.add(Conv2D(48, 3, activation='elu', input_shape=(45, 51, 1)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
#model.add(Dense(512, activation='selu', kernel_regularizer=L1(l1=0.0001)))
model.add(Dense(512, activation='selu'))
model.add(Dropout(0.2))
#model.add(Dense(32, activation='relu', kernel_regularizer=L2(l2=0.0001)))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(3, activation='softmax'))
model.summary()
"""

# MLP
p=0.2 # Dropout probability
model = Sequential()
model.add(Flatten(input_shape=(45, 51)))
model.add(Dense(2048, activation='relu'))
model.add(Dropout(p))
model.add(Dense(512, activation='relu'))
#model.add(Dense(512, activation='relu', kernel_regularizer=L1(l1=0.0001)))
model.add(Dropout(p))
model.add(Dense(128, activation='relu'))
#model.add(Dense(128, activation='relu', kernel_regularizer=L2(l2=0.0001)))
model.add(Dropout(p))
model.add(Dense(32, activation='relu'))
model.add(Dropout(p))
model.add(Dense(8, activation='relu'))
model.add(Dense(3, activation='softmax'))
model.summary()

#%%

# 5. Model training

model.compile(loss='categorical_crossentropy', optimizer=Adam(learning_rate = 0.0005), metrics=['accuracy'])
epochs = 50
batch_size = 64
validation_split = 0.2
early_stopping = EarlyStopping(monitor='val_loss', patience=5),

#history = model.fit(x_train_scaled, y_train_encoded, epochs=epochs, batch_size=batch_size, validation_split = validation_split)
history = model.fit(x_train_scaled, y_train_encoded, epochs=epochs, batch_size=batch_size, validation_split = validation_split, callbacks=[early_stopping])

#%%

# 6. Results prediction
y_predicted = model.predict(x_test_scaled)
y_encoded = np.where(y_predicted < 0.5, 0, 1)
y_decoded = np.argmax(y_encoded, axis=1)
identification = pd.DataFrame({"id":np.arange(length_test).T})
y_results = pd.DataFrame(np.add(y_decoded,1), columns = ['target'])
y_results_data = pd.concat([identification, y_results], axis=1)
y_results_data.to_csv('y_results.csv', index=False)

#%%

# 7. Model evaluation

score = model.evaluate(x_train_scaled, y_train_encoded, verbose=1)
print('Test loss:', score[0])
print(f'Test accuracy: {score[1]*100} %')
#print('Batch size: ', batch_size_list[batch_score.index(max(batch_score))])

plot_model(model, to_file = 'graph.png', show_shapes = True, show_layer_names = True)
plt.figure(0)
image = mpimg.imread('graph.png')
plt.imshow(image)
plt.show()

plt.figure(1)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.show()
plt.figure(2)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.show()

"""
plt.figure(3)
cm = confusion_matrix(y_results,y_results)
cm_display = ConfusionMatrixDisplay(confusion_matrix=cm)
cm_display.plot(cmap=plt.cm.Blues)
plt.show()
"""


