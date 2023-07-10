import pandas as pd

data_df = pd.read_csv('word_sentiments.csv')
mapping = {3: 1, 2: 0, 1: -1}
data_df['Sentiment'] = data_df['Sentiment'].map(mapping)
data_df.to_csv('word_sentiments.csv', index=False)