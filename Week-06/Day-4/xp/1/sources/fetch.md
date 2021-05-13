--Exercise 1
select first_name as "First Name",last_name as "Last Name" from employees;
--Exercise 2
select distinct first_name, last_name, department_id from employees order by department_id;
--Exercise 3
select * from employees order by first_name;
--Exercise 4
select first_name, last_name, salary, (salary*15)/100 as PF from employees;
--Exercise 5
select employee_id, (first_name, last_name)as names, salary from employees order by salary asc;
--Exercise 6
select sum(salary) from employees;
--Exercise 7
select max(salary) as "maximum salary", min(salary) "minimum salary" from employees;
--Exercise 8
select avg(salary) as "average salary" from employees;
--Exercise 9
select count(employee_id) from employees;
--Exercise 10
select upper(first_name) from employees;
--Exercise 11
select substring(first_name,1,3) from employees;
--Exercise 12
select (first_name, last_name) as full_name from employees;
