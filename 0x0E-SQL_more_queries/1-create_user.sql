-- creates the database hbtn_0d_2 and the user user_0d_2.
-- creates the MySQL server user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';