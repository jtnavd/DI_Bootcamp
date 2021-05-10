postgres=# \c Bootcamp
You are now connected to database "Bootcamp" as user "postgres".
Bootcamp=# SELECT * FROM students;
 id | last_name | first_name | birth_date
----+-----------+------------+------------
  1 | Marc      | Benichou   | 02/11/1998
  2 | Yoan      | Cohen      | 03/12/2010
  3 | Lea       | Benichou   | 27/071987
  4 | Amelia    | Dux        | 07/04/1996
  5 | David     | Grez       | 14/06/2003
  6 | Omer      | Simpson    | 03/10/1980
(6 rows)



Bootcamp=# SELECT first_name, last_name
Bootcamp-# FROM students;
 first_name | last_name
------------+-----------
 Benichou   | Marc
 Cohen      | Yoan
 Benichou   | Lea
 Dux        | Amelia
 Grez       | David
 Simpson    | Omer
(6 rows)



Bootcamp=# SELECT * FROM students
Bootcamp-# WHERE id = 2
Bootcamp-# ;
 id | last_name | first_name | birth_date
----+-----------+------------+------------
  2 | Yoan      | Cohen      | 03/12/2010
(1 row)



Bootcamp=# SELECT * FROM students
Bootcamp-# WHERE last_name = 'Marc' AND first_name = 'Benichou';
 id | last_name | first_name | birth_date
----+-----------+------------+------------
  1 | Marc      | Benichou   | 02/11/1998
(1 row)



Bootcamp=# SELECT * FROM students
Bootcamp-# WHERE last_name = 'Marc' OR first_name = 'Benichou';
 id | last_name | first_name | birth_date
----+-----------+------------+------------
  1 | Marc      | Benichou   | 02/11/1998
  3 | Lea       | Benichou   | 27/071987
(2 rows)



Bootcamp=# SELECT * FROM students
Bootcamp-# WHERE last_name LIKE '%a%';
 id | last_name | first_name | birth_date
----+-----------+------------+------------
  1 | Marc      | Benichou   | 02/11/1998
  2 | Yoan      | Cohen      | 03/12/2010
  3 | Lea       | Benichou   | 27/071987
  4 | Amelia    | Dux        | 07/04/1996
  5 | David     | Grez       | 14/06/2003
(5 rows)


Bootcamp=# SELECT * FROM students
Bootcamp-# WHERE last_name LIKE 'a%';
 id | last_name | first_name | birth_date
----+-----------+------------+------------
(0 rows)



Bootcamp=# SELECT * FROM students
Bootcamp-# WHERE last_name LIKE '%a';
 id | last_name | first_name | birth_date
----+-----------+------------+------------
  3 | Lea       | Benichou   | 27/071987
  4 | Amelia    | Dux        | 07/04/1996
(2 rows)



Bootcamp=# SELECT * FROM students
Bootcamp-# WHERE id = 1 OR id = 3;
 id | last_name | first_name | birth_date
----+-----------+------------+------------
  1 | Marc      | Benichou   | 02/11/1998
  3 | Lea       | Benichou   | 27/071987
(2 rows)