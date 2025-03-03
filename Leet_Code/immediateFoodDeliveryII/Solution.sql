-- Write your PostgreSQL query statement below
with first_del as (
    select customer_id as c_id, min(order_date) as or_date
    from delivery
    group by customer_id
),
imm as (
    select count(*) as imm_cnt
    from first_del, delivery
    where c_id = customer_id and or_date = order_date and order_date = customer_pref_delivery_date
),
sch as (
    select count(*) as sch_cnt
    from first_del, delivery
    where c_id = customer_id and or_date = order_date and order_date <> customer_pref_delivery_date
)

select round((imm_cnt/cast((imm_cnt + sch_cnt) as float) * 100)::numeric, 2) as immediate_percentage
from imm, sch
