-- SELECT * FROM customer
-- SELECT first_name, last_name AS full_name FROM customer
-- SELECT DISTINCT create_date FROM customer
-- SELECT * FROM customer ORDER BY first_name DESC
-- SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC
-- SELECT address, district, phone FROM address WHERE district= 'Texas'
-- SELECT * FROM film WHERE film_id ='15' or film_id ='150'
-- SELECT film_id, title, description, length, rental_rate FROM film WHERE title = 'Dragon Squad'
-- SELECT film_id, title, description, length, rental_rate FROM film WHERE title ILIKE 'dr%'  
-- SELECT * FROM film ORDER BY rental_rate ASC LIMIT 10
-- SELECT * FROM film ORDER BY rental_rate ASC OFFSET 10 LIMIT 10
--SELECT customer.first_name, customer.last_name, customer.customer_id, amount, staff_id, payment date
FROM payment JOIN customer
ON payment.customer_id = customer.customer_id ORDER BY staff_id ASC
SELECT * FROM purchases INNER JOIN customers ON purchases.customer_id= customers.cust_id
SELECT title FROM film WHERE film_id NOT IN (SELECT DISTINCT film_id FROM inventory) 
SELECT city.city, country.country FROM city JOIN country
ON city.country_id = country.country_id