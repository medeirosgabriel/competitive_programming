-- Write your PostgreSQL query statement below
/*
select 
    round(
        sum(
            case when 
                second_login_date is not null and first_login_date + 1 = second_login_date then 1
                else 0 
            end
        )::numeric / count(distinct player_id), 
        2
    ) as fraction
from (
    select 
        player_id,
        min(event_date) as first_login_date,
        lead(event_date, 1) over (partition by player_id order by event_date) as second_login_date
    from activity
    group by player_id, event_date
)
*/

/*
select 
    round(
        count(logins.player_id)::numeric / count(players.player_id)
    , 2) as fraction 
from
    (
        select distinct player_id
        from
            (
                select 
                    player_id,
                    min(event_date) as first_login_date,
                    lead(event_date, 1) over (partition by player_id order by event_date) as second_login_date
                from activity
                group by player_id, event_date
            )
        where first_login_date + 1 = second_login_date
    ) as logins,
    (
        select distinct player_id
        from activity
    ) as players
*/

/*
select 
    round(
        count(distinct player_id) / (select count(distinct player_id) from activity),
        2  
    ) as fraction
from activity
where 
    (player_id, event_date - INTERVAL '1 DAY') in 
    (
        select player_id, min(event_date)
        from activity
        group by player_id
    )
*/

select round(
    count(a1.player_id) * 1.0 / (select count(distinct player_id) from activity),
    2  
) as fraction
from 
    activity a1 
    inner join 
    (
        select player_id, min(event_date) as event_date
        from activity
        group by player_id
    ) a2 
    on a1.player_id = a2.player_id and a1.event_date = a2.event_date + (interval '1 DAY')
