-- script that creates the database hbtn_0d_2 and the user user_0d_2.
CREATE DATABASE hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON 'user_0d_2'@'localhost' ON GRANT OPTION;
FLUSH PRIVILEGES;
