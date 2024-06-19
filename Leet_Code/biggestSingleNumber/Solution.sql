-- Write your PostgreSQL query statement below
with aux as (
    select num
    from mynumbers
    group by num
    having count(*) = 1
)

select max(num) as num
from aux
