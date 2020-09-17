EXERCISE 1

-- UPDATE students SET name='Lea' WHERE name='lea' 
-- UPDATE students SET birth_date='1998-11-02' WHERE last_name = 'Dupont'
-- DELETE FROM students WHERE name='Lea' AND last_name='Dupont'
-- SELECT count(name) FROM students
-- SELECT count(*) FROM students WHERE(birth_date)> '01/01/2000'
-- ALTER TABLE students ADD COLUMN math_grade int;
-- UPDATE students SET math_grade='80' WHERE id = '1'
-- UPDATE students SET math_grade='90' WHERE id=  '2' OR id='4'
-- UPDATE students SET math_grade= '100' WHERE id ='6'
-- SELECT count(*) FROM students WHERE math_grade> 83
-- INSERT INTO students (name, last_name, birth_date, math_grade)
-- VALUES ('Omer', 'Simpson', '1980-03-10','70')
-- -- SELECT count(math_grade) FROM students GROUP BY name, last_name
-- SELECT sum(math_grade) FROM students

EXERCISE 2

-- SELECT * FROM items ORDER BY price DESC
-- SELECT * FROM items WHERE price > '80' ORDER BY price ASC 
-- SELECT first_n, last_n FROM customers ORDER BY first_n ASC limit 3
-- SELECT first_n, last_n FROM customers ORDER BY first_n ASC OFFSET 3
-- SELECT last_n FROM customers ORDER BY last_n DESC

CREATE TABLE purchases(
    id SERIAL PRIMARY KEY,	
	customer_id INT,	
 	item_id INT,
	FOREIGN KEY(customer_id) REFERENCES customers(cust_id),
 	FOREIGN KEY(item_id) REFERENCES items(items_id)
  )

INSERT INTO purchases (customer_id, item_id)
VALUES (1,1),(2,2),(3,3),(5,1),(4,2)

SELECT customers.first_n, last_n, product FROM purchases
JOIN customers ON purchases.customer_id = customers.cust_id
JOIN items ON purchases.item_id = items.items_id

WHERE purchases.customer_id='4' 

INSERT INTO items (product, price)
VALUES ('hard drive', '320')

INSERT INTO purchases (customer_id, item_id)
VALUES((SELECT cust_id FROM customers WHERE first_n = 'Scott'), (SELECT items_id FROM items WHERE product = 'hard drive'))

begin;
alter table purchases
drop constraint purchases_customer_id_fkey;
alter table purchases
add constraint purchases_customer_id_fkey
foreign key (customer_id)
references customers (cust_id)
on delete cascade;
commit;

DELETE FROM customers WHERE first_n ='Scott'



SELECT first_n, last_n, product FROM purchases
LEFT JOIN customers ON purchases.customer_id = customers.cust_id
LEFT JOIN items ON purchases.item_id = items.items_id