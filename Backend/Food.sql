-- mysql -u root -p < setup_mysql_dev.sql

-- # database 
CREATE DATABASE IF NOT EXISTS food_App_db;

-- # user
CREATE USER IF NOT EXISTS 'app_admin'@'localhost' IDENTIFIED BY 'food_pwd';

-- # grant privileges
GRANT ALL PRIVILEGES ON food_App_db.* TO 'app_admin'@'localhost';
FLUSH PRIVILEGES;

-- # have select privileges on database_Schema
GRANT SELECT ON perfomance_schema.* TO 'app_admin'@'localhost';  # gives select privileges on all tables in the database
FLUSH PRIVILEGES;
