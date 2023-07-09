import pandas as pd
from collections import Counter
import string

# Step 1: Preprocessing
reviews = pd.read_csv('reviews.csv')  # Load the dataset
text_data = reviews['text'].astype(str).tolist()

# Count the words
word_counts = Counter()

# Remove punctuation and convert to lowercase
translator = str.maketrans('', '', string.punctuation)
for text in text_data:
    text = text.translate(translator).lower()
    word_counts.update(text.split())

# Create a DataFrame with the word counts
word_count_df = pd.DataFrame(word_counts.items(), columns=['Word', 'Count'])

# Save the word counts to a CSV file
word_count_df.to_csv('word_counts.csv', index=False)