USE `MGAF`;

CREATE PROCEDURE insert_post()
BEGIN
    DECLARE v1 INT DEFAULT 100;

    WHILE v1 > 0 DO
    INSERT INTO posts (post_content, post_date, post_by, post_likes)
    VALUE
        ('{"title": "Test Post", "body": "This is a test post."}', now(), FLOOR(1 + (RAND() * 4)), RAND() * 100);
        SET v1 = v1 - 1;
    END WHILE;
END;

CALL insert_post()