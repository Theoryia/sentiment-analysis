import pandas as pd

# Read the modified reviews CSV file with the 'Sum' column
modified_reviews_df = pd.read_csv('modified_reviews_with_sum.csv')

# Read the original 'reviews.csv' file
reviews_df = pd.read_csv('reviews.csv')

# Create a new column 'Sentiment' based on the 'Sum' column values
reviews_df['Sentiment'] = modified_reviews_df['Sum'].apply(lambda x: 'Positive' if x > 0 else ('Not Understood / Neutral' if x == 0 else 'Negative'))

# Save the updated DataFrame to the 'reviews.csv' file
reviews_df.to_csv('reviews.csv', index=False)