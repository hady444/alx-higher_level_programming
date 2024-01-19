-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;

-- Convert the table to utf8mb4 with the specified collation
ALTER TABLE first_table
    CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the name field to utf8mb4 with the specified collation
ALTER TABLE first_table
    MODIFY COLUMN name varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
