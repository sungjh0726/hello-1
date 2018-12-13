-- 1)
select max(d.department_name) department_name, count(distinct e.employee_id) emp_cnt
  from Employees e inner join Departments d on e.department_id = d.department_id
  group by e.department_id
  order by emp_cnt desc;
  
-- 2)
select max(d.department_name) department_name, round(avg(e.salary), -1) avg_sal
  from Employees e inner join Departments d on e.department_id = d.department_id
  group by e.department_id
  order by avg_sal desc;
  
-- 4) 방식 1
select sub.*
  from (
        select e.employee_id, e.salary, e.manager_id,
               (select salary from Employees where employee_id = e.manager_id) mgr_sal
          from Employees e
       ) sub
 where sub.salary > sub.mgr_sal;
 
-- 4) 방식2
select e.*
  from Employees es inner join Employees e on es.employee_id = e.manager_id
 where e.salary > es.salary;
 
-- 5) 
-- select e.first_name || ' ' || e.last_name as emp_name, e.salary
select concat(concat(e.first_name, ' '), e.last_name) as emp_name, e.salary
  from Employees e inner join Jobs j on e.job_id = j.job_id
 where j.job_title = 'Sales Representative'
   and e.salary between 9000 and 10000;
   
select concat(concat(e.first_name, ' '), e.last_name) as emp_name, e.salary
  from Employees e
 where job_id = (select job_id from Jobs where job_title='Sales Representative')
   and e.salary between 9000 and 10000;

select * from Employees;

select rownum, rn
  from (select rownum as rn, e.* from Employees e where rownum < 10 order by salary desc, employee_id);

select rownum as rn, e.* from Employees e where rownum < 10 order by salary desc, employee_id;

select employee_id, manager_id from Employees order by manager_id;

select salary, trunc(salary, -1) from Employees;

