-- Create Customers Table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR,
    age INT,
    signup_date DATE,
    region VARCHAR
);
 
-- Create Orders Table
CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    value FLOAT,  -- Total amount spent on the order
    status VARCHAR,
    CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
 
INSERT INTO customers (customer_id, name, age, signup_date, region) VALUES
(1, 'Alice Johnson', 45, '2022-01-15', 'North'),
(2, 'Bob Smith', 32, '2021-06-25', 'South'),
(3, 'Charlie Brown', 54, '2020-03-10', 'East'),
(4, 'David White', 60, '2019-09-30', 'West'),
(5, 'Eve Adams', 29, '2023-05-20', 'North'),
(6, 'Frank Miller', 70, '2018-11-12', 'South'),
(7, 'Grace Hall', 39, '2020-12-05', 'East'),
(8, 'Henry Carter', 65, '2019-07-22', 'West'),
(9, 'Ivy Roberts', 50, '2021-08-30', 'North'),
(10, 'Jack Lewis', 28, '2023-02-14', 'South')
;
 
DO $$
DECLARE
    i INT := 1;
    cust_id INT;
    order_amount NUMERIC;
    order_status TEXT;
    order_dt DATE;
BEGIN
    WHILE i <= 200 LOOP
        -- Generate random customer_id between 1 and 10
        cust_id := FLOOR(RANDOM() * 10 + 1);
        
        -- Generate random order amount between 20 and 500
        order_amount := FLOOR(RANDOM() * (500 - 20 + 1) + 20);
        
        -- Generate random order date within the last 2 years
        order_dt := CURRENT_DATE - INTERVAL '1 day' * FLOOR(RANDOM() * 730);
        
        -- Assign random order status (Completed, Pending, Cancelled)
        order_status := CASE
            WHEN RANDOM() < 0.7 THEN 'Completed'   -- 70% chance
            WHEN RANDOM() < 0.9 THEN 'Pending'     -- 20% chance
            ELSE 'Cancelled'                       -- 10% chance
        END;
 
        -- Insert the generated order into the orders table
        INSERT INTO orders (order_id, customer_id, order_date, value, status)
        VALUES (i, cust_id, order_dt, order_amount, order_status);
 
        -- Increment loop counter
        i := i + 1;
    END LOOP;
END $$;

-- Re-connect after creating the DB. this needs to be in a separate file or executed after the previous script
\c flatiron_db;
