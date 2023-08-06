import pandas as pd
from core.config import Settings
from Handlers import log_database_handler

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logdb = log_database_handler.LogDBHandler()
logger.addHandler(logdb)

# Please uncomment/comment below line if you wish to stop/start logging
#logger.disabled = True

class DataLoading:
    def __init__(self) -> None:
        self.settings = Settings()
        

    def load_raw_dataset(self):
        try:
            logger.info("data loading started...")
            df_raw_data = pd.read_csv(self.settings.RAW_DATA_PATH)
            logger.info("data loading end...")
            return df_raw_data
        
        except Exception as ex:
            logger.error(str(ex))
    
    def load_X_train_dataset(self):

        df_X_train_data = pd.read_csv(self.settings.X_TRAIN_DATA_PATH)
        
        return df_X_train_data
    
    def load_X_test_dataset(self):

        df_X_test_data = pd.read_csv(self.settings.X_TEST_DATA_PATH)
        
        return df_X_test_data
    
    def load_y_train_dataset(self):

        df_y_train_data = pd.read_csv(self.settings.Y_TRAIN_DATA_PATH)
        
        return df_y_train_data
    
    def load_y_test_dataset(self):

        df_y_test_data = pd.read_csv(self.settings.Y_TEST_DATA_PATH)
        
        return df_y_test_data
        
    