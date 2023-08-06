import tensorflow as tf
from tensorflow import keras

from keras.preprocessing.text import one_hot, Tokenizer
from keras.utils import pad_sequences

from numpy import asarray
from numpy import zeros

from src.data.preprocess_datatsets import DataPreProcessing
from core.config import Settings
from Handlers import log_database_handler

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logdb = log_database_handler.LogDBHandler()
logger.addHandler(logdb)

# Please uncomment/comment below line if you wish to stop/start logging
logger.disabled = True

class DataTransformation:

    def __init__(self) -> None:
        self.settings = Settings()

    def get_embedding_layers(self): 

        """
        # Embedding layer expects the words to be in numeric form 
        # Using Tokenizer function from keras.preprocessing.text library
        # Method fit_on_text trains the tokenizer 
        # Method texts_to_sequences converts sentences to their numeric form

        """
        _data_preprocessing = DataPreProcessing()
        X_train, X_test, y_train, y_test = _data_preprocessing.get_train_test_data()

        word_tokenizer, X_train, X_test, vocab_length = self.get_tokenizer(X_train, X_test, self.settings.MAXLEN)
        
        embeddings_dictionary = dict()
        glove_file = open(self.settings.GLOVE_6B_100D, encoding="utf8")

        for line in glove_file:
            records = line.split()
            word = records[0]
            vector_dimensions = asarray(records[1:], dtype='float32')
            embeddings_dictionary [word] = vector_dimensions
        glove_file.close()

        embedding_matrix = zeros((vocab_length, 100))
        for word, index in word_tokenizer.word_index.items():
            embedding_vector = embeddings_dictionary.get(word)
            if embedding_vector is not None:
                embedding_matrix[index] = embedding_vector

        return embedding_matrix
    
    def get_tokenizer(self, X_train, X_test, maxlen):

        word_tokenizer = Tokenizer()
        word_tokenizer.fit_on_texts(X_train)

        X_train = word_tokenizer.texts_to_sequences(X_train)
        X_test = word_tokenizer.texts_to_sequences(X_test)

        vocab_length = len(word_tokenizer.word_index) + 1

        X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)
        X_test = pad_sequences(X_test, padding='post', maxlen=maxlen)
        
        return word_tokenizer, X_train, X_test, vocab_length

