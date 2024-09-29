-- Write your PostgreSQL query statement below
select user_id as buyer_id, join_date, count(buyer_id) as orders_in_2019
from users u left join 
    (
        select *
        from orders o
        where o.order_date >= '2019-01-01' 
    ) o on u.user_id = o.buyer_id
group by user_id, join_date
