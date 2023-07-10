import pandas as pd

# Read the CSV file
data_df = pd.read_csv('word_sentiments.csv')

# Drop the second column
data_df = data_df.drop(columns=data_df.columns[1])

# Save the modified data to a new CSV file
data_df.to_csv('word_sentiments.csv', index=False)

print("Column deletion completed successfully.")
