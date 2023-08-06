from tensorflow import keras
from keras.models import load_model
import pandas as pd
import numpy as np
import typing

from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences

from core.config import Settings
from src.data.preprocess_datatsets import DataPreProcessing
from src.features.build_features import DataTransformation
from Handlers import log_database_handler

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logdb = log_database_handler.LogDBHandler()
logger.addHandler(logdb)

# Please uncomment/comment below line if you wish to stop/start logging
#logger.disabled = True

class PredictPipeline:

    def __init__(self) -> None:
        self.settings = Settings()

    def predict(self):
        try:
            logger.info("data preprocessing started...")
            _data_preprocessing = DataPreProcessing()
            X_train, X_test, y_train, y_test = _data_preprocessing.get_train_test_data()
            logger.info("data preprocessing end...")
            logger.info("model loading started...")
            pretrained_lstm_model = load_model(self.settings.MODEL_PATH)
            logger.info("model loading end...")
            sample_reviews = pd.read_csv(self.settings.UNSEEN_REVIEWS_DATA_PATH)

            unseen_processed = sample_reviews['Review Text'].apply(_data_preprocessing.preprocess_text)

            _data_transformation = DataTransformation()
            word_tokenizer, X_train, unseen_padded, vocab_length = _data_transformation.get_tokenizer(X_train, unseen_processed, self.settings.MAXLEN)
            logger.info("prediction started...")
            # Passing tokenised instance to the LSTM model for predictions
            unseen_sentiments = pretrained_lstm_model.predict(unseen_padded)
            logger.info("prediction end...")
            # print(unseen_sentiments)
            logger.info("prediction merging started...")
            sample_reviews['Predicted Sentiments'] = np.round(unseen_sentiments*10,1)

            df_prediction_sentiments = pd.DataFrame(sample_reviews['Predicted Sentiments'], columns = ['Predicted Sentiments'])
            df_movie                 = pd.DataFrame(sample_reviews['Movie'], columns = ['Movie'])
            df_review_text           = pd.DataFrame(sample_reviews['Review Text'], columns = ['Review Text'])
            df_imdb_rating           = pd.DataFrame(sample_reviews['IMDb Rating'], columns = ['IMDb Rating'])


            dfx=pd.concat([df_movie, df_review_text, df_imdb_rating, df_prediction_sentiments], axis=1)

            dfx.to_csv("data/processed/c2_IMDb_Unseen_Predictions.csv", sep=',', encoding='UTF-8') #data\processed
            logger.info("prediction merging end...")

        except Exception as ex:
            logger.error(str(ex))

    
    def full_annotate(self, 
                      unseen_reviews: list[str]
                      ) -> None:
        """
        """
        self.unseen_reviews = unseen_reviews

        try:
            report_struc: typing.Dict[str, typing.Any] = {}  # Final structure
            sentiment_line_struc: typing.Dict[str, typing.Any] = {}
            report_struc['sentiments'] = []
            
            logger.info("data preprocessing started...")
            _data_preprocessing = DataPreProcessing()
            X_train, X_test, y_train, y_test = _data_preprocessing.get_train_test_data()
            logger.info("data preprocessing end...")
            
            logger.info("model loading started...")
            pretrained_lstm_model = load_model(self.settings.MODEL_PATH)
            logger.info("model loading end...")

            unseen_processed = []
            for review in unseen_reviews:
                review = _data_preprocessing.preprocess_text(review)
                unseen_processed.append(review)

            _data_transformation = DataTransformation()
            word_tokenizer, X_train, unseen_padded, vocab_length = _data_transformation.get_tokenizer(X_train, unseen_processed, self.settings.MAXLEN)
            
            logger.info("prediction started...")
            # Passing tokenised instance to the LSTM model for predictions
            unseen_sentiments = pretrained_lstm_model.predict(unseen_padded)
            unseen_sentiments = unseen_sentiments.tolist()
            logger.info("prediction end...")

            for sentiment_list in unseen_sentiments:
                for sentiment in sentiment_list:
                    if(sentiment * 100 >= 50):
                        sentiment_line_struc['sentiment'] = 'positive'
                        sentiment_line_struc['score'] = sentiment
                        report_struc['sentiments'].append(sentiment_line_struc.copy())
                    else:
                        sentiment_line_struc['sentiment'] = 'negative'
                        sentiment_line_struc['score'] = sentiment
                        report_struc['sentiments'].append(sentiment_line_struc.copy())

            return report_struc

        except Exception as ex:
            logger.error(str(ex))
