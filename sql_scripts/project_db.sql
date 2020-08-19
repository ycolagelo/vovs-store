CREATE TABLE IF NOT EXISTS 'user'
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username VARCHAR(80) NOT NULL,
    hash VARCHAR(500) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone INTEGER,
    created_date DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS 'orders'
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    created_date DATETIME NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES user(id)
);

CREATE TABLE IF NOT EXISTS 'tran'
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    amount NUMBER NOT NULL,
    date DATETIME NOT NULL,
    type INTEGER NOT NULL,
    orders_id INTEGER NOT NULL,
    FOREIGN KEY (orders_id) REFERENCES orders(id)
);

CREATE TABLE IF NOT EXISTS 'user_adress'
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    city VARCHAR(80) NOT NULL,
    street_name VARCHAR(255) NOT NULL,
    street_number INTEGER NOT NULL,
    postal_code VARCHAR(6) NOT NULL,
    province VARCHAR(2) NOT NULL,
    created_date DATETIME NOT NULL,
    FOREIGN KEY(user_id) REFERENCES user(id)
);

CREATE TABLE IF NOT EXISTS 'cart'
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    state INTEGER NOT NULL,
    created_date DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE IF NOT EXISTS 'cart_product'
(
   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   cart_id INTEGER NOT NULL,
   product_id INTEGER NOT NULL,
   quantity INTEGER NOT NULL,
   FOREIGN KEY (cart_id) REFERENCES cart(id),
   FOREIGN KEY (product_id) REFERENCES product(id),
   UNIQUE(product_id, cart_id)
);

CREATE TABLE IF NOT EXISTS 'category'
(
   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS 'product'
(
   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   name VARCHAR(255) NOT NULL,
   price NUMBER NOT NULL,
   active BOOLEAN NOT NULL,
   created_date DATETIME NOT NULL,
   category_id INTEGER NOT NULL,
   description TEXT NOT NULL,
   short_description VARCHAR (80) NOT NULL,
   FOREIGN KEY (category_id) REFERENCES category(id)
);

CREATE TABLE IF NOT EXISTS 'product_image'
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    url VARCHAR(500) NOT NULL,
    product_id INTEGER NOT NULL,
    priority INTEGER,
    FOREIGN KEY (product_id) REFERENCES product(id)
);

CREATE TABLE IF NOT EXISTS 'oder_product'
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    orders_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY(orders_id) REFERENCES oders(id)
    FOREIGN KEY(product_id) REFERENCES product(id)
);
