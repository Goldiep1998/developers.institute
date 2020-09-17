UPDATE film  set language_id= '2' WHERE title LIKE '%y'
UPDATE film  set language_id= '4' WHERE title LIKE '%s'
UPDATE film  set language_id= '3' WHERE title LIKE '%e'

INSERT INTO customer (first_name, last_name, store_id,  address_id, activebool, create_date)
VALUES ('Micky', 'Mouse', 1, 9,true, '2003-11-13'),
('Minnie', 'Mouse', 1, 9, true, '2002-3-19'),
('Donald', 'Duck', 3, 22, true, '2014-9-3')

INSERT INTO film (title, release_year, language_id, rental_duration, rental_rate, replacement_cost, last_update)
VALUES('Harry Potter', 2009, 1, 3, 2.99, 12.99, '2013-4-4'),
('The Secrect Garden', 1998, 2, 4, 3.99, 9.99, '2012-3-3'),
('Percy Jackson', 2015, 1, 7,3.99, 14.99, '2015-3-4')

SELECT title FROM film_actor
JOIN film ON film_actor.film_id = film.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE actor.first_name = 'Penelope' AND actor.last_name ='Monroe' AND film.description ILIKE '%sumo wrestler%'

SELECT film.title FROM film_category 
JOIN category ON category.category_id = film_category.category_id 
JOIN film ON film.film_id = film_category.film_id
WHERE film.rating = 'R' AND film.length < '60' AND category.name ILIKE 'documentary'


CREATE VIEW js_action AS
SELECT title FROM film JOIN film_category
ON film.film_id = film_category.film_id
JOIN film_actor on film.film_id = film_actor.film_id
WHERE actor_id = (SELECT actor_id FROM actor WHERE first_name = 'Joe' AND last_name = 'Swank')
AND category_id = (SELECT category_id FROM category WHERE name = 'Action')



INSERT INTO rental (rental_date, inventory_id, customer_id, staff_id, last_update)
VALUES ('2019-3-5', 40, (SELECT customer_id FROM customer WHERE first_name = 'Minnie' AND last_name = 'Mouse'), 1, '2020-3-7')
VALUES ('2019-3-5', 98, (SELECT customer_id FROM customer WHERE first_name = 'Micky' AND last_name = 'Mouse'), 1, '2020-3-7')
VALUES ('2019-3-5', 910, (SELECT customer_id FROM customer WHERE first_name = 'Micky' AND last_name = 'Mouse'), 1, '2020-3-7')

