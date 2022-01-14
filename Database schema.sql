create table papers1 (
id bigserial not null primary key,
title varchar(500),
researcher_id bigint,
degree_id int,
date_of_publish bigint
);
create table supervisor1 (
id bigserial not null primary key,
supervisor varchar(500)
);
create table researcher1 (
id bigserial not null primary key,
researcher varchar(500)
);
create table degree1 (
id serial not null primary key,
degree_type varchar(50)
);

--// altering papers1 by specifing researcher_id and supervisor_id as foreign keys //--
alter table papers1 add foreign key(researcher_id) references researcher1(id) on delete set null;

alter table papers1 add foreign key(degree_id) references degree1(id) on delete set null;


--// creating manytomany relation between papers1 and supervisor1 //--
create table paper_supervisor (
paper_id bigint,
supervisor_id bigint,
primary key(paper_id,supervisor_id),
foreign key(supervisor_id) references supervisor1(id) on delete cascade,
foreign key(paper_id) references papers1(id) on delete cascade
);


-- // seperating the names to 4 names //--
alter table researcher1 add third_name varchar(50);
alter table researcher1 add second_name varchar(50);
alter table researcher1 add fourth_name varchar(50);
alter table researcher1 add first_name varchar(50);
alter table researcher1 drop column researcher;

alter table supervisor1 add first_name varchar(50);
alter table supervisor1 add second_name varchar(50);
alter table supervisor1 add third_name varchar(50);
alter table supervisor1 add fourth_name varchar(50);
alter table supervisor1 drop column supervisor;



--// adding alternative name and titles //--
alter table researcher1 add alternative_name varchar(50);
alter table supervisor1 add alternative_name varchar(50);
alter table researcher1 add title varchar(50);
alter table supervisor1 add title varchar(50);