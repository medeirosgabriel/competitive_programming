-- Write your PostgreSQL query statement below
with cte as (
    select product_id, min(year) as year
    from sales s 
    group by product_id
)

select s.product_id, s.year as first_year, s.quantity, s.price 
from sales s inner join cte on cte.product_id = s.product_id and s.year = cte.year
