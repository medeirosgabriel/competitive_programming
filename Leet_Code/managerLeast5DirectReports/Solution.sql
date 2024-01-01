-- Write your PostgreSQL query statement below
with count as (
    select e.managerId as mid, count(*) as count
    from employee e 
    group by e.managerId
)

select e.name
from count c right join employee e on c.mid = e.id
where c.count >= 5
