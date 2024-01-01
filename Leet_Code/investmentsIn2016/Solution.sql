-- Write your PostgreSQL query statement below
with loc_count as (
    select 
        lat as lat_c, 
        lon as lon_c, 
        count(*) as loc_c
    from insurance
    group by lat, lon
), tiv_15_count as (
    select 
        tiv_2015 as tiv_15, 
        count(*) as tiv_15_c
    from insurance
    group by tiv_2015
)

select round(cast(sum(tiv_2016) as numeric), 2) as tiv_2016
from 
    (insurance i left join loc_count lc on i.lat = lc.lat_c and i.lon = lc.lon_c) as wloc
    left join tiv_15_count t15 on wloc.tiv_2015 = t15.tiv_15
where tiv_15_c > 1 and loc_c = 1
