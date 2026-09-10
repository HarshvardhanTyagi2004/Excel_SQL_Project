import pandas as pd

data = {
    "employee_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],

    "name": [
        "Rahul", "Aman", "Priya", "Neha", "Arjun",
        "Simran", "Karan", "Anjali", "Rohit", "Pooja"
    ],

    "age": [24, 27, 25, 29, 26, 30, 23, 28, 31, 25],

    "gender": [
        "Male", "Male", "Female", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female"
    ],

    "department": [
        "IT", "HR", "IT", "Finance", "IT",
        "HR", "Sales", "IT", "Finance", "Sales"
    ],

    "job_role": [
        "Python Developer",
        "HR Executive",
        "Backend Developer",
        "Accountant",
        "Software Engineer",
        "HR Manager",
        "Sales Executive",
        "Python Developer",
        "Financial Analyst",
        "Sales Manager"
    ],

    "salary": [
        65000, 45000, 75000, 55000, 70000,
        80000, 50000, 72000, 85000, 68000
    ],

    "city": [
        "Chandigarh", "Delhi", "Mohali", "Ludhiana", "Delhi",
        "Chandigarh", "Amritsar", "Mohali", "Delhi", "Ludhiana"
    ],

    "experience": [1, 3, 2, 5, 2, 6, 1, 3, 7, 4],

    "performance_rating": [4, 3, 5, 4, 5, 4, 3, 5, 5, 4]
}

df = pd.DataFrame(data)

df.to_excel("employees.xlsx", index=False)

print("Excel file created successfully!")
print(df)