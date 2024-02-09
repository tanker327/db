# Use the official PostgreSQL image as the base
FROM postgres:15.4

# Copy the initialization script to the correct location
COPY init.sql /docker-entrypoint-initdb.d/
