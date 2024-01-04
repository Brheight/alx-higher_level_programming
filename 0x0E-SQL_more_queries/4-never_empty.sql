-- Script to create the id_not_null table
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
INSERT INTO id_not_null (id, name) VALUES (89, 'Best School');
SELECT * FROM id_not_null;
