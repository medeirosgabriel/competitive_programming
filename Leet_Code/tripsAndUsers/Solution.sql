with canc_counts as (
    select 
        t.request_at as date,
        sum(
            case 
                when t.status like 'cancelled%' then 1 
            else 0 
            end
        ) as canc_count
    from 
        trips t
        inner join users uc on uc.banned = 'No' and t.client_id = uc.users_id
        inner join users ud on ud.banned = 'No' and t.driver_id = ud.users_id
        where request_at between '2013-10-01' and '2013-10-03'
    group by t.request_at
)

select 
    cc.date as day,
    round(cast(cc.canc_count as decimal)/t.total, 2) as "Cancellation Rate"
from
    canc_counts cc
    inner join
    (
        select count(*) as total, t.request_at as date
        from 
            trips as t
            inner join users uc on uc.banned = 'No' and t.client_id = uc.users_id
            inner join users ud on ud.banned = 'No' and t.driver_id = ud.users_id
            where request_at between '2013-10-01' and '2013-10-03'
        group by t.request_at
    ) as t
    on cc.date = t.date 
