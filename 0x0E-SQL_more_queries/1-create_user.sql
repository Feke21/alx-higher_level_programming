-- create MySQL server user, user_0d_1
-- create user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED by 'user_0d_1_pwd';
-- grant all privileges
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
