-- 1. Show all employees
SELECT * FROM employees;

-- 2. Show employees from IT
SELECT * FROM employees
WHERE department = 'IT';

-- 3. Employees with salary above 70000
SELECT * FROM employees
WHERE salary > 70000;

-- 4. Highest salary
SELECT MAX(salary) AS highest_salary
FROM employees;

-- 5. Average salary
SELECT AVG(salary) AS average_salary
FROM employees;

-- 6. Employee count by department
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department;

-- 7. Employees sorted by salary
SELECT * FROM employees
ORDER BY salary DESC;

-- 8. Employees with 3+ years experience
SELECT * FROM employees
WHERE experience >= 3;

-- 9. Employees from Delhi
SELECT * FROM employees
WHERE city = 'Delhi';