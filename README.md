# Excel SQL Employee Data Management System

A backend data management project that processes employee data from Excel, cleans it using Pandas, stores it in MySQL, and provides REST APIs using FastAPI.

## Technologies Used

- Python
- Pandas
- Excel
- MySQL
- SQL
- FastAPI
- Uvicorn
- Python-dotenv

## Project Flow

Excel File
    ↓
Pandas Data Cleaning
    ↓
MySQL Database
    ↓
FastAPI REST API
    ↓
JSON Response

## Features

- Read employee data from Excel
- Detect missing values
- Detect duplicate records
- Clean employee data using Pandas
- Store data in MySQL
- Perform SQL queries
- REST API for employee management
- Create employees
- Read employees
- Update employees
- Delete employees
- Search employees by department
- Swagger API documentation

## API Endpoints

### GET
`GET /`

Check whether the API is running.

### GET
`GET /employees`

Get all employees.

### GET
`GET /employees/{employee_id}`

Get a specific employee.

### GET
`GET /employees/department/{department}`

Get employees from a specific department.

### POST
`POST /employees`

Create a new employee.

### PUT
`PUT /employees/{employee_id}`

Update an existing employee.

### DELETE
`DELETE /employees/{employee_id}`

Delete an employee.

## Database

Database name:

`employee_database`

Main table:

`employees`

## How to Run

Install dependencies:

```bash
pip install -r requirements.tx