-- Create the users table
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    PRIMARY KEY (id)
);

-- Add unique constraint on email column
ALTER TABLE users
ADD CONSTRAINT unique_email UNIQUE (email);

