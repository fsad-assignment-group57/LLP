drop database if exists llp;

create database llp;
use llp;

CREATE TABLE user_languages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    language VARCHAR(255) NOT NULL
);