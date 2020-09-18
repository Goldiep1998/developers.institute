CREATE FUNCTION calc_sum(order_id INT)
RETURNS INT AS $order_sum$
BEGIN

RETURN(SELECT sum(price) FROM items
JOIN orders ON orders.id = items.fk_orders_id WHERE orders.id = 'order_id');

END
 $order_sum$ LANGUAGE plpgsql;

 SELECT * FROM calc_sum(1)