-- Create database to use
show databses;
show tables;
drop database if exists school;
create database school;
use school;

-- Create table and add data
create table books(Acc_no varchar(5) primary key, Title varchar(200) UNIQUE NOT NULL, Author varchar(40), Subject varchar(25), Publisher varchar(25), Year_published int, Price int, No_copies int);
insert into books values ('C005', 'How networks work', 'Frank Derfler', 'Networking', 'Huga', 1999, 400, 2);
insert into books values ('C002', 'Beginning C++', 'Ivor Horton', 'Networking', 'Flipkart', 2001, 525, 5);
insert into books values ('M001', 'Cloud Computing', 'Ray Rafaels', 'Networking', 'Prime', 2015, 450, 3);
insert into books values ('CS03', 'Programming Python', 'Mark Lutz', 'Networking', 'Prime', 2011, 1150, NULL);
insert into books values ('P001', 'Internet of Things', 'Arsheep Bahga', 'Networking', 'Paperback', 2015, 587, 4);
insert into books values ('C004', 'The Complete C++ Reference', 'Schildt', 'Networking', 'Rediff', 1996, 490, 5);
insert into books values ('C001', 'Data Communications and Networking', 'Behrouz A. Forouzan', 'Networking', 'Huga', 2000, 750, 30);
insert into books values ('G001', 'Web Designing', 'Hirdesh Bharadwaj', 'Networking', 'Paperback', 2017, 475, 20);
insert into books values ('B001', 'Programming with Java', NULL, 'Networking', 'Paperback', 2016, 425, 15);

-- select command
select * from books;
select Acc_no, Author from books;
select Acc_no as "Account Number", Author, Title, Price as 'Book Price' from books;
select Price * 100 from books;
select ifnull(Author, 'anonymous') from books;
select distinct Publisher from books;
select 'Author is', Author from books;

-- desc command
desc books;

-- Calculations
select 1 + 2;
select 3 * 6 from dual;
select curdate();

-- where clause
select Title, Price from books where Price < 500;
select Title, Price from books where Price between 350 and 450;
select Title, Price from books where Title like '%C++%';
select Acc_no, Title, Price from books where Acc_no in ('M001', 'C001');
select Acc_no, Title, Price from books where Acc_no like 'C00_';
select Acc_no, Title, Price from books where Author is NULL;

-- order by clause
select Title, Price from books order by Price;
select Title, Price from books order by Price desc;
select Title, Price from books where Acc_no like 'C00_' order by Price;
select Title, Price, Publisher from books order by Publisher, Price desc;

-- aggregate functions
select avg(Price) "Average" from books;
select sum(Price) from books;
select count(distinct Publisher) from books;
select max(Price) from books;
select min(Price) from books;

-- Create command
create database if not exists school;
use school;
-- drop database school
create table books_issued(Acc_no varchar(5) primary key, Title varchar(200) UNIQUE NOT NULL, Author varchar(40), Subject varchar(25) references books(Acc_no), Publisher varchar(25), Year_published int, Price int check (price >= 0), No_copies int default 0);
create table new_books as (select * from books where Title like '%C++%');
select * from new_books;

-- insert command
insert into books_issued values ('C005', 'How networks work', 'Frank Derfler', 'Networking', 'Huga', 1999, 400, 2);
insert into books_issued (Acc_no, Title, Author, Publisher, Year_published) values ('CS03', 'Programming Python', 'Mark Lutz',  'Prime', 2011);
insert into new_books select * from books where Title like '%Python%';
select * from books_issued;

-- update command
update books_issued set Price = Price / 2;
update new_books set Price = Price - 200 where Title like '%Python%';
select * from new_books;
select * from books_issued;

-- delete command
delete from new_books where Year_published < 2000;
select * from new_books;

-- alter command
alter table books_issued modify Title char(100) NOT NULL;
alter table books_issued change No_copies Quantity int;
alter table books_issued drop primary key;
alter table books_issued add Rating int;
desc books_issued;

-- group by clause
select Publisher, count(*) from books group by Publisher;
select Publisher, count(*), sum(price) from books group by Publisher;
select Publisher, count(*), sum(price) from books group by Publisher having count(*) > 1;

-- joins
select * from new_books, books_issued;
select books.Title, books_issued.Price, Rating from books, books_issued;
select x.Title, y.Author, y.Title from books as x, books_issued as y;
select x.Title, x.Author, x.Price from books as x, books_issued as y where x.Price < 500;
select x.Title, y.Author from books as x, books_issued as y where x.Title = y.Title;
select x.Title, x.Price from books as x, books_issued as y where x.Title = y.Title order by x.Title;
select x.Title, x.Price from books as x, books_issued as y where x.Title = y.Title and y.Price < 500;
