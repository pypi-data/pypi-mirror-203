from sklearn.model_selection import train_test_split

from core.config import Settings
from src.data.load_datasets import DataLoading
from Handlers import log_database_handler
import regex
import numpy as np
import pandas as pd

import nltk
from nltk.corpus import stopwords

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logdb = log_database_handler.LogDBHandler()
logger.addHandler(logdb)

# Please uncomment/comment below line if you wish to stop/start logging
logger.disabled = True

nltk.download('stopwords')

TAG_RE = regex.compile(r'<[^>]+>')

class DataPreProcessing:

    def __init__(self) -> None:
        self.settings = Settings()
    
    def remove_tags(self, text):
        '''Removes HTML tags: replaces anything between opening and closing <> with empty space'''

        return TAG_RE.sub('', text)

    def preprocess_text(self, sen):
        '''Cleans text data up, leaving only 2 or more char long non-stepwords composed of A-Z & a-z only
        in lowercase'''
        
        sentence = sen.lower()

        # Remove html tags
        sentence = self.remove_tags(sentence)

        # Remove punctuations and numbers
        sentence = regex.sub('[^a-zA-Z]', ' ', sentence)

        # Single character removal
        sentence = regex.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)  # When we remove apostrophe from the word "Mark's", the apostrophe is replaced by an empty space. Hence, we are left with single character "s" that we are removing here.

        # Remove multiple spaces
        sentence = regex.sub(r'\s+', ' ', sentence)  # Next, we remove all the single characters and replace it by a space which creates multiple spaces in our text. Finally, we remove the multiple spaces from our text as well.

        # Remove Stopwords
        pattern = regex.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
        sentence = pattern.sub('', sentence)

        return sentence 
    
    def get_train_test_data(self):

        _data_loading = DataLoading()
        df_raw_data = _data_loading.load_raw_dataset()

        # X = []
        # sentences = list(df_raw_data['review'])
        # for sen in sentences:
        #     X.append(self.preprocess_text(sen))

        X = df_raw_data['review'].apply(self.preprocess_text)
        y = df_raw_data['sentiment']

        y = np.array(list(map(lambda x: 1 if x=="positive" else 0, y)))

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

        # X_train.to_csv(self.settings.X_TRAIN_DATA_PATH, index=False, header=True)
        # X_test.to_csv(self.settings.X_TEST_DATA_PATH, index=False, header=True)
        # y_train.to_csv(self.settings.Y_TRAIN_DATA_PATH, index=False, header=True)
        # y_test.to_csv(self.settings.Y_TEST_DATA_PATH, index=False, header=True)

        return X_train, X_test, y_train, y_test
