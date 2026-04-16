/*
a) In the table actor actor-id, first name, last naame, and last update are included
b) this table stores all details about films, including identification, pricing, duration, and metadata.
c) film actor table
d) This information is somewhat hard to read because it uses IDs
    (like customer_id and inventory_id) instead of actual names or movie titles. You need to 
     join this table with other tables (like customer or film) to fully understand the data.
 e) This table is also hard to read on its own because it only uses IDs
 (film_id, store_id) instead of actual movie names or store details. To fully understand it,
 you would need to join it with other tables like film (for the title) and store.    
 
SELECT rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film; 

These are the relevant tables because: rental tells you the rental dateinventory connects the rental to a film .film gives you the film title
*/