postgres=# \c public
You are now connected to database "public" as user "postgres".
public=# select * from items
public-# ;
 id |  products  | prizes
----+------------+--------
  7 | Small Desk |    100
  8 | Large Desk |    300
  9 | Fan        |     80
(3 rows)



public=# select * from items
public-# order by prizes +0;
 id |  products  | prizes
----+------------+--------
  9 | Fan        |     80
  7 | Small Desk |    100
  8 | Large Desk |    300
(3 rows)



public=# select prizes from items
public-# where prizes >= 80
public-# order by prizes +0;
 prizes
--------
     80
    100
    300
(3 rows)



public=# select * from customer
public-# order by firstname asc
public-# limit 3;
 firstname | lastname
-----------+----------
 Greg      | Jones
 Melanie   | Johnson
 Sandra    | Jones
(3 rows)



public=# select lastname from customer
public-# order by lastname desc;
 lastname
----------
 Scott
 Jones
 Jones
 Johnson
 Green
(5 rows)



public=# create table purchases(
public(# customer_id varchar not null,
public(# item_id varchar not null);
CREATE TABLE
public=# select * from purchases
public-# ;
 customer_id | item_id
-------------+---------
(0 rows)



