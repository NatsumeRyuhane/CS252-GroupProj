CREATE DATABASE `MGAF_db`;
  USE `MGAF_db`;


-- create
CREATE TABLE users (
  user_id     INT(8) UNSIGNED NOT NULL AUTO_INCREMENT,
  user_name   VARCHAR(20) NOT NULL,
  user_password   VARCHAR(255) NOT NULL,
  user_email  VARCHAR(255) NOT NULL,
  user_date   DATETIME NOT NULL,
  PRIMARY KEY (user_id)
) ENGINE=INNODB;

CREATE TABLE posts (
  post_id         INT NOT NULL AUTO_INCREMENT,
  post_content    TEXT NOT NULL,
  post_date       DATETIME NOT NULL,
  post_topic      INT(8) NOT NULL,
  post_by     INT(8) UNSIGNED NOT NULL,
  PRIMARY KEY (post_id)
) ENGINE=INNODB;

ALTER TABLE posts ADD FOREIGN KEY(post_by) REFERENCES users(user_id) ON DELETE RESTRICT ON UPDATE CASCADE;


-- fetch 
SELECT * FROM users;
SELECT * FROM posts;