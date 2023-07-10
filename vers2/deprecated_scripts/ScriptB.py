import pandas as pd

# Read the modified reviews CSV file
modified_reviews_df = pd.read_csv('modified_reviews.csv')

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

# Calculate the sum of each row
modified_reviews_df['Sum'] = modified_reviews_df['Modified Review'].str.split().apply(lambda row: sum(int(val) if val.isdigit() or val == '-1' else 0 for val in row))

# Save the DataFrame to a new CSV file
modified_reviews_df.to_csv('modified_reviews_with_sum.csv', index=False)
