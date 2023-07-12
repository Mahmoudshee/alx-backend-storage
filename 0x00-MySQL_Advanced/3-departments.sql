-- Create the departments table
CREATE TABLE IF NOT EXISTS departments (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

-- Insert sample data
INSERT INTO departments (name) VALUES ('Engineering');
INSERT INTO departments (name) VALUES ('Marketing');
INSERT INTO departments (name) VALUES ('Finance');

-- Show the departments table
SELECT * FROM departments;

