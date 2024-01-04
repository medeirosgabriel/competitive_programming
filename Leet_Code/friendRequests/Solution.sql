-- Write your PostgreSQL query statement below
with accepters as (
    select accepter_id, count(*) as a_count
    from RequestAccepted r
    group by accepter_id
), requesters as (
    select requester_id, count(*) as r_count
    from RequestAccepted r
    group by requester_id
)

select 
    case 
        when j.accepter_id is null then j.requester_id
        else j.accepter_id
    end id,
    a_count + r_count as num
from 
    (
        select accepter_id, requester_id,
        case 
            when r.r_count is null then 0
            else r.r_count
        end r_count,
        case 
            when a.a_count is null then 0
            else a.a_count
        end a_count
        from accepters a full outer join requesters r on a.accepter_id = r.requester_id
    ) as j 
order by (a_count + r_count) desc
limit 1

