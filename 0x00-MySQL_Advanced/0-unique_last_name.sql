-- Create the employees table
CREATE TABLE IF NOT EXISTS employees (
    id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

-- Add unique constraint on last_name column
ALTER TABLE employees
ADD CONSTRAINT unique_last_name UNIQUE (last_name);

