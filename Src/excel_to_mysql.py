import pandas as pd
import mysql.connector

# Read cleaned Excel file
df = pd.read_excel("../Data/cleaned_employees.xlsx")

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Harsh@12345",
    database="employee_database"
)

cursor = connection.cursor()

# Insert data
query = """
INSERT INTO employees
(employee_id, name, age, gender, department, job_role, salary, city, experience, performance_rating)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

for _, row in df.iterrows():
    values = (
        row["employee_id"],
        row["name"],
        row["age"],
        row["gender"],
        row["department"],
        row["job_role"],
        row["salary"],
        row["city"],
        row["experience"],
        row["performance_rating"]
    )

    cursor.execute(query, values)

connection.commit()

print("Data inserted successfully!")

cursor.close()
connection.close()