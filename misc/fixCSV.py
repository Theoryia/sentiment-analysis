import pandas as pd

data_df = pd.read_csv('word_sentiments.csv')
data_df = data_df[['Word', 'Sentiment']]
data_df = data_df.fillna('0')
data_df['Sentiment'] = data_df['Sentiment'].str.replace('[^n\-1/10]', '')
data_df.to_csv('output.csv', index=False, header=['Word', 'Sentiment'])
print("Conversion completed successfully.")