CREATE TABLE leads(
id serial PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
email VARCHAR(355) NOT NULL,
signup_date TIMESTAMP NOT NULL,
minutes_spend integer NOT NULL
);