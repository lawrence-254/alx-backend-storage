-- This script creates a table 'users' with specified attributes and requirements


IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'users')
BEGIN
	CREATE TABLE users (
		id INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
		email VARCHAR(255) UNIQUE NOT NULL,
		name VARCHAR(255)
		);
END;
