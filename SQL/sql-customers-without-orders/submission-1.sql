-- Write your query below
SELECT name FROM customers where id not in (select customer_id from orders);