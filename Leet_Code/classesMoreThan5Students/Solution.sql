-- Write your PostgreSQL query statement below
select class
from courses c
group by class
having count(*) >= 5
