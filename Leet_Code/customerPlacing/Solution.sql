-- Write your PostgreSQL query statement below
select customer_number
from orders as o
group by o.customer_number
order by count(*) desc
limit 1
