import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from KaggleWorld2VecUtility import KaggleWorld2VecUtility
import pandas as pd
import  nltk


if __name__ == '__main__':
    # Read the data
    train = pd.read_csv(os.path.join(os.path.dirname(__file__),'data',
    'labelledTrainData.tsv'),header=0,\
            delimiter="\t",quoting=3)
    
