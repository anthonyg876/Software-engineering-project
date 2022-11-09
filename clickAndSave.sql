grant select, insert, update, delete on participants to hlee3;
grant select, insert, update, delete on business to hlee3;
grant select, insert, update, delete on items to hlee3;


create table participants(
    email varchar(30),
    firstName varchar(30),
    lastName varchar(30),
    income numeric(10, 2),
    password varchar(30),
    primary key(email)
);    