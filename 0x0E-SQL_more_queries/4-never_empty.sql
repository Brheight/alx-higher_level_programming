-- Script to create the id_not_null table

-- Create the table id_not_null if it doesn't exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

-- Insert data into the id_not_null table
INSERT INTO id_not_null (id, name) VALUES (89, 'Best School');

-- Query to select all rows from the id_not_null table
SELECT * FROM id_not_null;
