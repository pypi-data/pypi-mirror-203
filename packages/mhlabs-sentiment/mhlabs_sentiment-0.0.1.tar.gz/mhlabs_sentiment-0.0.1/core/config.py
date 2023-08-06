from dataclasses import dataclass
import os

@dataclass
class Settings:

    RAW_DATA_PATH : str=os.path.join('data\\raw',"a1_IMDB_Dataset.csv") #data\raw

    #uncomment below if you wish store spilted data
    # X_TRAIN_DATA_PATH : str=os.path.join('data\\interim',"a1_IMDB_Dataset.csv") #data\interim
    # X_TEST_DATA_PATH : str=os.path.join('data\\interim',"a1_IMDB_Dataset.csv") #data\interim
    # Y_TRAIN_DATA_PATH : str=os.path.join('data\\interim',"a1_IMDB_Dataset.csv") #data\interim
    # Y_TEST_DATA_PATH : str=os.path.join('data\\interim',"a1_IMDB_Dataset.csv") #data\interim

    GLOVE_6B_100D : str=os.path.join('data\\raw',"a2_glove.6B.100d.txt") #data\raw
    MODEL_PATH : str=os.path.join('models',"sentimentdl_glove_imdb_en.h5") #models\sentimentdl_glove_imdb_en.h5
    UNSEEN_REVIEWS_DATA_PATH : str=os.path.join('data\\raw',"a3_IMDb_Unseen_Reviews.csv") #data\raw\a3_IMDb_Unseen_Reviews.csv
    
    MAXLEN = 100

    #Database Connection strings
    CONNECTION_STRINGS = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost;DATABASE=MusaddiqueHussainLabs;Trusted_Connection=yes;TrustServerCertificate=yes'

settings = Settings()