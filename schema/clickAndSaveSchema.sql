drop table Business cascade constraints;
drop table participants cascade constraints;
drop table items cascade constraints;
drop table ownsBusiness cascade constraints;
​
create table Business(
    id int, 
    name varchar(255),
    password varchar(255),
    address varchar(255),
    county varchar(255),
    phone_number int,
    primary key(id)
    );
    
create table participants(
    email varchar(255),
    firstName varchar(255),
    lastName varchar(255),
    income int,
    password varchar(255),
    primary key(email)
    );
    
create table items(
    name varchar(255),
    category varchar(255),
    postPrice numeric (8, 2),
    originalPrice numeric(8,2),
    quantity int,
    bId int,
    foreign key (bId) references Business(id),
    constraint PK_itemBusiness primary key(name, bId)
    );
    
create table ownsBusiness(
    email varchar(255),
    bId int,
    foreign key(email) references participants(email),
    foreign key(bId) references Business(id),
    constraint PK_ownsbusiness primary key(email,bId)
    );
