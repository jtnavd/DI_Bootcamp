postgres=# \c Hollywood
You are now connected to database "Hollywood" as user "postgres".
Hollywood=# SELECT * FROM actors
Hollywood-# ;
 actors_id | firstname | lastname |    age     | number_oscars | married
-----------+-----------+----------+------------+---------------+---------
         1 | John      | Cleese   | 1939-10-27 |             2 |
         2 | Piers     | Brosnan  | 1963-05-16 |             1 |
         3 | Sharon    | Stone    | 1958-03-10 |             2 |
         4 | Halle     | Berry    | 1966-08-14 |             3 |
         5 | Sean      | Connery  | 1930-08-25 |             6 |
         6 | Nicolas   | Cage     | 1968-01-07 |             1 |
         7 | Anthony   | Hopkins  | 1937-12-31 |             3 |
(7 rows)


Hollywood=# SELECT COUNT(*)
Hollywood-# FROM actors;
 count
-------
     7
(1 row)