import pandas as pd
import re

# Read the reviews and the words with sentiments CSV files
reviews_df = pd.read_csv('reviews.csv')
sentiments_df = pd.read_csv('word_sentiments.csv')

# Create a new DataFrame to store the modified reviews
modified_reviews_df = pd.DataFrame(columns=['Modified Review'])

# Iterate over each review
for _, row in reviews_df.iterrows():
    review_text = row['text']
    modified_review_text = review_text
    
    # Iterate over each word in the review
    for word in review_text.split():
        # Find the sentiment for the word in the word sentiments CSV file
        sentiment = sentiments_df.loc[sentiments_df['Word'] == word, 'Sentiment'].values
        
        # Replace the word with the corresponding sentiment number or 0 if not found
        modified_review_text = re.sub(r"\b" + re.escape(word) + r"(?!\w)", str(sentiment[0]) if len(sentiment) > 0 else '0', modified_review_text)
    
    # Add the modified review to the DataFrame
    modified_reviews_df = modified_reviews_df.append({'Modified Review': modified_review_text}, ignore_index=True)

# Save the modified reviews to a new CSV file
modified_reviews_df.to_csv('modified_reviews.csv', index=False)

