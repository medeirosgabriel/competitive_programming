-- Write your PostgreSQL query statement below
WITH RankedSalaries AS (
    SELECT
        d.name as Department,
        e.name as Employee,
        e.salary as Salary,
        DENSE_RANK() OVER(PARTITION BY d.name ORDER BY e.salary DESC) AS SalaryRank
    FROM Employee e INNER JOIN Department d on e.departmentId = d.id
)

SELECT
    Department,
    Employee,
    Salary
FROM RankedSalaries
WHERE SalaryRank <= 3;
