
-- 문제 3
create table ClubMember(
    id int unsigned not null auto_increment primary key, 
    student int unsigned, 
    club smallint unsigned not null,
    level tinyint(1) unsigned not null default 0,
    constraint foreign key fk_stu(student) references Student(id) on delete cascade,
    constraint foreign key fk_club(club) references Club(id) on delete cascade
);

-- 같은학생이 같은 동아리에 중복되지 않도록!!
alter table ClubMember add unique index uk_club_student (student, club);

-- 먼저 리더 처리
insert into ClubMember(club, student, level) select id, leader, 2 from Club where leader is not null;

-- 랜덤하게 학생 약 50명 (세개 클럽이니 150개) 등록
insert ignore into ClubMember(club, student, level)
 select c.id, s.id, 0 from Student s, Club c order by rand() limit 150;

-- 클럽별 몇명의 학생을 간부로 등록
select * from ClubMember where student < 100;   -- 적절하게 id로 끊어서 처리
update ClubMember set level = 1
 where student in (select id from Student where id < 100);
 
-- 클럽짱이 비어있는 4번 클럽에 회원 한명을 클럽짱으로!!
update ClubMember set level=2 where club=4 order by rand() limit 1;

-- 검증
select * from ClubMember;
select club, count(*) from ClubMember group by club;
select club, level, count(*) from ClubMember group by club, level;

drop table ClubMember;

show variables like '%commit%';

START transaction;
commit;


-- 문제 4
create table Dept(
    id smallint unsigned not null auto_increment primary key,
    name varchar(31) not null,
    prof smallint unsigned,
    student int unsigned,
    constraint foreign key fk_prof(prof) references Prof(id) on delete set null,
    constraint foreign key fk_student(student) references Student(id) on delete set null
);

alter table Student add column dept smallint unsigned;
alter table Student add constraint foreign key fk_dept(dept) references Dept(id);

select * from Dept;
select * from Student;
select * from Subject;

-- dept 생성
insert into Dept(name, prof)
 select '국문학과', id from Prof order by rand() limit 10;
 
-- 과이름 정리
select substring('국문학과,통계학과,역사학과,영문학과,물리학과,생물학과,화공학과,수리학과,윤리학과,사회학과', (id - 1) * 5 + 1 , 4) from Dept order by id;
update Dept set name = substring('국문학과,통계학과,역사학과,영문학과,물리학과,생물학과,화공학과,수리학과,윤리학과,사회학과', (id - 1) * 5 + 1 , 4) order by id;

-- 학생테이블 과배정
update Student set dept=(select id from Dept order by rand() limit 1);

-- 과 배정 검증
select dept, count(*) from Student group by dept;

-- Dept 테이블에 학생대표 저장
update Dept d set student = (select id from Student where dept = d.id order by rand() limit 1);

-- 학생대표 검증(해당 과대표가 해당 과 소속인지만 체크)
select d.name, d.student, d.id, (select dept from Student where id = d.student) from Dept d;


show create table Student;
show index from Student;

-- 정리 --------------------------------------------------------
alter table Student drop foreign key Student_ibfk_1;
alter table Student drop index fk_dept;
alter table Student drop column dept;
drop table Dept;
-- ------------------------------------------------------------


-- 문제 5. 강의실 문제
create table Classroom(
    id smallint unsigned not null auto_increment primary key,
    name varchar(31) not null
);

alter table Subject add column classroom smallint unsigned;
alter table Subject add constraint foreign key fk_classroom(classroom) references Classroom(id);

insert into Classroom(name)
select concat('10', id, '호') from Subject;

update Subject set classroom = (11 - id); 

-- 강의실 중복방지
alter table Subject add unique index uk_classroom(classroom);



-- if: rand를 이용한 중복방지
select ceil(rand(id) * 10) from Student;
select distinct(ceil(rand(id) * 10)) rr from Student;

update Subject s, (select distinct(ceil(rand(id) * 10)) rr from Student) x set classroom=x.rr;


select * from Subject;
select * from Classroom;

show create table Subject;
-- 정리 --------------------------------------------------------
alter table Subject drop foreign key Subject_ibfk_2;
alter table Subject drop index fk_classroom;
alter table Subject drop index uk_classroom;
alter table Subject drop column classroom;
drop table Classroom;
-- ------------------------------------------------------------


desc Prof;






















desc Club;
select * from Club;

select concat(ceil(rand() * 1000), '호') from Student order by id desc limit 10;

select * from jj;


select id from Subject order by rand();

update jj j inner join Subject s on j.stu <> s.id set j.stu = s.id;
 
 
update jj set stu = (select id from Subject order by rand() limit 1);

create table Pp As select * from jj;

desc Student;
desc Dept;

create table Dept(id int unsigned not null auto_increment primary key, student int unsigned, foreign key fk_aa(student) references Student(id));

alter table Student add column dept int unsigned;

alter table Student add constraint foreign key fk_sss(dept) references Dept(id);

drop table Dept;




update jj set stu = 1
  from Subject;

