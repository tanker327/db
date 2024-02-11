
CREATE DATABASE "clipocean";

CREATE ROLE clipocean WITH LOGIN PASSWORD 'clipocean';

GRANT ALL PRIVILEGES ON DATABASE clipocean TO clipocean;
