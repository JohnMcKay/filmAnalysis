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
from tensorflow import Keras


# === Keras Models


def sentiNet(
    input_shape,
    activation,
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

    net = keras.Sq
#


