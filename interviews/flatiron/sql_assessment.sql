WITH total_amout AS (SELECT o.customer_id, SUM(o.value) as total
                     FROM orders o
					 WHERE o.status = 'Completed'
                     GROUP BY o.customer_id
					 HAVING total > 5000
)

  
SELECT c.name, c.age,
  FROM customers as c
 JOIN total_amount on c.customer_id = total_amount.customer_id
 WHERE c.age > 50

--- Question 2. What's the ratio between the number of customers having 50y+ and the customers not having 50y+?
Postgres v16
