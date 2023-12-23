-- Write your PostgreSQL query statement below
select d.dName as Department, e.eName as Employee, e.salary as Salary
from 
    ((select name as eName, salary, departmentId from Employee) e 
    inner join 
    (select id, name as dName from Department) d on e.departmentId = d.id)
where (d.dName, e.salary) in 
    (
        select d.dName, max(e.salary)
        from
            (select name as eName, salary, departmentId from Employee) e 
            inner join 
            (select id, name as dName from Department) d on e.departmentId = d.id
            group by d.dName
    )
