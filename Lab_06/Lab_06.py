
# Exercise 1 - Classification of an images

# 0. 0. Import libraries
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout
from keras.callbacks import EarlyStopping
from keras.optimizers import SGD
from keras.optimizers import Adam
from tensorflow.keras import regularizers
from keras.datasets import cifar10
from keras.utils import to_categorical
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

font = {'weight' : 'bold',
        'size'   : 12}
matplotlib.rc('font', **font)

# 1. Load the Dataset
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
labels = {0:'airplane',1:'automobile',2:'bird',3:'cat',4:'deer',5:'dog',6:'frog',7:'horse',8:'ship',9:'truck'}

# 2. Data Examination
def display_random_images(x_data: np.array, y_data: np.array, count: int = 10) -> None:
    index = np.array(len(x_data))
    selected_ind = np.random.choice(index, count)
    selected_img = x_data[selected_ind]
    selected_labels_encoded = y_data[selected_ind]
    selected_labels = [labels[x[0]] for x in selected_labels_encoded]
    concat_img = np.concatenate(selected_img, axis=1)
    plt.figure(figsize=(20,10))
    plt.imshow(concat_img)

    for id_label, label in enumerate(selected_labels):
        plt.text((32/2) + 32*id_label - len(label), 32*(5/4), label)
    plt.axis('off')
    plt.show()

display_random_images(X_train, y_train)

#check the shape of image dataset

X_train.shape

def display_channels_separately(image: np.array) -> None:
    plt.figure()
    fig, axs = plt.subplots(nrows=1, ncols=4, figsize=(10, 5))
    axs[0].imshow(image[:,:,0],cmap='Reds')
    axs[1].imshow(image[:,:,1],cmap='Blues')
    axs[2].imshow(image[:,:,2],cmap='Greens')
    axs[3].imshow(image)
    plt.show()

display_channels_separately(X_train[0])

# 3. Preprocessing of the images

X_train_scaled = X_train.astype('float32') / 255.0
y_train_encoded = to_categorical(y_train, num_classes=10)

# 4. Define the model architecture
p=0.1
model = Sequential()
model.add(Flatten(input_shape=(32, 32, 3)))
model.add(Dense(128*8, activation='relu'))
model.add(Dropout(p))
model.add(Dense(128*4, activation='relu'))
model.add(Dense(128*2, activation='relu'))
model.add(Dropout(p))
model.add(Dense(128*1, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.summary()
#optimizer = SGD(learning_rate = 0.001)
optimizer = Adam(learning_rate = 0.001)

model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

# 5. Train the model
early_stopping = EarlyStopping(monitor='val_loss', patience=3),
history = model.fit(X_train_scaled, y_train_encoded, epochs=50, batch_size=128, validation_split = 0.2, callbacks=[early_stopping])

#6. Model evaluation
X_test = X_test.astype('float32') / 255.0
y_test_encoded = to_categorical(y_test, num_classes=10)

score = model.evaluate(X_test, y_test_encoded, verbose=0)
print('Test loss:', score[0])
print(f'Test accuracy: {score[1]*100} %')

plt.figure()
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.figure()
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])

def show_the_best_predictions(model, x_test: np.array, y_test: np.array, n_of_pred: int = 10) -> None:
    mapping = {0:'airplane',1:'automobile',2:'bird',3:'cat',4:'deer',5:'dog',6:'frog',7:'horse',8:'ship',9:'truck'}
    
    predictions = model.predict(x_test)
    y_test = y_test.reshape(1,-1)
    predictions_ind = np.argmax(predictions, axis=1)
    predictions_ind = predictions_ind.reshape(1, -1)
    corect_predictions = np.where(predictions_ind == y_test)
    rows_correct = corect_predictions[1]
    target_correct = y_test[0][rows_correct]
    max_samples = predictions[rows_correct, target_correct]
    selected_images = x_test[rows_correct]
    sorted_ind = np.argsort(max_samples)[::-1]
    images = []
    prob = []
    labels = []
    
    for ind in range(n_of_pred):
        index = sorted_ind[ind]
        labels.append(target_correct[index])
        prob.append(max_samples[index])
        images.append(selected_images[index])
        
    plt.figure(figsize=(20,10))
      
    images = np.concatenate(np.asarray(images),axis=1)
    plt.imshow(images)
    for ins in range(n_of_pred):
        texts = '{}: \n{:.3f} %'.format(mapping[labels[ins]], prob[ins]*100)
        plt.text((32/2) + 32*ins - len(mapping[labels[ins]]), 32*(5/4), texts)
        
    plt.axis('off')
    plt.show()

show_the_best_predictions(model, X_test, y_test)

# TASK
"""
1) Hyperparameter tuning
    number of neurons - 8x more
    number of hidden layers - added 5 hidden layers, avoid underfitting
    activation functions - with ReLU better results achieved
    learning rate - 0.001 is fine to avoid divergence
    optimizer change - Adam provides better results than SGD or RMSprop and Ftrl
    learning epochs - higher for better training
    batch size - tried more and less, 128 is the best
    
2) Regularization techniques
    Dropout - 2 dropouts with 0.1 probability to avoid overfitting
    L1, L2 regularization - tried but it made results worse, not used
    Early stopping - used to avoid overfitting, stops after aproximately 25 epochs
    
Results)
    Test accuracy - 50.89 %
    Test loss - 1.396
    Best predicions exceed 99.9 % accuracy
"""
