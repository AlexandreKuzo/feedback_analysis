import os
import openai
import csv
import time
import pandas as pd


from os.path import join, dirname
from dotenv import load_dotenv

# Init environment
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

openai.api_key = os.environ.get('OPEN_API_KEY')

# Load and Read the csv file
df = pd.read_csv('mentor_quality.csv', sep=";")
# Identify the column we want to calculate scores on
set1 = df['content']

feedbacks = []
for i in set1:
    feedbacks.append(i)

for i in feedbacks: 
    # OpenAI implementation
    prompt =  f"Please give a sentiment score for this text: '{i}'. The score should be between -1 and 1, where -1 is very negative, 0 is neutral, and 1 is very positive."
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        temperature = 0, 
        max_tokens = 1024,
        n=1,
        stop=None,
        timeout=10,
    )

    sentiment = float(response.choices[0].text)
    
    # Write scores in a new CSV file
    with open('results.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([sentiment])
    time.sleep(0.5)