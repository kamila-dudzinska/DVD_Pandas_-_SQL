# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 19:27:31 2026

@author: Kamila Dudzińska
"""

sql_filmy = """
        SELECT
                f.film_id,
                f.title,
                f.release_year,
                f.length,
                a.actor_id,
                a.first_name,
                a.last_name,
                l.language_id,
                l.name AS lname,
                cu.customer_id,
                cu.first_name,
                cu.last_name,
                cu.active,
                ci.city,
                cou.country,
                pay.amount
        FROM film AS f
        JOIN film_actor AS fa ON f.film_id = fa.film_id
        JOIN actor AS a ON fa.actor_id = a.actor_id
        JOIN language AS l ON f.language_id = l.language_id
        JOIN inventory AS i ON f.film_id = i.film_id
        JOIN customer AS cu ON i.store_id = cu.store_id
        JOIN payment AS pay ON cu.customer_id = pay.customer_id
        JOIN address AS ad ON cu.address_id = ad.address_id
        JOIN city AS ci ON ad.city_id = ci.city_id
        JOIN country AS cou ON ci.country_id = cou.country_id
		LIMIT 500000;
"""   
