
postgres=# \c public
public=# SELECT * FROM items;
 id |  products  | prizes
----+------------+--------
  7 | Small Desk |    100
  8 | Large Desk |    300
  9 | Fan        |     80
(3 rows)



public=# SELECT * FROM items
public-# WHERE prizes=80;
 id | products | prizes
----+----------+--------
  9 | Fan      |     80
(1 row)



public=# SELECT * FROM items
public-# WHERE prizes=300;
 id |  products  | prizes
----+------------+--------
  8 | Large Desk |    300
(1 row)




public=# SELECT * FROM customer
public-# ;
 firstname | lastname
-----------+----------
 Greg      | Jones
 Sandra    | Jones
 Scott     | Scott
 Trevor    | Green
 Melanie   | Johnson
(5 rows)



public=# SELECT * FROM customer
public-# WHERE  firstname = 'Smith' AND lastname = 'Smith';
 firstname | lastname
-----------+----------
(0 rows)




public=# SELECT * FROM customer
public-# WHERE lastname = 'Jones' OR firstname = 'Jones';
 firstname | lastname
-----------+----------
 Greg      | Jones
 Sandra    | Jones
(2 rows)




public=# SELECT firstname, lastname
public-# FROM customer
public-# EXCEPT
public-# SELECT firstname, lastname
public-# FROM customer
public-# WHERE firstname = 'Jones' OR lastname = 'Jones';
 firstname | lastname
-----------+----------
 Scott     | Scott
 Melanie   | Johnson
 Trevor    | Green
(3 rows)
