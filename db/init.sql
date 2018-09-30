CREATE USER admin with passworld 'admin';
ALTER role admin SET client_encoding to 'utf8';
CREATE DATABASE service2;
grant all privileges on DATABASE service2 to admin;
GRANT ALL ON ALL TABLES IN SCHEMA public to admin;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public to admin;
GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to admin;

