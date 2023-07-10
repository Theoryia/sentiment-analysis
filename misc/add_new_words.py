import pandas as pd

existing_df = pd.read_csv('word_sentiments.csv')
new_words_df = pd.read_csv('new_words.csv', header=None, names=['Word', 'Sentiment'])
new_words_df = new_words_df.drop_duplicates(subset=['Word'])
duplicates = new_words_df[new_words_df['Word'].isin(existing_df['Word'])]
merged_df = pd.concat([existing_df, new_words_df], ignore_index=True)
merged_df.drop_duplicates(subset=['Word'], keep='last', inplace=True)
merged_df.to_csv('word_sentiments.csv', index=False)

if len(new_words_df) > 0:
    added_words = new_words_df[~new_words_df['Word'].isin(duplicates['Word'])]['Word'].values
    if len(added_words) > 0:
        print(f"Added {len(added_words)} new word(s):")
        print(added_words)
    else:
        print("No new words to add.")
else:
    print("No new words to add.")

if len(duplicates) > 0:
    print("Duplicate word(s) found:")
    print(duplicates['Word'].values)

print("Word addition completed successfully.")
