-- 1. Create the 'webshare' database
CREATE DATABASE IF NOT EXISTS webshare
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_general_ci;

-- 2. Use the 'webshare' database
USE webshare;

-- 3. Create the 'proxies' table
CREATE TABLE IF NOT EXISTS proxies (
    id INT NOT NULL AUTO_INCREMENT,
    proxy_address VARCHAR(255) NOT NULL,
    port INT NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    country_code VARCHAR(20) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
