-- Write your PostgreSQL query statement below
with aux as (
    select sales_id 
    from company c right join orders o on o.com_id = c.com_id
    where c.name = 'RED'
)

select s.name
from salesperson s
where s.sales_id not in (select * from aux)
