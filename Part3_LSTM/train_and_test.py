"""
Training and Testing for NLP Tensorflow-Based Keras Network
Created on 03/28/2020

Sources:
https://towardsdatascience.com/a-beginners-guide-on-sentiment-analysis-with-rnn-9e100627c02e
"""


# === Globals
NUM_WORDS = 10000
MAX_WORDS =1000

# === Imports
# System Imports

# 3rd Party Imports
from tensorflow import keras
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
import matplotlib.pyplot as pyplot
import numpy as np 

# System Imports
from models import models


# === Handle Data
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=NUM_WORDS)
# Pad
x_train = sequence.pad_sequences(x_train, maxlen=MAX_WORDS)
x_test =squence.pad_sequences(x_test, maxlen=MAX_WORDS)


# === Define Network
net = models.sentiNet(

)
