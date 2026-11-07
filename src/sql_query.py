# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 19:27:31 2026
Extended on Sat Nov  7 14:41:37 2026

@author: Kamila Dudzińska
SQL query to upload the columns needed for data  further analysis. 
Corrected SQL query to avoid duplicated rows (cartesian) and ensure data accuracy.

"""

sql_filmy = """
        SELECT
                f.film_id,
                f.title,
                f.release_year,
                f.length,
                l.language_id,
                l.name AS lname,
                cu.customer_id,
                cu.first_name,
                cu.last_name,
                cu.active,
                ci.city,
                cou.country,
                pay.amount
        FROM payment AS pay
        JOIN rental AS r ON pay.rental_id = r.rental_id
        JOIN inventory AS i ON r.inventory_id = i.inventory_id
        JOIN film AS f ON i.film_id = f.film_id
        JOIN language AS l ON f.language_id = l.language_id
        JOIN customer AS cu ON pay.customer_id = cu.customer_id
        JOIN address AS ad ON cu.address_id = ad.address_id
        JOIN city AS ci ON ad.city_id = ci.city_id
        JOIN country AS cou ON ci.country_id = cou.country_id;
"""   
