
# Exercise 1 - Text predictor

from keras.models import Sequential
from keras.layers import Dense, Activation, LSTM
from keras.optimizers import RMSprop
import numpy as np

text = open('kafka_Metamorphosis.txt', 'r', encoding="utf-8").read().lower()
print('text lenght: ',len(text))
print(text[:1000])

chars = sorted(list(set(text)))
print('total chars: ', len(chars))

char_indices = dict((c, i) for i,c in enumerate(chars))
indices_char = dict((i, c) for i,c in enumerate(chars))

maxlen = 40
step = 3
sentences = []
next_chars = []
for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])

print(sentences[:3])
print(next_chars[:3])

x = np.zeros((len(sentences), maxlen, len(chars)), dtype=bool)
y = np.zeros((len(sentences), len(chars)), dtype=bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        x[i, t, char_indices[char]] = 1
        y[i, char_indices[next_chars[i]]] = 1
        
print(x[:3])
print(y[:3])

model = Sequential()
model.add(LSTM(254, input_shape=(maxlen, len(chars))))
model.add(Dense(10*len(chars)))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))

model.compile(loss = 'categorical_crossentropy', optimizer = RMSprop(lr = 0.01))

model.fit(x, y, batch_size = 128, epochs = 100)

def sample(preds, temperature = 1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds)/temperature
    exp_preds = np.exp(preds)
    preds = exp_preds/np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

def generate_text(sentence, length, diversity):
    generated = ''
    generated += sentence
    for i in range(length):
        x_pred = np.zeros((1, maxlen, len(chars)))
        for t, char in enumerate(sentence):
            x_pred[0, t, char_indices[char]] = 1.
            
        preds = model.predict(x_pred, verbose = 0)[0]
        next_index = sample(preds, diversity)
        next_char = indices_char[next_index]
        
        generated += next_char
        sentence = sentence[1:] + next_char
        
    return generated

#%%
text = " the first thing he wanted to do was to "
sentence = text[0: maxlen]

print(generate_text(sentence, 30, 0.2))

