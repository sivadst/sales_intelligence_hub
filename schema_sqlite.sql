CREATE TABLE IF NOT EXISTS branches (
    branch_id INTEGER PRIMARY KEY AUTOINCREMENT,
    branch_name TEXT NOT NULL,
    branch_admin_name TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    branch_id INTEGER,
    role TEXT NOT NULL CHECK(role IN ('Super Admin', 'Admin')),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (branch_id) REFERENCES branches(branch_id)
);

CREATE TABLE IF NOT EXISTS customer_sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    branch_id INTEGER NOT NULL,
    sale_date DATE NOT NULL,
    customer_name TEXT NOT NULL,
    mobile_number TEXT NOT NULL,
    product_name TEXT NOT NULL,
    gross_sales REAL NOT NULL,
    received_amount REAL DEFAULT 0,
    pending_amount REAL GENERATED ALWAYS AS (gross_sales - received_amount) STORED,
    status TEXT DEFAULT 'Open' CHECK(status IN ('Open', 'Close')),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (branch_id) REFERENCES branches(branch_id)
);

CREATE TABLE IF NOT EXISTS payment_splits (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sale_id INTEGER NOT NULL,
    payment_date DATE NOT NULL,
    amount_paid REAL NOT NULL,
    payment_method TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sale_id) REFERENCES customer_sales(sale_id)
);

CREATE TRIGGER IF NOT EXISTS update_received_amount
AFTER INSERT ON payment_splits
FOR EACH ROW
BEGIN
    UPDATE customer_sales
    SET received_amount = (
        SELECT COALESCE(SUM(amount_paid), 0)
        FROM payment_splits
        WHERE sale_id = NEW.sale_id
    )
    WHERE sale_id = NEW.sale_id;
END;
