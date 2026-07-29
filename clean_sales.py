import os
import pandas as pd

# Full absolute path to your raw data file
raw_file_path = r"D:\CODING FOLDERS\Sales Dashboard Project\data_raw\sales_data.csv"

# Full absolute path to your processed data folder
processed_folder = r"D:\CODING FOLDERS\Sales Dashboard Project\data_processed"
processed_file_path = os.path.join(processed_folder, "cleaned_sales.csv")

# Ensure the output folder exists
os.makedirs(processed_folder, exist_ok=True)

# Load the dataset
df = pd.read_csv(raw_file_path, encoding='latin-1')

# Quick checks
print("Shape before cleaning:", df.shape)
print(df.head())

# Handle missing values
print("Missing values:\n", df.isnull().sum())
df.dropna(inplace=True)

# Fix date column
df['Sale_Date'] = pd.to_datetime(df['Sale_Date'], errors='coerce')

# Extract useful time columns
df['Year'] = df['Sale_Date'].dt.year
df['Month'] = df['Sale_Date'].dt.month
df['Month_Name'] = df['Sale_Date'].dt.month_name()

# Add calculated fields
df['Revenue'] = df['Quantity_Sold'] * df['Unit_Price']
df['Profit'] = df['Revenue'] - (df['Quantity_Sold'] * df['Unit_Cost'])

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save the cleaned file
df.to_csv(processed_file_path, index=False)

print("✅ Cleaning done! Shape after cleaning:", df.shape)
print(f"Cleaned file saved to: {processed_file_path}")









