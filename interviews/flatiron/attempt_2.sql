select * from public.customers;

select * from public.orders;

with expend_more_than_5000 AS (
	select o.customer_id, SUM(o.value) as total_expend
	from orders o
	where o.status = 'Completed'
	group by o.customer_id
),
customers_over_50_years AS (
	select c.customer_id, c.name, c.age
	from customers c
	where c.age > 50
)

select cy.customer_id, cy.name, cy.age, e5000.total_expend
from customers_over_50_years cy
join expend_more_than_5000 e5000 on cy.customer_id = e5000.customer_id
where cy.age > 50
and e5000.total_expend > 3000