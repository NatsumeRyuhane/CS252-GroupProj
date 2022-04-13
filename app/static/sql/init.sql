CREATE DATABASE `MGAF`;
USE `MGAF`;

CREATE TABLE users (
  user_id     INT(8) UNSIGNED NOT NULL AUTO_INCREMENT,
  user_name   VARCHAR(20) NOT NULL,
  user_password   VARCHAR(255) NOT NULL,
  user_email  VARCHAR(255) NOT NULL,
  user_register_date   DATETIME NOT NULL,
  user_session_id CHAR(36),
  PRIMARY KEY (user_id)
) ENGINE=INNODB;

CREATE TABLE posts (
  post_id         INT NOT NULL AUTO_INCREMENT,
  post_content    TEXT NOT NULL,
  post_date       DATETIME NOT NULL,
  post_by     INT(8) UNSIGNED NOT NULL,
  post_likes INT UNSIGNED NOT NULL,
  PRIMARY KEY (post_id)
) ENGINE=INNODB;

ALTER TABLE posts ADD FOREIGN KEY(post_by) REFERENCES users(user_id) ON DELETE RESTRICT ON UPDATE CASCADE;