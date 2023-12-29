SELECT c.customer_id
FROM customer c
INNER JOIN product p
ON c.product_key = p.product_key
WHERE c.product_key IN
    (SELECT DISTINCT product.product_key
    FROM product)
GROUP BY c.customer_id;