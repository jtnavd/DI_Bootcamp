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
          12 |        1 | Nancy       | Thomas       | nancy.thomas@sakilacustomer.org          |         16 | t        
          
          -- More  --
          \q



vdrental=# select first_name as full_name, last_name as full_name
dvdrental-# from customer;
  full_name  |  full_name
-------------+--------------
 Jared       | Ely
 Mary        | Smith
 Patricia    | Johnson
 Linda       | Williams
 Barbara     | Jones
 Elizabeth   | Brown
 Jennifer    | Davis
 Maria       | Miller
 Susan       | Wilson
 Margaret    | Moore
 Dorothy     | Taylor
 Lisa        | Anderson
 Nancy       | Thomas
 Karen       | Jackson
 Betty       | White
 Helen       | Harris
 Sandra      | Martin
 Donna       | Thompson
 Carol       | Garcia
 Ruth        | Martinez
 Sharon      | Robinson
 Michelle    | Clark
 Laura       | Rodriguez
 Sarah       | Lewis
 Kimberly    | Lee
 Deborah     | Walker
 Jessica     | Hall
 Shirley     | Allen
 Cynthia     | Young
 Angela      | Hernandez
 Melissa     | King
 Brenda      | Wright
 Amy         | Lopez
 Anna        | Hill
 Rebecca     | Scott




dvdrental=# select create_date from customer;
 create_date
-------------
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14
 2006-02-14




 dvdrental=# select * from customer
dvdrental-# order by first_name desc;
 customer_id | store_id | first_name  |  last_name   |                  email                   | address_id | activebool | create_date |       last_update       | active
-------------+----------+-------------+--------------+------------------------------------------+------------+------------+-------------+-------------------------+--------
         479 |        1 | Zachary     | Hite         | zachary.hite@sakilacustomer.org          |        484 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         174 |        2 | Yvonne      | Watkins      | yvonne.watkins@sakilacustomer.org        |        178 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         190 |        2 | Yolanda     | Weaver       | yolanda.weaver@sakilacustomer.org        |        194 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         212 |        2 | Wilma       | Richards     | wilma.richards@sakilacustomer.org        |        216 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         359 |        2 | Willie      | Markham      | willie.markham@sakilacustomer.org        |        364 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         219 |        2 | Willie      | Howell       | willie.howell@sakilacustomer.org         |        223 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         303 |        2 | William     | Satterfield  | william.satterfield@sakilacustomer.org   |        308 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         578 |        2 | Willard     | Lumpkin      | willard.lumpkin@sakilacustomer.org       |        584 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         469 |        2 | Wesley      | Bull         | wesley.bull@sakilacustomer.org           |        474 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         115 |        1 | Wendy       | Harrison     | wendy.harrison@sakilacustomer.org        |        119 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         370 |        2 | Wayne       | Truong       | wayne.truong@sakilacustomer.org          |        375 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         462 |        2 | Warren      | Sherrod      | warren.sherrod@sakilacustomer.org        |        467 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
          87 |        1 | Wanda       | Patterson    | wanda.patterson@sakilacustomer.org       |         91 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         339 |        2 | Walter      | Perryman     | walter.perryman@sakilacustomer.org       |        344 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         562 |        1 | Wallace     | Slone        | wallace.slone@sakilacustomer.org         |        568 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         598 |        1 | Wade        | Delvalle     | wade.delvalle@sakilacustomer.org         |        604 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         184 |        1 | Vivian      | Ruiz         | vivian.ruiz@sakilacustomer.org           |        188 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
          35 |        2 | Virginia    | Green        | virginia.green@sakilacustomer.org        |         39 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         581 |        1 | Virgil      | Wofford      | virgil.wofford@sakilacustomer.org        |        587 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         289 |        1 | Violet      | Rodriquez    | violet.rodriquez@sakilacustomer.org      |        294 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         244 |        2 | Viola       | Hanson       | viola.hanson@sakilacustomer.org          |        248 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         414 |        1 | Vincent     | Ralston      | vincent.ralston@sakilacustomer.org       |        419 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         116 |        1 | Victoria    | Gibson       | victoria.gibson@sakilacustomer.org       |        120 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         382 |        2 | Victor      | Barkley      | victor.barkley@sakilacustomer.org        |        387 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         251 |        2 | Vickie      | Brewer       | vickie.brewer@sakilacustomer.org         |        255 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         201 |        1 | Vicki       | Fields       | vicki.fields@sakilacustomer.org          |        205 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         158 |        1 | Veronica    | Stone        | veronica.stone@sakilacustomer.org        |        162 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         483 |        2 | Vernon      | Chapa        | vernon.chapa@sakilacustomer.org          |        488 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         218 |        1 | Vera        | Mccoy        | vera.mccoy@sakilacustomer.org            |        222 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1



dvdrental=# select film_id, title, description, release_year, rental_rate
dvdrental-# from film
dvdrental-# order by rental_rate asc;
 film_id |            title            |                                                            description                                                             | release_year | rental_rate
---------+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------+--------------+-------------
     341 | Frost Head                  | A Amazing Reflection of a Lumberjack And a Cat who must Discover a Husband in A MySQL Convention                                   |         2006 |        0.99
     634 | Odds Boogie                 | A Thrilling Yarn of a Feminist And a Madman who must Battle a Hunter in Berlin                                                     |         2006 |        0.99
     886 | Theory Mermaid              | A Fateful Yarn of a Composer And a Monkey who must Vanquish a Womanizer in The First Manned Space Station                          |         2006 |        0.99
     344 | Fury Murder                 | A Lacklusture Reflection of a Boat And a Forensic Psychologist who must Fight a Waitress in A Monastery                            |         2006 |        0.99
     345 | Gables Metropolis           | A Fateful Display of a Cat And a Pioneer who must Challenge a Pastry Chef in A Baloon Factory                                      |         2006 |        0.99
     631 | Novocaine Flight            | A Fanciful Display of a Student And a Teacher who must Outgun a Crocodile in Nigeria                                               |         2006 |        0.99
     630 | Notting Speakeasy           | A Thoughtful Display of a Butler And a Womanizer who must Find a Waitress in The Canadian Rockies                                  |         2006 |        0.99
     348 | Gandhi Kwai                 | A Thoughtful Display of a Mad Scientist And a Secret Agent who must Chase a Boat in Berlin                                         |         2006 |        0.99
      12 | Alaska Phantom              | A Fanciful Saga of a Hunter And a Pastry Chef who must Vanquish a Boy in Australia                                                 |         2006 |        0.99
     629 | Notorious Reunion           | A Amazing Epistle of a Woman And a Squirrel who must Fight a Hunter in A Baloon                                                    |         2006 |        0.99
     105 | Bull Shawshank              | A Fanciful Drama of a Moose And a Squirrel who must Conquer a Pioneer in The Canadian Rockies                                      |         2006 |        0.99
     352 | Gathering Calendar          | A Intrepid Tale of a Pioneer And a Moose who must Conquer a Frisbee in A MySQL Convention                                          |         2006 |        0.99
      36 | Argonauts Town              | A Emotional Epistle of a Forensic Psychologist And a Butler -- More  --




dvdrental=# select address, phone
dvdrental-# from address
dvdrental-# where district = 'Texas';
             address             |    phone
---------------------------------+--------------
 1795 Santiago de Compostela Way | 860452626434
 333 Goinia Way                  | 909029256431
 913 Coacalco de Berriozbal Loop | 262088367001
 530 Lausanne Lane               | 775235029633
 1894 Boa Vista Way              | 239357986667
(5 rows)




dvdrental=# select description
dvdrental-# from film
dvdrental-# where film_id between 15 and 150;
                                                            description
------------------------------------------------------------------------------------------------------------------------------------
 A Brilliant Drama of a Cat And a Mad Scientist who must Battle a Feminist in A MySQL Convention
 A Fast-Paced Drama of a Robot And a Composer who must Battle a Astronaut in New Orleans
 A Fast-Paced Character Study of a Composer And a Dog who must Outgun a Boat in An Abandoned Fun House
 A Thoughtful Drama of a Composer And a Feminist who must Meet a Secret Agent in The Canadian Rockies
 A Emotional Display of a Pioneer And a Technical Writer who must Battle a Man in A Baloon
 A Boring Drama of a Woman And a Squirrel who must Conquer a Student in A Baloon
 A Insightful Drama of a Girl And a Astronaut who must Face a Database Administrator in A Shark Tank
 A Emotional Character Study of a Dentist And a Crocodile who must Meet a Sumo Wrestler in California
 A Lacklusture Display of a Dentist And a Dentist who must Fight a Girl in Australia
 A Thoughtful Display of a Explorer And a Pastry Chef who must Overcome a Feminist in The Sahara Desert
 A Thoughtful Display of a Woman And a Astronaut who must Battle a Robot in Berlin
 A Amazing Panorama of a Pastry Chef And a Boat who must Escape a Woman in An Abandoned Amusement Park
 A Amazing Reflection of a Database Administrator And a Astronaut who must Outrace a Database Administrator in A Shark Tank
 A Touching Panorama of a Waitress And a Woman who must Outrace a Dog in An Abandoned Amusement Park
 A Fateful Yarn of a Womanizer And a Feminist who must Succumb a Database Administrator in Ancient India
 A Epic Story of a Pastry Chef And a Woman who must Chase a Feminist in An Abandoned Fun House
 A Awe-Inspiring Reflection of a Pastry Chef And a Teacher who must Overcome a Sumo Wrestler in A U-Boat
 A Astounding Story of a Dog And a Squirrel who must Defeat a Woman in An Abandoned Amusement Park
 A Action-Packed Reflection of a Crocodile And a Explorer who must Find a Sumo Wrestler in An Abandoned Mine Shaft
 A Touching Epistle of a Madman And a Mad Cow who must Defeat a Student in Nigeria
 A Action-Packed Reflection of a Pastry Chef And a Composer who must Discover a Mad Scientist in The First Manned Space Station
 A Emotional Epistle of a Forensic Psychologist And a Butler who must Challenge a Waitress in An Abandoned Mine Shaft
 A Brilliant Panorama of a Mad Scientist And a Mad Cow who must Meet a Pioneer in A Monastery
 A Beautiful Yarn of a Pioneer And a Monkey who must Pursue a Explorer in The Sahara Desert
 A Fast-Paced Tale of a Boat And a Teacher who must Succumb a Composer in An Abandoned Mine Shaft
 A Boring Saga of a Database Administrator And a Womanizer who must Battle a Waitress in Nigeria
 A Fanciful Documentary of a Mad Cow And a Womanizer who must Find a Dentist in Berlin
 A Stunning Reflection of a Robot And a Moose who must Challenge a Woman in California
 A Thrilling Yarn of a Feminist And a Hunter who must Fight a Technical Writer in A Shark Tank
 A Fast-Paced Panorama of a Technical Writer And a Mad Scientist who must Find a Feminist in An Abandoned Mine Shaft
 A Astounding Panorama of a Composer And a Frisbee who must Reach a Husband in Ancient Japan
 A Beautiful Tale of a Dentist And a Mad Cow who must Battle a Moose in The Sahara Desert
 A Boring Character Study of a A Shark And a Girl who must Outrace a Feminist in An Abandoned Mine Shaft
 A Stunning Character Study of a Mad Scientist And a Mad Cow who must Kill a Car in A Monastery
 A Emotional Panorama of a Pioneer And a Composer who must Escape a Mad Scientist in A Jet Boat
 A Stunning Drama of a Forensic Psychologist And a Husband who must Overcome a Waitress in A Monastery
 A Insightful Panorama of a Forensic Psychologist And a Mad Cow who must Build a Mad Scientist in The First Manned Space Station
 A Thrilling Documentary of a Composer And a Monkey who must Find a Feminist in California
 A Epic Drama of a Madman And a Cat who must Face a A Shark in An Abandoned Amusement Park
 A Awe-Inspiring Drama of a Car And a Pastry Chef who must Chase a Crocodile in The First Manned Space Station
 A Awe-Inspiring Story of a Feminist And a Cat who must Conquer a Dog in A Monastery
 A Intrepid Story of a Cat And a Student who must Vanquish a Girl in An Abandoned Amusement Park
 A Stunning Epistle of a Man And a Husband who must Reach a Mad Scientist in A Jet Boat
 A Fateful Display of a Womanizer And a Mad Scientist who must Outgun a A Shark in Soviet Georgia
 A Astounding Saga of a Dog And a Boy who must Kill a Teacher in The First Manned Space Station
 A Awe-Inspiring Epistle of a Student And a Squirrel who must Defeat a Boy in Ancient China
 A Fast-Paced Display of a Composer And a Moose who must Sink a Robot in An Abandoned Mine Shaft
 A Astounding Panorama of a Lumberjack And a Dog who must Redeem a Woman in An Abandoned Fun House
 A Astounding Character Study of a Madman And a Robot who must Meet a Mad Scientist in An Abandoned Fun House
 A Epic Display of a Pioneer And a Student who must Challenge a Butler in The Gulf of Mexico
 A Unbelieveable Drama of a Student And a Husband who must Outrace a Sumo Wrestler in Berlin
 A Astounding Panorama of a Man And a Monkey who must Discover a Man in The First Manned Space Station
 A Taut Saga of a Crocodile And a Boy who must Overcome a Technical Writer in Ancient China
 A Emotional Character Study of a Boat And a Pioneer who must Find a Explorer in A Shark Tank
 A Fanciful Documentary of a Womanizer And a Boat who must Defeat a Madman in The First Manned Space Station
 A Astounding Drama of a Astronaut And a Cat who must Discover a Woman in The First Manned Space Station
 A Emotional Reflection of a Teacher And a Man who must Meet a Cat in The First Manned Space Station
 A Stunning Saga of a Mad Scientist And a Forensic Psychologist who must Challenge a Squirrel in A MySQL Convention
 A Touching Tale of a Girl And a Crocodile who must Discover a Waitress in Nigeria
 A Fanciful Panorama of a Husband And a Pioneer who must Outgun a Dog in A Baloon
dvdrental=#



dvdrental=# select * from film
dvdrental-# order by rental_rate asc
dvdrental-# limit 10;
 film_id |        title         |                                                description                                                | release_year | language_id | rental_duration | rental_rate | length | replacement_cost | rating |       last_update       |                  special_features                   |                                                                          fulltext
---------+----------------------+-----------------------------------------------------------------------------------------------------------+--------------+-------------+-----------------+-------------+--------+------------------+--------+-------------------------+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------
      19 | Amadeus Holy         | A Emotional Display of a Pioneer And a Technical Writer who must Battle a Man in A Baloon                 |         2006 |           1 |               6 |        0.99 |    113 |            20.99 | PG     | 2013-05-26 14:50:58.951 | {Commentaries,"Deleted Scenes","Behind the Scenes"} | 'amadeus':1 'baloon':20 'battl':15 'display':5 'emot':4 'holi':2 'man':17 'must':14 'pioneer':8 'technic':11 'writer':12
      23 | Anaconda Confessions | A Lacklusture Display of a Dentist And a Dentist who must Fight a Girl in Australia                       |         2006 |           1 |               3 |        0.99 |     92 |             9.99 | R      | 2013-05-26 14:50:58.951 | {Trailers,"Deleted Scenes"}                         | 'anaconda':1 'australia':18 'confess':2 'dentist':8,11 'display':5 'fight':14 'girl':16 'lacklustur':4 'must':13
      17 | Alone Trip           | A Fast-Paced Character Study of a Composer And a Dog who must Outgun a Boat in An Abandoned Fun House     |         2006 |           1 |               3 |        0.99 |     82 |            14.99 | R      | 2013-05-26 14:50:58.951 | {Trailers,"Behind the Scenes"}                      | 'abandon':22 'alon':1 'boat':19 'charact':7 'compos':11 'dog':14 'fast':5 'fast-pac':4 'fun':23 'hous':24 'must':16 'outgun':17 'pace':6 'studi':8 'trip':2
      18 | Alter Victory        | A Thoughtful Drama of a Composer And a Feminist who must Meet a Secret Agent in The Canadian Rockies      |         2006 |           1 |               6 |        0.99 |     57 |            27.99 | PG-13  | 2013-05-26 14:50:58.951 | {Trailers,"Behind the Scenes"}                      | 'agent':17 'alter':1 'canadian':20 'compos':8 'drama':5 'feminist':11 'meet':14 'must':13 'rocki':21 'secret':16 'thought':4 'victori':2
      12 | Alaska Phantom       | A Fanciful Saga of a Hunter And a Pastry Chef who must Vanquish a Boy in Australia                        |         2006 |           1 |               6 |        0.99 |    136 |            22.99 | PG     | 2013-05-26 14:50:58.951 | {Commentaries,"Deleted Scenes"}                     | 'alaska':1 'australia':19 'boy':17 'chef':12 'fanci':4 'hunter':8 'must':14 'pastri':11 'phantom':2 'saga':5 'vanquish':15
     213 | Date Speed           | A Touching Saga of a Composer And a Moose who must Discover a Dentist in A MySQL Convention               |         2006 |           1 |               4 |        0.99 |    104 |            19.99 | R      | 2013-05-26 14:50:58.951 | {Commentaries}                                      | 'compos':8 'convent':20 'date':1 'dentist':16 'discov':14 'moos':11 'must':13 'mysql':19 'saga':5 'speed':2 'touch':4
      11 | Alamo Videotape      | A Boring Epistle of a Butler And a Cat who must Fight a Pastry Chef in A MySQL Convention                 |         2006 |           1 |               6 |        0.99 |    126 |            16.99 | G      | 2013-05-26 14:50:58.951 | {Commentaries,"Behind the Scenes"}                  | 'alamo':1 'bore':4 'butler':8 'cat':11 'chef':17 'convent':21 'epistl':5 'fight':14 'must':13 'mysql':20 'pastri':16 'videotap':2
      14 | Alice Fantasia       | A Emotional Drama of a A Shark And a Database Administrator who must Vanquish a Pioneer in Soviet Georgia |         2006 |           1 |               6 |        0.99 |     94 |            23.99 | NC-17  | 2013-05-26 14:50:58.951 | {Trailers,"Deleted Scenes","Behind the Scenes"}     | 'administr':13 'alic':1 'databas':12 'drama':5 'emot':4 'fantasia':2 'georgia':21 'must':15 'pioneer':18 'shark':9 'soviet':20 'vanquish':16
       1 | Academy Dinosaur     | A Epic Drama of a Feminist And a Mad Scientist who must Battle a Teacher in The Canadian Rockies          |         2006 |           1 |               6 |        0.99 |     86 |            20.99 | PG     | 2013-05-26 14:50:58.951 | {"Deleted Scenes","Behind the Scenes"}              | 'academi':1 'battl':15 'canadian':20 'dinosaur':2 'drama':5 'epic':4 'feminist':8 'mad':11 'must':14 'rocki':21 'scientist':12 'teacher':17
      26 | Annie Identity       | A Amazing Panorama of a Pastry Chef And a Boat who must Escape a Woman in An Abandoned Amusement Park     |         2006 |           1 |               3 |        0.99 |     86 |            15.99 | G      | 2013-05-26 14:50:58.951 | {Commentaries,"Deleted Scenes"}                     | 'abandon':20 'amaz':4 'amus':21 'anni':1 'boat':12 'chef':9 'escap':15 'ident':2 'must':14 'panorama':5 'park':22 'pastri':8 'woman':17
(10 rows)




dvdrental=# select * from film
dvdrental-# order by rental_rate asc
dvdrental-# offset 10 limit 10;
 film_id |        title         |                                                 description                                                  | release_year | language_id | rental_duration | rental_rate | length | replacement_cost | rating |       last_update       |                special_features                 |                                                                          fulltext
---------+----------------------+--------------------------------------------------------------------------------------------------------------+--------------+-------------+-----------------+-------------+--------+------------------+--------+-------------------------+-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------
      40 | Army Flintstones     | A Boring Saga of a Database Administrator And a Womanizer who must Battle a Waitress in Nigeria              |         2006 |           1 |               4 |        0.99 |    148 |            22.99 | R      | 2013-05-26 14:50:58.951 | {Trailers,Commentaries}                         | 'administr':9 'armi':1 'battl':15 'bore':4 'databas':8 'flintston':2 'must':14 'nigeria':19 'saga':5 'waitress':17 'woman':12
      23 | Anaconda Confessions | A Lacklusture Display of a Dentist And a Dentist who must Fight a Girl in Australia                          |         2006 |           1 |               3 |        0.99 |     92 |             9.99 | R      | 2013-05-26 14:50:58.951 | {Trailers,"Deleted Scenes"}                     | 'anaconda':1 'australia':18 'confess':2 'dentist':8,11 'display':5 'fight':14 'girl':16 'lacklustur':4 'must':13
      11 | Alamo Videotape      | A Boring Epistle of a Butler And a Cat who must Fight a Pastry Chef in A MySQL Convention                    |         2006 |           1 |               6 |        0.99 |    126 |            16.99 | G      | 2013-05-26 14:50:58.951 | {Commentaries,"Behind the Scenes"}              | 'alamo':1 'bore':4 'butler':8 'cat':11 'chef':17 'convent':21 'epistl':5 'fight':14 'must':13 'mysql':20 'pastri':16 'videotap':2
      12 | Alaska Phantom       | A Fanciful Saga of a Hunter And a Pastry Chef who must Vanquish a Boy in Australia                           |         2006 |           1 |               6 |        0.99 |    136 |            22.99 | PG     | 2013-05-26 14:50:58.951 | {Commentaries,"Deleted Scenes"}                 | 'alaska':1 'australia':19 'boy':17 'chef':12 'fanci':4 'hunter':8 'must':14 'pastri':11 'phantom':2 'saga':5 'vanquish':15
     213 | Date Speed           | A Touching Saga of a Composer And a Moose who must Discover a Dentist in A MySQL Convention                  |         2006 |           1 |               4 |        0.99 |    104 |            19.99 | R      | 2013-05-26 14:50:58.951 | {Commentaries}                                  | 'compos':8 'convent':20 'date':1 'dentist':16 'discov':14 'moos':11 'must':13 'mysql':19 'saga':5 'speed':2 'touch':4
      17 | Alone Trip           | A Fast-Paced Character Study of a Composer And a Dog who must Outgun a Boat in An Abandoned Fun House        |         2006 |           1 |               3 |        0.99 |     82 |            14.99 | R      | 2013-05-26 14:50:58.951 | {Trailers,"Behind the Scenes"}                  | 'abandon':22 'alon':1 'boat':19 'charact':7 'compos':11 'dog':14 'fast':5 'fast-pac':4 'fun':23 'hous':24 'must':16 'outgun':17 'pace':6 'studi':8 'trip':2
      14 | Alice Fantasia       | A Emotional Drama of a A Shark And a Database Administrator who must Vanquish a Pioneer in Soviet Georgia    |         2006 |           1 |               6 |        0.99 |     94 |            23.99 | NC-17  | 2013-05-26 14:50:58.951 | {Trailers,"Deleted Scenes","Behind the Scenes"} | 'administr':13 'alic':1 'databas':12 'drama':5 'emot':4 'fantasia':2 'georgia':21 'must':15 'pioneer':18 'shark':9 'soviet':20 'vanquish':16
      26 | Annie Identity       | A Amazing Panorama of a Pastry Chef And a Boat who must Escape a Woman in An Abandoned Amusement Park        |         2006 |           1 |               3 |        0.99 |     86 |            15.99 | G      | 2013-05-26 14:50:58.951 | {Commentaries,"Deleted Scenes"}                 | 'abandon':20 'amaz':4 'amus':21 'anni':1 'boat':12 'chef':9 'escap':15 'ident':2 'must':14 'panorama':5 'park':22 'pastri':8 'woman':17
       1 | Academy Dinosaur     | A Epic Drama of a Feminist And a Mad Scientist who must Battle a Teacher in The Canadian Rockies             |         2006 |           1 |               6 |        0.99 |     86 |            20.99 | PG     | 2013-05-26 14:50:58.951 | {"Deleted Scenes","Behind the Scenes"}          | 'academi':1 'battl':15 'canadian':20 'dinosaur':2 'drama':5 'epic':4 'feminist':8 'mad':11 'must':14 'rocki':21 'scientist':12 'teacher':17
      63 | Bedazzled Married    | A Astounding Character Study of a Madman And a Robot who must Meet a Mad Scientist in An Abandoned Fun House |         2006 |           1 |               6 |        0.99 |     73 |            21.99 | PG     | 2013-05-26 14:50:58.951 | {Trailers,"Deleted Scenes","Behind the Scenes"} | 'abandon':21 'astound':4 'bedazzl':1 'charact':5 'fun':22 'hous':23 'mad':17 'madman':9 'marri':2 'meet':15 'must':14 'robot':12 'scientist':18 'studi':6
(10 rows)






dvdrental=# select (first_name, last_name) as full_name, amount, payment_date from payment
dvdrental-# inner join customer on payment.customer_id = customer.customer_id
dvdrental-# order by payment.customer_id;
        full_name        | amount |        payment_date
-------------------------+--------+----------------------------
 (Mary,Smith)            |   5.99 | 2007-02-14 23:22:38.996577
 (Mary,Smith)            |   0.99 | 2007-02-15 16:31:19.996577
 (Mary,Smith)            |   9.99 | 2007-02-15 19:37:12.996577
 (Mary,Smith)            |   4.99 | 2007-02-16 13:47:23.996577
 (Mary,Smith)            |   4.99 | 2007-02-18 07:10:14.996577
 (Mary,Smith)            |   0.99 | 2007-02-18 12:02:25.996577
 (Mary,Smith)            |   3.99 | 2007-02-21 04:53:11.996577
 (Mary,Smith)            |   4.99 | 2007-03-01 07:19:30.996577
 (Mary,Smith)            |   3.99 | 2007-03-02 14:05:18.996577
 (Mary,Smith)            |   0.99 | 2007-03-02 16:30:04.996577
 (Mary,Smith)            |   4.99 | 2007-03-17 11:06:20.996577
 (Mary,Smith)            |   0.99 | 2007-03-18 02:25:55.996577
 (Mary,Smith)            |   0.99 | 2007-03-19 08:23:42.996577
 (Mary,Smith)            |   2.99 | 2007-03-19 12:25:20.996577
 (Mary,Smith)            |   0.99 | 2007-03-21 22:02:23.996577
 (Mary,Smith)            |   1.99 | 2007-03-21 23:56:23.996577
 (Mary,Smith)            |   2.99 | 2007-03-22 18:10:03.996577
 (Mary,Smith)            |   5.99 | 2007-03-22 18:32:12.996577
 (Mary,Smith)            |   5.99 | 2007-04-08 01:45:31.996577
 (Mary,Smith)            |   5.99 | 2007-04-08 06:02:22.996577
 (Mary,Smith)            |   4.99 | 2007-04-09 11:52:33.996577
 (Mary,Smith)            |   4.99 | 2007-04-09 15:06:27.996577
 (Mary,Smith)            |   7.99 | 2007-04-11 08:42:12.996577
 (Mary,Smith)            |   2.99 | 2007-04-27 09:59:48.996577
 (Mary,Smith)            |   4.99 | 2007-04-28 07:33:11.996577
 (Mary,Smith)            |   4.99 | 2007-04-28 14:46:49.996577
 (Mary,Smith)            |   0.99 | 2007-04-28 16:02:05.996577
 (Mary,Smith)            |   0.99 | 2007-04-28 17:48:33.996577
 (Mary,Smith)            |   2.99 | 2007-04-29 02:27:15.996577
 (Mary,Smith)            |   2.99 | 2007-04-30 01:10:44.996577
 (Patricia,Johnson)      |   2.99 | 2007-02-17 19:23:24.996577
 (Patricia,Johnson)      |   0.99 | 2007-03-01 08:13:52.996577
 (Patricia,Johnson)      |   0.99 | 2007-03-02 00:39:22.996577
 (Patricia,Johnson)      |   5.99 | 2007-03-02 06:10:07.996577
 (Patricia,Johnson)      |   6.99 | 2007-03-02 09:12:14.996577
 (Patricia,Johnson)      |   2.99 | 2007-03-02 12:13:19.996577
 (Patricia,Johnson)      |   2.99 | 2007-03-17 02:20:44.996577
 (Patricia,Johnson)      |   2.99 | 2007-03-19 04:54:30.996577
 (Patricia,Johnson)      |   4.99 | 2007-03-21 11:52:58.996577
 (Patricia,Johnson)      |   5.99 | 2007-03-21 21:10:22.996577
 (Patricia,Johnson)      |   4.99 | 2007-03-22 12:21:30.996577
 (Patricia,Johnson)      |   4.99 | 2007-03-23 16:08:01.996577
 (Patricia,Johnson)      |   2.99 | 2007-04-10 04:59:50.996577
 (Patricia,Johnson)      |   6.99 | 2007-04-10 11:07:22.996577
 (Patricia,Johnson)      |   4.99 | 2007-04-27 12:59:08.996577
 (Patricia,Johnson)      |   5.99 | 2007-04-27 13:51:28.996577
 (Patricia,Johnson)      |   5.99 | 2007-04-27 17:08:46.996577
 (Patricia,Johnson)      |   5.99 | 2007-04-28 22:41:25.996577
 (Patricia,Johnson)      |   2.99 | 2007-04-29 11:25:25.996577
 (Patricia,Johnson)      |   5.99 | 2007-04-29 15:42:55.996577
 (Patricia,Johnson)      |   4.99 | 2007-04-30 04:34:36.996577
 (Patricia,Johnson)      |  10.99 | 2007-04-30 12:16:09.996577
 (Patricia,Johnson)      |   0.99 | 2007-04-30 12:42:37.996577
 (Patricia,Johnson)      |   6.99 | 2007-04-30 14:49:39.996577
 (Patricia,Johnson)      |   6.99 | 2007-04-30 21:08:19.996577
 (Patricia,Johnson)      |   2.99 | 2007-04-30 20:27:22.996577
 (Linda,Williams)        |   8.99 | 2007-02-16 00:02:31.996577
 (Linda,Williams)        |   6.99 | 2007-02-16 13:47:36.996577
 (Linda,Williams)        |   6.99 | 2007-02-17 03:43:41.996577
 (Linda,Williams)        |   2.99 | 2007-02-19 07:03:19.996577




dvdrental=# select title from film
dvdrental-# left join inventory on film.film_id = inventory.film_id
dvdrental-# where inventory.inventory_id is null
dvdrental-# order by title;
         title
------------------------
 Alice Fantasia
 Apollo Teen
 Argonauts Town
 Ark Ridgemont
 Arsenic Independence
 Boondock Ballroom
 Butch Panther
 Catch Amistad
 Chinatown Gladiator
 Chocolate Duck
 Commandments Express
 Crossing Divorce
 Crowds Telemark
 Crystal Breaking
 Dazed Punk
 Deliverance Mulholland
 Firehouse Vietnam
 Floats Garden
 Frankenstein Stranger
 Gladiator Westward
 Gump Date
 Hate Handicap
 Hocus Frida
 Kentuckian Giant
 Kill Brotherhood
 Muppet Mile
 Order Betrayed
 Pearl Destiny
 Perdition Fargo
 Psycho Shrunk
 Raiders Antitrust
 Rainbow Shock
 Roof Champion
 Sister Freddy
 Sky Miracle
 Suicides Silence
 Tadpole Park
 Treasure Command
 Villain Desperate
 Volume House
 Wake Jaws
 Walls Artist
(42 rows)




dvdrental=# select country, city
dvdrental-# from city
dvdrental-# inner join country
dvdrental-# on country.country_id = city.country_id
dvdrental-# group by country.country, city.city
dvdrental-# order by country.country;
                country                |            city
---------------------------------------+----------------------------
 Afghanistan                           | Kabul
 Algeria                               | Batna
 Algeria                               | Bchar
 Algeria                               | Skikda
 American Samoa                        | Tafuna
 Angola                                | Benguela
 Angola                                | Namibe
 Anguilla                              | South Hill
 Argentina                             | Almirante Brown
 Argentina                             | Avellaneda
 Argentina                             | Baha Blanca
 Argentina                             | Crdoba
 Argentina                             | Escobar
 Argentina                             | Ezeiza
 Argentina                             | La Plata
 Argentina                             | Merlo
 Argentina                             | Quilmes
 Argentina                             | San Miguel de Tucumn
 Argentina                             | Santa F
 Argentina                             | Tandil
 Argentina                             | Vicente Lpez
 Armenia                               | Yerevan
 Australia                             | Woodridge
 Austria                               | Graz
 Austria                               | Linz
 Austria                               | Salzburg
 Azerbaijan                            | Baku
 Azerbaijan                            | Sumqayit
 Bahrain                               | al-Manama
 Bangladesh                            | Dhaka
 Bangladesh                            | Jamalpur
 Bangladesh                            | Tangail
 Belarus                               | Mogiljov
 Belarus                               | Molodetno
 Bolivia                               | El Alto
 Bolivia                               | Sucre
 Brazil                                | Alvorada
 Brazil                                | Angra dos Reis
 Brazil                                | Anpolis
 Brazil                                | Aparecida de Goinia
 Brazil                                | Araatuba
 Brazil                                | Bag
 Brazil                                | Belm
 Brazil                                | Blumenau
 Brazil                                | Boa Vista
 Brazil                                | Braslia
 Brazil                                | Goinia
 Brazil                                | Guaruj
 Brazil                                | guas Lindas de Gois
 Brazil                                | Ibirit
 Brazil                                | Juazeiro do Norte
 Brazil                                | Juiz de Fora
 Brazil                                | Luzinia
 Brazil                                | Maring
 Brazil                                | Po
 Brazil                                | Poos de Caldas
 Brazil                                | Rio Claro
 Brazil                                | Santa Brbara dOeste
 Brazil                                | Santo Andr
 Brazil                                | So Bernardo do Campo