USE `MGAF`;

INSERT INTO users (user_name, user_password, user_email, user_register_date, user_session_id)
VALUE
    ('Admin', '1234', 'admin@mgaf.com', now(), uuid()),
    ('Alice', '1234', 'alice@mgaf.com', now(), uuid()),
    ('Bob', '1234', 'bob@mgaf.com', now(), uuid()),
    ('Carl', '1234', 'carl@mgaf.com', now(), uuid())
;

INSERT INTO posts (post_content, post_date, post_by, post_likes)
VALUE
    ('Hi! This is a test post.', now(), 1, 0),
    ('Hi! This is another test post.', now(), 2, 0)
;