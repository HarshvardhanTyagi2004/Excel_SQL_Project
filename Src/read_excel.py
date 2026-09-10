import pandas as pd

file_path = "../Data/employees.xlsx"

df = pd.read_excel(file_path)

print("Original data:")
print(df)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nData types:")
print(df.dtypes)

# Remove duplicate rows
df = df.drop_duplicates()

# Check for missing values
df = df.dropna()

# Save cleaned data
df.to_excel("../Data/cleaned_employees.xlsx", index=False)

print("\nCleaned data saved successfully!")


import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Harsh@12345",
    database="employee_database"
)

print("MySQL connected successfully!")