import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

# Load the CSV files into Pandas DataFrames, skipping the first line (header)
correct_df = pd.read_csv('correct_reviews.csv', names=['Answer', 'Comparison'], skiprows=1)
algorithm_df = pd.read_csv('reviews.csv', names=['Answer', 'Comparison'], skiprows=1)

# Get unique classes from both correct and algorithm data
unique_classes = set(correct_df['Comparison'].tolist() + algorithm_df['Comparison'].tolist())

# Extract answers and comparison labels
correct_answers = correct_df['Comparison'].tolist()
algorithm_answers = algorithm_df['Comparison'].tolist()

# Calculate accuracy
accuracy = accuracy_score(correct_answers, algorithm_answers)
print(f'Accuracy: {accuracy:.2f}')

# Generate a classification report using unique classes
report = classification_report(correct_answers, algorithm_answers, labels=list(unique_classes))
print('Classification Report:')
print(report)
