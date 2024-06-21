-- Write your PostgreSQL query statement below
select x, y, z, 
    CASE 
        WHEN x < y + z and y < x + z and z < x + y then 'Yes'
        ELSE 'No'
    END as triangle
from triangle
