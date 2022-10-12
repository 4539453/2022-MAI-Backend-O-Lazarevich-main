-- Create new user and user's database 

CREATE ROLE filmadmin
  NOSUPERUSER
  CREATEDB
  NOCREATEROLE
  LOGIN
  PASSWORD 'P@ssword';
  
CREATE DATABASE films
  OWNER filmadmin
  ENCODING UTF8;

