CREATE TABLE Customer (
    customer_id INTEGER NOT NULL PRIMARY KEY autoincrement,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    address TEXT NOT NULL,
    phone_number TEXT NOT NULL
);


CREATE TABLE `Order` (
    order_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    payment_option_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
    FOREIGN KEY (payment_option_id) REFERENCES PaymentOption(payment_option_id)
);


CREATE TABLE Product (
    product_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price TEXT NOT NULL
);

CREATE TABLE PaymentOption (
    payment_option_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    account_number TEXT NOT NULL,
    customer_id INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);


CREATE TABLE OrderProduct (
    order_product_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES `Order`(order_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);


INSERT INTO Product VALUES (null, 'Desk', '125.50');
INSERT INTO Product VALUES (null, 'Pen', '1.50');
INSERT INTO Product VALUES (null, 'Notebook', '12.50');
INSERT INTO Product VALUES (null, 'Computer', '1825.50');

DROP TABLE ORDERPRODUCT
DROP TABLE PAYMENTOPTION
DROP TABLE CUSTOMER
DROP TABLE PRODUCT
DROP TABLE `ORDER`
