-- Write your query below


select name 
from 
customers c where not exists (select 1 from orders o where c.id = o.customer_id) 



-- select name 
-- from 
-- customers c
-- left join 
-- orders o
-- on c.id = o.customer_id
-- where o.customer_id is null
