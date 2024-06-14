-- Write your PostgreSQL query statement below
with aux as (
    select *, id - row_number() over (partition by people >= 100 order by id) n
    from stadium
)

select id, visit_date, people
from aux inner join (
    select count(*) cnt, n 
    from aux
    group by people >= 100, n
) t ON aux.n = t.n
WHERE (t.cnt > 2 AND people >= 100)
ORDER BY id
