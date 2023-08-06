# sentimentdl_glove_imdb_en
In this introductory sample, we'll try to predict a sentiment (positive or negative) for customer reviews. In the world of machine learning, this type of prediction is known as binary classification.

# Sentiment Classification - of IMDb User Reviews - using LSTM
An end-to-end toolkit on building a movie review sentiment classification LSTM model in Keras Deep Learning with model h5 file. Model is trained on IMDb Movie reviews [source](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews).

As part of model training, we have trained LSTM nodels, with reasoning as to why LSTMs are well suited to handle (sequential) text data.

## Features List
1.   Modular project structure
2.   Python package setup configured, package available on [pypi](https://pypi.org/)
3.   Connecting to MS SQL Databse by [pyodbc](https://mkleehammer.github.io/pyodbc/), you can install latest MS SQL driver for python from [here](https://learn.microsoft.com/en-us/sql/connect/python/pyodbc/python-sql-driver-pyodbc?view=sql-server-ver16)
4.   Logging and Exception handling to MS SQL by [Calling Stored Procedures](https://github.com/mkleehammer/pyodbc/wiki/Calling-Stored-Procedures)


## MS SQL
You can find create table and stored Procedure scripts under "references" folder

## Download Datasets
You can download required datasets from [here](https://drive.google.com/drive/folders/1TK9k41RT8Nf3IhzerNWHpEqWztsk2gAP) and keep it in "data/raw" folder

## Plan of Action
1.   Load **IMDb Movie Reviews dataset (50,000 reviews)**
2.   **Pre-process dataset** by removing special characters, numbers, etc. from user reviews + convert **sentiment labels** positive & negative to numbers 1 & 0, respectively
3.   **Import GloVe Word Embedding** to build Embedding Dictionary + Use this to build Embedding Matrix for our Corpus
4. Model Training using **Deep Learning in Keras** for: **LSTM Models** and analyse model performance and results
4. Last, perform **predictions on real IMDb movie reviews**

## Steps to run on Windows

* Prerequisites: [Python 3.9](https://www.python.org/downloads/) (ensure Python is added to [PATH](https://medium.com/co-learning-lounge/how-to-download-install-python-on-windows-2021-44a707994013)) + [Git](https://www.markdownguide.org/basic-syntax/) Client 
* Open GIT CMD >> navigate to working directory >> Clone this Github Repo (or download project files from GitHub directly)

      git clone https://github.com/MusaddiqueHussainLabs/sentimentdl_glove_imdb_en.git  
* Open Windows Powershell >> navigate to new working directory (cloned repo folder)
* Run Project


  * Using Conda Environment:

        conda env create -f conda_env_win.yml   # create conda environment called 'app_env'
        conda env list                          # check if app_env is created
        conda activate app_env                  # activate app_env
        python main.py                           # run the project
        conda deactivate                        # close conda environment once done

  * Using PIP + Virtualenv:
 
        pip install virtualenv                  # install virtual environment        
        virtualenv ENV                          # create virtual environment by the name ENV
        .\ENV\Scripts\activate                  # activate ENV
        pip install -r .\pip_requirements.txt       # install project dependencies
        python main.py                           # run the project
        deactivate                              # close virtual environment once done

### Bug / Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/MusaddiqueHussainLabs/sentimentdl_glove_imdb_en/issues) by including your search query and the expected result.

## References / Thanks

Big thanks to below authors:

- [Krish Naik](https://www.youtube.com/watch?v=1m3CPP-93RI)
- [Data Science Garage](https://www.youtube.com/watch?v=lVvjy5P26cw)
- [codebasics](https://www.youtube.com/@codebasics)
- [SKILLCATE](https://www.youtube.com/@skillcate)