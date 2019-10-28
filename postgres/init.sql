CREATE DATABASE scraper;
CREATE USER scraper WITH PASSWORD 'password';
ALTER ROLE scraper SET client_encoding TO 'utf8';
ALTER ROLE scraper SET default_transaction_isolation TO 'read committed';
ALTER ROLE scraper SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE scraper TO scraper;
