import tensorflow as tf
from tensorflow import keras

from keras.layers import LSTM
from keras.models import Sequential
from keras.layers import Activation, Dropout, Dense
from keras.layers import Flatten, GlobalMaxPooling1D, Embedding, Conv1D, LSTM
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences

from core.config import Settings
from src.features.build_features import DataTransformation
from src.data.preprocess_datatsets import DataPreProcessing
from Handlers import log_database_handler

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logdb = log_database_handler.LogDBHandler()
logger.addHandler(logdb)

# Please uncomment/comment below line if you wish to stop/start logging
#logger.disabled = True

class TrainPipeline:

    def __init__(self) -> None:
        self.settings = Settings()

    def train(self):
        try:
            logger.info("data preprocessing started...")
            _data_preprocessing = DataPreProcessing()
            X_train, X_test, y_train, y_test = _data_preprocessing.get_train_test_data()
            logger.info("data preprocessing end...")
            logger.info("data transformation started...")
            _data_transformation = DataTransformation()
            embedding_matrix = _data_transformation.get_embedding_layers()
            logger.info("data transformation started...")
            logger.info("word tokenizer started...")
            word_tokenizer, X_train, X_test, vocab_length = _data_transformation.get_tokenizer(X_train, X_test, self.settings.MAXLEN)
            logger.info("word tokenizer end...")
            logger.info("create model started...")
            lstm_model = Sequential()
            embedding_layer = Embedding(vocab_length, 100, weights=[embedding_matrix], input_length=self.settings.MAXLEN , trainable=False)
            lstm_model.add(embedding_layer)
            lstm_model.add(LSTM(128))
            lstm_model.add(Dense(1, activation='sigmoid'))
            lstm_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
            logger.info("model training started...")
            lstm_model.fit(X_train, y_train, batch_size=128, epochs=6, verbose=1, validation_split=0.2)
            logger.info("model training end...")
            score = lstm_model.evaluate(X_test, y_test, verbose=1)
            logger.info("model saving started...")
            lstm_model.save(f"models/sentimentdl_glove_imdb_en.h5", save_format='h5')
            logger.info("model saving end...")
            logger.info("create model end...")
        except Exception as ex:
            logger.error(str(ex))

