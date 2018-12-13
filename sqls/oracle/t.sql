select sysdate, current_timestamp from dual;

select to_char(sysdate, 'YYYY-mm-dd HH24:MI:SS') from dual;

select to_char(current_timestamp, 'YYYY-mm-dd HH:MI:SS AM') from dual;

select to_char(CURRENT_TIMESTAMP, 'WW W DDD RM DY PM TZD')
  from dual;

select to_char(tsz, 'J'), to_char(tsz, 'YY-MM-DD HH24:MI:SS') from Test;

select power(2,3), sqrt(2) from dual;

select to_date('2018-12-25 12:22:44', 'YYYY-MM-DD HH24:MI:SS') from dual;


select manager_id, NVL(manager_id, 12), uid, user from Employees;
select manager_id as "매니저 ID", 'abc' "abc", NVL(manager_id, 12), uid, user from Employees;

select decode(employee_id, 100, 'one', 200, 'two', 150, 'ten', 'none') from Employees;
select (case employee_id when 100 then 'one' else 'none' end) from Employees;

select * from Employees;

select USERENV('sid') from dual;

desc Employees;

select max(salary) from Employees;
select least(1,5,3,2,9) from dual;

select replace('abc', 'bc', 'x') from dual;


create table Test (
	ts   timestamp,
	tsz  timestamp with time zone,
	ts0  timestamp(0)
);

insert into Test(ts, tsz, ts0)
 values(SYSDATE, SYSDATE, SYSDATE);

select ts, tsz, ts0, lengthb(ts), lengthb(tsz),
       lengthb(ts0) from Test;
       
       
select salary, count(*) cnt from Employees group by salary order by cnt desc;

select stats_mode(salary) from Employees;


select employee_id, first_name, salary,
	  dense_rank() over(order by salary) Ranking
  from Employees;
 
select e.job_id, max(j.job_title), sum(e.salary) tot
  from Employees e inner join Jobs j on e.job_id = j.job_id
 group by e.job_id
 order by tot desc;
 
 
select NVL(department_id, 0) from Employees where department_id is null;

-- ---------------------------------------------------------------------------------------
-- 6
select sub.*
  from (
        select max(j.job_title) job_title, sum(e.salary) tot
          from Employees e inner join Jobs j on e.job_id = j.job_id
         group by e.job_id
         order by tot desc) sub
 where sub.tot > 30000;
 
 
-- 7
select sub.*
  from (
        select l.city, round(avg(e.salary)) avg_salary
          from Locations l inner join Departments d on l.location_id = d.location_id
                           inner join Employees e on d.department_id = e.department_id
         group by l.city
         order by avg_salary desc) sub
 where rownum <= 3;



-- 8
select to_char(e.hire_date, 'YYYY') hire_year, avg(e.salary) avg_sal
  from Employees e inner join Jobs j on e.job_id = j.job_id
 where j.job_title = 'Sales Manager'
 group by to_char(e.hire_date, 'YYYY')
 order by to_char(e.hire_date, 'YYYY');
 
-- 9
select * from Locations;
select * from Departments;

select l.city, avg(e.salary) avg_salary, count(e.employee_id) emp_cnt
  from Locations l inner join Departments d on l.location_id = d.location_id
                   inner join Employees e on d.department_id = e.department_id
 group by l.city
 having count(*) < 10
 order by avg(e.salary);

-- 11
select e.employee_id, e.first_name, e.last_name, NVL(d.department_name, '<Not Assigned>') department_name
  from Employees e left outer join Departments d on e.department_id = d.department_id
 where to_char(e.hire_date, 'YYYY') = '2007';
 
-- 12
select min(department_name) department_name, min(e.salary) salary, count(e.employee_id) emp_cnt
  from Employees e left outer join Departments d on e.department_id = d.department_id
 group by e.department_id
 order by salary;

select sub.department_name, ee.last_name, ee.salary
    from (
        select min(department_name) department_name, min(e.salary) salary, count(e.employee_id) emp_cnt
          from Employees e inner join Departments d on e.department_id = d.department_id
         group by e.department_id) sub inner join Employees ee on sub.salary = ee.salary
 order by sub.department_name, ee.last_name;
 

-- 13
select sub.last_name, sub.first_name, sub.salary
  from (
        select last_name, first_name, salary,
            rank() over(order by salary desc) as ranking
          from Employees
        ) sub
 where ranking between 6 and 10;
 
-- 14
select e.first_name, e.salary, d.department_name
  from Employees e inner join Departments d on e.department_id = d.department_id
 where d.department_name = 'Sales'
   and e.salary < (select avg(salary) from Employees where department_id=100);
   
select hire_date, to_char(hire_date, 'MM'), to_char(hire_date, 'Mon') from Employees;
   
-- 15
select max(d.department_name) department_name, to_char(e.hire_date, 'MM') mm, count(*) emp_cnt
  from Employees e inner join Departments d on e.department_id = d.department_id
 group by e.department_id, to_char(e.hire_date, 'MM')
 having count(*) >= 5
 order by department_name;
 
select max(d.department_name) department_name, to_char(e.hire_date, 'MM') mm, count(*) emp_cnt
  from Employees e inner join Departments d on e.department_id = d.department_id
 where d.department_id in (select department_id from Employees group by department_id having count(*) >= 5)
 group by e.department_id, to_char(e.hire_date, 'MM')
 -- having count(*) >= 5
 order by department_name;

 
-- 16
select d.department_name, e.first_name, e.salary, e.commission_pct
  from Employees e inner join Departments d on e.department_id = d.department_id
 order by e.commission_pct desc nulls last, e.salary desc;

select sub.* from (
    select d.department_name, e.first_name, e.salary, e.commission_pct
      from Employees e inner join Departments d on e.department_id = d.department_id
     order by e.commission_pct desc nulls last, e.salary desc) sub
 where rownum <= 4;







  
select * from Employees;
 
select employee_id, first_name, salary, rownum,
	  row_number() over(order by salary) Ranking
  from Employees;
 
select employee_id, first_name, department_id, salary, 
      rank() over(partition by department_id order by salary desc) ranking
  from Employees;
  
select * from Employees;




desc Departments;


