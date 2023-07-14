-- Show initial state of the users table
SELECT * FROM users;

-- Insert some data into the users table
INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");
INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");
INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Jean");

-- Show the updated state of the users table
SELECT * FROM users;

