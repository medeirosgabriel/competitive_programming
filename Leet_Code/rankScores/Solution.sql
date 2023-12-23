-- Write your PostgreSQL query statement below
select s.score, dense_rank() OVER (ORDER BY s.score desc) as rank
from Scores s
