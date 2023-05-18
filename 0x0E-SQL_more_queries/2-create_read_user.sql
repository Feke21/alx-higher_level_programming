--create database hbtn_0d_2 and user, user_0d_2
-- create database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create user_0d_2 with passwd
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grant select privileges in database hbtn_0d_2
GRANT SELECT ON `hbtn_0d_2.`* TO 'user_0d_2'@'localhost';
