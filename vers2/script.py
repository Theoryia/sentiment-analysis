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
    
    # Remove all full stops and commas, excluding CSV punctuation
    modified_review_text = re.sub(r'(?<!\.)\.(?!\.)|(?<!,),(?!,)', '', modified_review_text)

    # Iterate over each word in the modified review
    for word in modified_review_text.split():
        # Find the sentiment for the word in the word sentiments CSV file
        sentiment = sentiments_df.loc[sentiments_df['Word'] == word, 'Sentiment'].values
        
        # Replace the word with the corresponding sentiment number or 0 if not found
        modified_review_text = re.sub(r"\b" + re.escape(word) + r"(?!\w)", str(sentiment[0]) if len(sentiment) > 0 else '0', modified_review_text)
    
    # Add the modified review to the DataFrame
    modified_reviews_df = modified_reviews_df.append({'Modified Review': modified_review_text}, ignore_index=True)

# Iterate over each cell in the 'Modified Review' column
for i, cell in enumerate(modified_reviews_df['Modified Review']):
    # Split the cell into individual values
    values = cell.split()
    
    # Check if the cell contains 'n' followed by 1 or -1
    if 'n 1' in cell:
        # Replace 'n 1' with '-1' in the cell
        modified_reviews_df.at[i, 'Modified Review'] = cell.replace('n 1', '-1')
    elif 'n -1' in cell:
        # Replace 'n -1' with '1' in the cell
        modified_reviews_df.at[i, 'Modified Review'] = cell.replace('n -1', '0')
    elif 'n 0' in cell:
        # Replace 'n -1' with '1' in the cell
        modified_reviews_df.at[i, 'Modified Review'] = cell.replace('n 0', '-1')

# Calculate the sum of each row
modified_reviews_df['Sum'] = modified_reviews_df['Modified Review'].str.split().apply(lambda row: sum(int(val) if val.isdigit() or val == '-1' else 0 for val in row))

original_reviews_df = pd.read_csv('reviews.csv')
original_reviews_df['text'] = original_reviews_df['text'] + ' ' + modified_reviews_df['Sum'].astype(str)

# Save the DataFrame to a new CSV file
modified_reviews_df.to_csv('modified_reviews_with_sum.csv', index=False)

# Create a new column 'Sentiment' based on the 'Sum' column values
reviews_df['Sentiment'] = modified_reviews_df['Sum'].apply(lambda x: 'Positive' if x > 0 else ('Not Understood / Neutral' if x == 0 else 'Negative'))

# Save the updated DataFrame to the 'reviews.csv' file
reviews_df.to_csv('reviews.csv', index=False)
