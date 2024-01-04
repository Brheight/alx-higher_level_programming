-- Script to create users and grant privileges

-- Create user user_0d_1 if it doesn't exist
CREATE USER 'user_0d_1'@'localhost';

-- Grant all privileges to user_0d_1 on all databases and tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Check the privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Create user user_0d_2 if it doesn't exist
CREATE USER 'user_0d_2'@'localhost';

-- Check the privileges for user_0d_2
-- This will result in an error because no privileges have been granted to user_0d_2 yet
SHOW GRANTS FOR 'user_0d_2'@'localhost';
