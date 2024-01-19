-- Filename: 100-move_to_utf8.sql

-- Convert the database to UTF-8
ALTER DATABASE IF EXISTS hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the table to UTF-8
ALTER TABLE IF EXISTS first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the 'name' field to UTF-8
ALTER TABLE IF EXISTS first_table MODIFY COLUMN name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
