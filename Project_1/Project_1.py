
# Project 1 - Classification of wireless transmitters

# 0. Import libraries
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout
from keras.callbacks import EarlyStopping
from keras.optimizers import SGD, Adam
from keras.utils import to_categorical
from tensorflow.keras import regularizers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import gc

# 1. Load the Dataset
x_train_data = pd.read_csv('x_train.csv')
x_test_data = pd.read_csv('x_test.csv')
y_train_data = pd.read_csv('y_train.csv')

# 2. Data Examination
print(x_train_data)
print(x_test_data)
print(y_train_data)

# 3. Data preprocessing
x_train_clear = x_train_data.drop(columns=['Unnamed: 0','m_power','Tosc','Tmix'])
x_test_clear = x_test_data.drop(columns=['Unnamed: 0','m_power','Tosc','Tmix'])
y_train_clear = y_train_data.drop(columns=['id'])
print(x_train_clear)
print(x_test_clear)
print(y_train_clear)

y_train_nonencoded=y_train_clear-1
y_train_encoded = to_categorical(y_train_nonencoded, num_classes=8)
print(y_train_nonencoded)
print(y_train_encoded)

scaling_train = x_train_clear.abs().max()
x_train_scaled = x_train_clear / scaling_train
x_train_scaled = x_train_scaled.astype('float32')
print(x_train_scaled)

scaling_test = x_test_clear.abs().max()
x_test_scaled = x_test_clear / scaling_test
x_test_scaled = x_test_scaled.astype('float32')
print(x_test_scaled)

# 4. Model building, 5. Performance tunning and 6. Voluntary hyperparameter tuning algorithm

batch_size_list = [64, 128, 256]
batch_score = []

for batch_size in (batch_size_list):
    p=0.1 # Dropout probability
    model = Sequential()
    model.add(Flatten(input_shape=(8, 1)))
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(p))
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(p))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(8, activation='softmax'))
    model.summary()
    #optimizer = SGD(learning_rate = 0.001)
    optimizer = Adam(learning_rate = 0.0005)
    early_stopping = EarlyStopping(monitor='val_loss', patience=3),

    model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    history = model.fit(x_train_scaled, y_train_encoded, epochs=50, batch_size=batch_size, validation_split = 0.2, callbacks=[early_stopping])
    
    # 7. Model evaluation
    score = model.evaluate(x_train_scaled, y_train_encoded, verbose=1)
    print('Test loss:', score[0])
    print(f'Test accuracy: {score[1]*100} %')
    
    batch_score.append(score[1])
    del(model)
    del(history)
    gc.collect()

# 8. Best model training
p=0.1 # Dropout probability
model = Sequential()
model.add(Flatten(input_shape=(8, 1)))
model.add(Dense(256, activation='relu'))
model.add(Dropout(p))
model.add(Dense(128, activation='relu'))
model.add(Dropout(p))
model.add(Dense(32, activation='relu'))
model.add(Dense(8, activation='softmax'))
model.summary()
#optimizer = SGD(learning_rate = 0.001)
optimizer = Adam(learning_rate = 0.0005)
early_stopping = EarlyStopping(monitor='val_loss', patience=3),

model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
#history = model.fit(x_train_scaled, y_train_encoded, epochs=50, batch_size=64, validation_split = 0.2, callbacks=[early_stopping])
history = model.fit(x_train_scaled, y_train_encoded, epochs=50, batch_size=batch_size_list[batch_score.index(max(batch_score))], validation_split = 0.2, callbacks=[early_stopping])

# 9. Best model evaluation
score = model.evaluate(x_train_scaled, y_train_encoded, verbose=1)
print('Test loss:', score[0])
print(f'Test accuracy: {score[1]*100} %')
print('Batch size: ', batch_size_list[batch_score.index(max(batch_score))])

plt.figure()
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.figure()
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])

# 10. Results creation
y_predicted = model.predict(x_test_scaled)
y_encoded = np.where(y_predicted < 0.5, 0, 1)
y_decoded = np.argmax(y_encoded, axis=1)
identification = pd.DataFrame({"id":np.arange(3840).T})
y_results = pd.DataFrame(np.add(y_decoded,1), columns = ['target'])
y_results_data = pd.concat([identification, y_results], axis=1)
y_results_data.to_csv('y_results.csv', index=False)


