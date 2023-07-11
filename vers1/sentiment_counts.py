import pandas as pd

word_sentiments = pd.read_csv('word_sentiments.csv')

sentiment_mapping = {
    1: 'negative',
    2: 'unknown',
    3: 'positive'
}

reviews_df = pd.read_csv('reviews.csv')
reviews_df['Overall Sentiment'] = ""
reviews_df['Sentiment Counts'] = ""
reviews_df['Accuracy'] = ""

for i, row in reviews_df.iterrows():
    review_text = row['text']
    sentiment_counts = {
        'negative': 0,
        'positive': 0
    }
    words = review_text.split()

    for word in words:
        word_sentiment_row = word_sentiments[word_sentiments['Word'] == word]
        if not word_sentiment_row.empty:
            sentiment_label = word_sentiment_row['Sentiment'].values[0]
            sentiment = sentiment_mapping[sentiment_label]
            if sentiment in sentiment_counts:
                sentiment_counts[sentiment] += 1

    overall_sentiment = max(sentiment_counts, key=sentiment_counts.get)
    reviews_df.at[i, 'Overall Sentiment'] = overall_sentiment
    reviews_df.at[i, 'Sentiment Counts'] = sentiment_counts

    total_words = sum(sentiment_counts.values())
    if total_words > 0:
        accuracy = (sentiment_counts[overall_sentiment] / total_words) * 100
    else:
        accuracy = 0

    reviews_df.at[i, 'Accuracy'] = accuracy

reviews_df.to_csv('reviews_with_sentiment_counts_and_accuracy.csv', index=False)
