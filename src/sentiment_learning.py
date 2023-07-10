import pandas as pd

df = pd.read_csv('word_counts_sorted.csv')
df['Sentiment'] = ""

for i, row in df.iterrows():
    text = row['text']
    print(f"Review: {text}")
    sentiment = input("Enter sentiment (1 for negative, 2 for no meaning, 3 for positive): ")
    while sentiment not in ['1', '2', '3']:
        print("Invalid input. Please enter 1, 2, or 3.")
        sentiment = input("Enter sentiment (1 for negative, 2 for no meaning, 3 for positive): ")
    df.at[i, 'Sentiment'] = int(sentiment) #TODO modify

df.to_csv('wordlist.csv', index=False)