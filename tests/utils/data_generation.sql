USE `MGAF`;

INSERT INTO MGAF.users (user_name, user_password, user_email, user_register_date, user_session_id)
VALUE
    ('Alice', '1234', 'alice@mgaf.com', now(), uuid()),
    ('Bob', '1234', 'bob@mgaf.com', now(), uuid()),
    ('Carl', '1234', 'carl@mgaf.com', now(), uuid())
;

INSERT INTO MGAF.user_info (user_id, user_motto, user_major, user_grade)
VALUE
    (2, NULL, NULL, NULL),
    (3, NULL, NULL, NULL),
    (4, NULL, NULL, NULL)
;

INSERT INTO MGAF.posts (post_reply_id, post_content, post_date, post_last_update, post_by, post_likes)
VALUE
    (0, '{"title": "Test Post", "body": "This is a test post."}', now(), now(), 3, 0),
    (0, '{"title": "Test Post", "body": "This is another test post."}', now(), now(), 2, 0)
;

INSERT INTO MGAF.posts (post_topic_id, post_reply_id, post_content, post_date, post_last_update, post_by, post_likes)
VALUE
    (1, 1, '{"title": null, "body": "This is a test reply test post."}', now(), NULL, 2, 0),
    (1, 2, '{"title": null, "body": "This is another test reply test post."}', now(), NULL, 3, 0),
    (1, 3, '{"title": null, "body": "Seriously why there are so many tests?"}', now(), NULL, 1, 0),
    (1, 4, '{"title": null, "body": "Okay I think it is time to stop now."}', now(), NULL, 1, 0),
    (1, 5, '{"title": null, "body": "IT\'S TIME TO STOP."}', now(), NULL, 1, 0)
;