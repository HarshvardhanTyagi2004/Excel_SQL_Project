from fastapi import FastAPI
import mysql.connector
from pydantic import BaseModel

import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


@app.get("/")
def home():
    return {"message": "Employee API is working!"}


@app.get("/employees")
def get_employees():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    cursor.close()
    connection.close()

    return employees

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM employees WHERE employee_id = %s"
    cursor.execute(query, (employee_id,))

    employee = cursor.fetchone()

    cursor.close()
    connection.close()

    return employee

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM employees WHERE employee_id = %s"
    cursor.execute(query, (employee_id,))

    employee = cursor.fetchone()

    cursor.close()
    connection.close()

    return employee


@app.get("/employees/department/{department}")
def get_employees_by_department(department: str):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM employees WHERE department = %s"
    cursor.execute(query, (department,))

    employees = cursor.fetchall()

    cursor.close()
    connection.close()

    return employees



class Employee(BaseModel):
    employee_id: int
    name: str
    age: int
    gender: str
    department: str
    job_role: str
    salary: int
    city: str
    experience: int
    performance_rating: int


@app.post("/employees")
def create_employee(employee: Employee):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO employees
    (employee_id, name, age, gender, department, job_role, salary, city, experience, performance_rating)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        employee.employee_id,
        employee.name,
        employee.age,
        employee.gender,
        employee.department,
        employee.job_role,
        employee.salary,
        employee.city,
        employee.experience,
        employee.performance_rating
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return {"message": "Employee created successfully"}


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    query = "DELETE FROM employees WHERE employee_id = %s"
    cursor.execute(query, (employee_id,))

    connection.commit()

    cursor.close()
    connection.close()

    return {"message": "Employee deleted successfully"}


@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: Employee):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    UPDATE employees
    SET name = %s,
        age = %s,
        gender = %s,
        department = %s,
        job_role = %s,
        salary = %s,
        city = %s,
        experience = %s,
        performance_rating = %s
    WHERE employee_id = %s
    """

    values = (
        employee.name,
        employee.age,
        employee.gender,
        employee.department,
        employee.job_role,
        employee.salary,
        employee.city,
        employee.experience,
        employee.performance_rating,
        employee_id
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return {"message": "Employee updated successfully"}