import pandas as pd
import nltk
import os
import csv
import ssl

# Path for NLTK data files
os.environ['nltk_data'] = '/env/lib/nltk_data'

# Import NLTK 
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm import tqdm


# Let NLTK load without SSL Certification
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')



df = pd.read_csv('mentor_quality.csv', sep=";")
set1 = df['content']
comments = []

for i in set1:
    comments.append(i)

lexicon_file_path = 'vader_lexicon.txt'

sia = SentimentIntensityAnalyzer(lexicon_file=lexicon_file_path)


with open('test_nltk.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Score'])

    for i in comments:
        score = sia.polarity_scores(i)
        writer.writerow([score])
