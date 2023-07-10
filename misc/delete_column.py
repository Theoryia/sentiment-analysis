import pandas as pd

def delete_column(csv_file, column_name):
    df = pd.read_csv(csv_file)
    if column_name not in df.columns:
        print(f"Column '{column_name}' does not exist in the CSV file.")
        return
    df.drop(column_name, axis=1, inplace=True)
    
    df.to_csv('reviews.csv', index=False)
    print(f"Column '{column_name}' has been deleted. The updated CSV file has been saved as 'updated_file.csv'.")

csv_file_path = 'reviews.csv' 
column_to_delete = 'Sentiment'   

delete_column(csv_file_path, column_to_delete)
