"""
Tensorflow Keras Models for Sequential Inputs
Authored by John McKay, JMcKayPitt@gmail.com
Created on 03/28/2020

Sources:
https://towardsdatascience.com/a-beginners-guide-on-sentiment-analysis-with-rnn-9e100627c02e
"""


# === Imports

# System Imports

# 3rd Party Imports
from tensorflow import keras


# === Keras Models


def sentiNet(
    vocab_size,
    embed_size,
    words_size,
):
    """
    Sentiment Analysis Network

    Input
    =====
    input_shape: int
        Sequence length for network.
    activation: keras activation option
        Activation function to use within network.

    Output
    ======
    net: compiled tensorflow.keras network model
        RNN network for sentiment analysis.
    """

    net = keras.Sequential()
    net.add(keras.layers.Embedding(
        vocab_size,
        embed_size,
        input_length=words_size
    ))
    net.add(keras.layers.LSTM(100))
    net.add(keras.layers.Dense(1, activation='sigmoid'))

    return net
#


