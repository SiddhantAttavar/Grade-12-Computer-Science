create database school;
use school;

create table books(Acc_no varchar(5) primary key, Title varchar(200), Author varchar(40), Subject varchar(25), Publisher varchar(25), Year_published int, Price int, No_copies int);
insert into books values ('C005', 'How networks work', 'Frank Derfler', 'Networking', 'Huga', 1999, 400, 2);
insert into books values ('C002', 'Beginning C++', 'Ivor Horton', 'Networking', 'Flipkart', 2001, 525, 5);
insert into books values ('M001', 'Cloud Computing', 'Ray Rafaels', 'Networking', 'Prime', 2015, 450, 3);
insert into books values ('CS03', 'Programming Python', 'Mark Lutz', 'Networking', 'Prime', 2011, 1150, NULL);
insert into books values ('P001', 'Internet of Things', 'Arsheep Bahga', 'Networking', 'Paperback', 2015, 587, 4);
insert into books values ('C004', 'The Complete C++ Reference', 'Schildt', 'Networking', 'Rediff', 1996, 490, 5);
insert into books values ('C001', 'Data Communications and Networking', 'Behrouz A. Forouzan', 'Networking', 'Huga', 2000, 750, 30);
insert into books values ('G001', 'Web Designing', 'Hirdesh Bharadwaj', 'Networking', 'Paperback', 2017, 475, 20);
insert into books values ('B001', 'Programming with Java', 'Barry A. Burd', 'Networking', 'Paperback', 2016, 425, 15);

create table books_issued(Accno varchar(5) primary key, Member_name varchar(50) unique not null, Date_issued date);
insert into books_issued values ('B001', 'Amish Singh', '2019-07-17');
insert into books_issued values ('CS003', 'Rajesh Murthy', '2019-07-24');
insert into books_issued values ('C004', 'Shreya Vasanth', '2019-08-15');
insert into books_issued values ('P001', 'Arun Verma', '2019-08-16');
insert into books_issued values ('M001', 'Roopa Roy', '2019-09-02');

-- 2. Display the structure of the tables: BOOKS and BOOKS_ISSUED 
desc books;
desc books_issued;

-- 3. Display the contents of the tables: BOOKS and BOOKS_ISSUED
select * from books;
select * from books_issued;

-- 4. List the book details published by Prime
select * from books where Publisher like 'Prime';

-- 5. Display title and author of all books. Use the headings: Book_title and Author_name
select title as Book_title, Author as Author_name from books;

-- 6. Display the details of the book titled Internet of Things.
select * from books where title like "Internet of Things";

-- 7. List the books title published between 2010 and 2015.
select title from books where Year_published between 2010 and 2015;

-- 8. Add a new book with the following data: (Pl. take care of the order of attributes)
-- C009, Digital Image Processing, Computer Science, Gonzalez and Woods, Pearson, 2015, 750, 5
insert into books values('C009', 'Digital Image Processing', 'Computer Science', 'Gonalez and Woods', 'Pearson', 2015, 750, 5);

-- 9. Add a new book with the following data: (Pl. take care of the number of attributes)
-- K001, Cracking the Coding interview, Gayle Laakmann McDowell, Computer Science, 2008,599
insert into books values('K001', 'Cracking the Coding interview', 'Gayle Laakmann McDowell', 'Computer Science', 2008, 599, NULL);

-- 10.	Display the details of books with number of copies > 4
select * from books where No_copies > 4;

-- 11.	Display the price of the books published by Paperback
select price from books where Publisher like 'Paperback';

-- 12.	List all C++ books
select * from books where Title like '%C++%';

-- 13.	List the books published in the year 1996, 1999, 2017
select * from books where Year_published in (1996, 1997, 2017);

-- 14.	List the different subjects
select distinct subject from books;

-- 15.	List the books priced more than 500
select * from books where Price > 500;

-- 16.	Display Title of all books with Acc_no in ascending order of Title
select title from books order by Title;

-- 17.	Display book details in the descening order of price
select * from books order by price desc;

-- 18.	List the books starting with P
select * from books where title like 'P%';

-- 19. List the books starting with P  
select * from books where title like 'P%';

-- 20. Increase the no_copies  of  Huga books by 5

-- 21. Create a table to store the details of books published after 2000
create table new_books(Acc_no varchar(5) primary key, Title varchar(200), Author varchar(40), Subject varchar(25), Publisher varchar(25), Year_published int, Price int, No_copies int);
insert into new_books select * from books where Year_published > 2000;

-- 22. Add a column total and store the total price of books
alter table books add (total int);

-- 23. Populate the column total with values

-- 24. Find the number of publishers.

-- 25. List the earliest and latest published books.

-- 26. Change the size of the attribute Title to store 50 characters.
alter table books modify Title varchar(50);

-- 27. Find the difference between the highest and least priced books

-- 28. Find the average price of Prime books

-- 29. List the different publishers
select distinct Publisher from books;

-- 30. Find the number of books issued

-- 31. List the total value of books

-- 32. Find the average price of the books published 

-- 33. List the books that were issued on/ before  6th August 2019

-- 34. Delete the book published by Flipkart before 2012 