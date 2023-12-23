SELECT CASE
    WHEN COUNT(*) = 0 THEN NULL
    ELSE (
        SELECT DISTINCT e.salary
        FROM employee e
        ORDER BY salary DESC
        LIMIT 1,1
    )
    END AS SecondHighestSalary;
