
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



Bootcamp=# SELECT * FROM students
Bootcamp-# LIMIT 4;
 id | last_name | first_name | birth_date
----+-----------+------------+------------
  1 | Marc      | Benichou   | 02/11/1998
  2 | Yoan      | Cohen      | 03/12/2010
  3 | Lea       | Benichou   | 27/071987
  4 | Amelia    | Dux        | 07/04/1996
(4 rows)



!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



Bootcamp=# SELECT * FROM students
Bootcamp-# LIMIT 2 OFFSET 3;
 id | last_name | first_name | birth_date
----+-----------+------------+------------
  4 | Amelia    | Dux        | 07/04/1996
  5 | David     | Grez       | 14/06/2003
(2 rows)