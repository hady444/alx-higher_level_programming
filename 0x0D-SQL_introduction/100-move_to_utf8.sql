-- script that converts hbtn_0c_0 database to UTF-8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table ALTER COLUMN name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
