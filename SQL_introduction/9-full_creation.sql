-- creates a new table with new values
    CREATE TABLE IF NOT EXISTS second_table(
        id INT,
        name VARCHAR(56),
        score INT
    );
    INSERT INTO second_table (id, name, score) VALUES
        (1, 'Jhon', 10),
        (2, 'Alex', 3),
        (3, 'Bob', 14),
        (4, 'George', 8);