-- creates second_table if it does not already exist, and adds rows
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
-- populates second_table with initial records
INSERT INTO second_table (id, name, score) VALUES
    (1, "John", 10),
    (2, "Alex", 3),
    (3, "Bob", 14),
    (4, "George", 8);
