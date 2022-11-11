grant select, insert, update, delete on participants to hlee3;
grant select, insert, update, delete on business to hlee3;
grant select, insert, update, delete on items to hlee3;


drop table participants cascade constraints;
drop table Business cascade constraints;
drop table items cascade constraints;
drop table ownsBusiness cascade constraints;



create table participants(
    email varchar(30),
    firstName varchar(30),
    lastName varchar(30),
    income numeric(10, 2),
    password varchar(30),
    primary key(email)
);    

create table Business(
    id int,
    name varchar(30),
    password varchar(30),
    address varchar(30),
    county varchar(30),
    phoneNumber int
);

create table items(
    name varchar(30),
    category varchar(30),
    postPrice float, 
    originalPrice float,
    quantity int, 
    bID int,
    foreign key(bID) references Business(id)
);

create table ownsBusiness(
    email varchar(30) unique, 
    bID int unique,
    foreign key(email) references participants(email),
    foreign key(bID) references Business(id)
);

