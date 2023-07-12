-- Create the users table
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    PRIMARY KEY (id)
);

-- Insert sample data
INSERT INTO users (email, name) VALUES ('john@example.com', 'John Doe');
INSERT INTO users (email, name) VALUES ('jane@example.com', 'Jane Smith');
INSERT INTO users (email, name) VALUES ('michael@example.com', 'Michael Johnson');

-- Show the users table
SELECT * FROM users;

