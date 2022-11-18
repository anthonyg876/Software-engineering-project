drop table Business cascade constraints;
drop table participants cascade constraints;
drop table items cascade constraints;
drop table ownsBusiness cascade constraints;
​
create table Business(
    id int, 
    name varchar(30),
    password varchar(20),
    address varchar(30),
    county varchar(30),
    phone_number int,
    primary key(id)
    );
    
create table participants(
    email varchar(30),
    firstName varchar(30),
    lastName varchar(30),
    income int,
    password varchar(30),
    primary key(email)
    );
    
create table items(
    name varchar(30),
    category varchar(30),
    postPrice numeric (8, 2),
    originalPrice numeric(8,2),
    quantity int,
    bId int,
    foreign key (bId) references Business(id),
    constraint PK_itemBusiness primary key(name, bId)
    );
    
create table ownsBusiness(
    userEmail varchar(30),
    bId int,
    foreign key(userEmail) references participants(email),
    foreign key(bId) references Business(id),
    constraint PK_ownsbusiness primary key(userEmail,bId)
    );
