-- creates database hbtn_0d_usa and table, states (in database hbtn_0d_2) in MySQL server
-- create database hbtn_0d_usa
CREATE TABLE IF NOT EXISTS hbtn_0d_usa;
-- use created database
USE hbtn_0d_usa;
-- create table states
CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL UNIQUE AUTO_INCREMENT,
        name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id)
);	
