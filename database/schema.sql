CREATE DATABASE IF NOT EXISTS employee_database;

USE employee_database;

CREATE TABLE IF NOT EXISTS employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    department VARCHAR(50),
    job_role VARCHAR(50),
    salary INT,
    city VARCHAR(50),
    experience INT,
    performance_rating INT
);