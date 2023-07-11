import pandas as pd

word_sentiments = pd.read_csv('word_sentiments.csv')

sentiment_mapping = {
    1: 'negative',
    2: 'unknown',
    3: 'positive'
}

reviews_df = pd.read_csv('reviews.csv')
reviews_df['Overall Sentiment'] = ""

for i, row in reviews_df.iterrows():
    review_text = row['text']
    sentiment_labels = []
    words = review_text.split()
    
    for word in words:
        word_sentiment_row = word_sentiments[word_sentiments['Word'] == word]
        if not word_sentiment_row.empty:
            sentiment_label = word_sentiment_row['Sentiment'].values[0]
            sentiment_labels.append(sentiment_label)
    
    if sentiment_labels:
        if any(label == 1 for label in sentiment_labels):
            overall_sentiment = 'negative'
        elif any(label == 3 for label in sentiment_labels):
            overall_sentiment = 'positive'
        else:
            overall_sentiment = 'unknown'
    else:
        overall_sentiment = 'error'
    
    reviews_df.at[i, 'Overall Sentiment'] = overall_sentiment

reviews_df.to_csv('reviews_with_overall_sentiment.csv', index=False)
