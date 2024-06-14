-- Write your PostgreSQL query statement below
with p_ids as (
    select p_id 
    from tree
)

select id, 
    case 
        when p_id is null then 'Root'
        when id in (select p_id from p_ids) then 'Inner'
        else 'Leaf'
    end type
from tree
