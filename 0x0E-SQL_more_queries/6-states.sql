-- script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_2;
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL  ,
    name varchar(256)
);