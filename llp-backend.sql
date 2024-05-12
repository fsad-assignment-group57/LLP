-- drop database if exists llp;

-- create database llp;
use llp;

-- CREATE TABLE users (
--    id INT AUTO_INCREMENT PRIMARY KEY,
--    user_id VARCHAR(255) NOT NULL,
--    name VARCHAR(255) NOT NULL
-- );

-- INSERT INTO users (user_id, name) VALUES (1, "sagar");
-- INSERT INTO users (user_id, name) VALUES (2, "manjusha");
-- INSERT INTO users (user_id, name) VALUES (3, "sampada");

CREATE TABLE user_languages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    language VARCHAR(255) NOT NULL
);

INSERT INTO user_languages (user_id, language) VALUES ("sampada", "English");
INSERT INTO user_languages (user_id, language) VALUES ("sampada", "Sanskrit");
INSERT INTO user_languages (user_id, language) VALUES ("sagar", "English");
INSERT INTO user_languages (user_id, language) VALUES ("manjusha", "French");



SELECT * from user_languages;
SELECT * from users;

INSERT INTO user_languages (user_id, language)
SELECT * FROM (SELECT 4, "Portugese") AS temp
WHERE NOT EXISTS (
    SELECT 1
    FROM user_languages
    WHERE user_id = 4 AND language = "Portugese"
);

SELECT language FROM user_languages WHERE user_id = 3;

DROP TABLE user_languages;

DELETE from user_languages WHERE user_id = 4;

-- ---

CREATE TABLE user_streak(
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    streak int NOT NULL,
    update_time datetime NOT NULL
);

INSERT INTO user_streaks (user_id, streak, update_time) VALUES ("sagar", 3, NOW());
INSERT INTO user_streak (user_id, streak, update_time) VALUES ("ramesha", 4, DATE_SUB(NOW(), INTERVAL 1 DAY));
INSERT INTO user_streak (user_id, streak, update_time) VALUES ("mukesha", 8, DATE_SUB(NOW(), INTERVAL 2 DAY));
INSERT INTO user_streak (user_id, streak, update_time) VALUES ("suresha", 6, DATE_SUB(NOW(), INTERVAL 3 DAY));

SELECT * from user_streak;

SELECT streak, update_time from user_streaks WHERE user_id = 'sampada';
UPDATE user_streaks SET streak = 5, update_time = now() WHERE user_id = 'sampada';
