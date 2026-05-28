CREATE DATABASE IF NOT EXISTS sales_hub;

USE sales_hub;

-- =========================================
-- TABLE 1 : branches
-- =========================================

CREATE TABLE branches (

```
branch_id INT AUTO_INCREMENT PRIMARY KEY,

branch_name VARCHAR(100) NOT NULL,

branch_admin_name VARCHAR(100),

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
```

);

-- =========================================
-- TABLE 2 : users
-- =========================================

CREATE TABLE users (

```
user_id INT AUTO_INCREMENT PRIMARY KEY,

username VARCHAR(100) NOT NULL,

email VARCHAR(255) UNIQUE NOT NULL,

password_hash VARCHAR(255) NOT NULL,

branch_id INT,

role ENUM('Super Admin', 'Admin') NOT NULL,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

FOREIGN KEY (branch_id)
REFERENCES branches(branch_id)
```

);

-- =========================================
-- TABLE 3 : customer_sales
-- =========================================

CREATE TABLE customer_sales (

```
sale_id INT AUTO_INCREMENT PRIMARY KEY,

branch_id INT NOT NULL,

sale_date DATE NOT NULL,

customer_name VARCHAR(100) NOT NULL,

mobile_number VARCHAR(15) UNIQUE NOT NULL,

product_name VARCHAR(30) NOT NULL,

gross_sales DECIMAL(12,2) NOT NULL,

received_amount DECIMAL(12,2) DEFAULT 0,



pending_amount DECIMAL(12,2)

GENERATED ALWAYS AS

(gross_sales - received_amount) STORED,



status ENUM('Open','Close') DEFAULT 'Open',

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,



FOREIGN KEY (branch_id)

REFERENCES branches(branch_id)
```

);

-- =========================================
-- TABLE 4 : payment_splits
-- =========================================

CREATE TABLE payment_splits (

```
payment_id INT AUTO_INCREMENT PRIMARY KEY,

sale_id INT NOT NULL,

payment_date DATE NOT NULL,

amount_paid DECIMAL(12,2) NOT NULL,

payment_method VARCHAR(50) NOT NULL,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,



FOREIGN KEY (sale_id)

REFERENCES customer_sales(sale_id)
```

);
