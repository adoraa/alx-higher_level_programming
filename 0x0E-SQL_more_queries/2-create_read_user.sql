-- Check if the database hbtn_0d_2 already exists, and if not, create it
-- Check if the user user_0d_2 already exists, and if not, create it
-- Grant SELECT privilege to user_0d_2 only on the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
