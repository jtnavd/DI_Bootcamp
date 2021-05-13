postgres=# \c dvdrental
You are now connected to database "dvdrental" as user "postgres".
dvdrental=# select * from customer
dvdrental-# ;
 customer_id | store_id | first_name  |  last_name   |                  email                   | address_id | activebool | create_date |       last_update       | active
-------------+----------+-------------+--------------+------------------------------------------+------------+------------+-------------+-------------------------+--------
         524 |        1 | Jared       | Ely          | jared.ely@sakilacustomer.org             |        530 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
           1 |        1 | Mary        | Smith        | mary.smith@sakilacustomer.org            |          5 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
           2 |        1 | Patricia    | Johnson      | patricia.johnson@sakilacustomer.org      |          6 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
           3 |        1 | Linda       | Williams     | linda.williams@sakilacustomer.org        |          7 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
           4 |        2 | Barbara     | Jones        | barbara.jones@sakilacustomer.org         |          8 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
           5 |        1 | Elizabeth   | Brown        | elizabeth.brown@sakilacustomer.org       |          9 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
           6 |        2 | Jennifer    | Davis        | jennifer.davis@sakilacustomer.org        |         10 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
           7 |        1 | Maria       | Miller       | maria.miller@sakilacustomer.org          |         11 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
           8 |        2 | Susan       | Wilson       | susan.wilson@sakilacustomer.org          |         12 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
           9 |        2 | Margaret    | Moore        | margaret.moore@sakilacustomer.org        |         13 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
          10 |        1 | Dorothy     | Taylor       | dorothy.taylor@sakilacustomer.org        |         14 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
          11 |        2 | Lisa        | Anderson     | lisa.anderson@sakilacustomer.org         |         15 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
          12 |        1 | Nancy       | Thomas       | nancy.thomas@sakilacustomer.org          |         16 | t        -- More  --