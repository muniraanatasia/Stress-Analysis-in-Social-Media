# Import necessary libraries
import pandas as pd

# Set file paths (make sure these CSVs are in the same folder as this Python file)
train_path = 'dreaddit-train.csv'
test_path = 'dreaddit-test.csv'

# Load the CSV files
try:
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)

    # Print confirmation and preview of data
    print("✅ Training data loaded successfully!")
    print(train_df.head())  # Show first 5 rows

    print("\n✅ Test data loaded successfully!")
    print(test_df.head())  # Show first 5 rows

except FileNotFoundError:
    print("❌ Error: One or both CSV files not found. Make sure they're in the same folder as this script.")