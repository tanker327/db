-- Create a new database 
CREATE DATABASE "clipocean";
-- Create a new user with password 
CREATE ROLE clipocean WITH LOGIN PASSWORD 'clipocean';
-- Grant privileges to the new user
GRANT ALL PRIVILEGES ON DATABASE clipocean TO clipocean;
-- enable support for UUIDs
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";