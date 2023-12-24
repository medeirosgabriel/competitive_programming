-- Write your PostgreSQL query statement below
select w1.id
from 
    weather w1 inner join
    (
        select id as id2, recordDate + 1 as rd2, temperature as t2
        from weather
    ) w2 on w1.recordDate = w2.rd2
where w1.temperature > w2.t2
