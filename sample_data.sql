USE sales_hub;

-- =========================================
-- INSERT BRANCHES
-- =========================================

INSERT INTO branches
(branch_name, branch_admin_name)

VALUES
('Chennai', 'Arun Kumar'),
('Bangalore', 'Priya Sharma'),
('Hyderabad', 'Rahul Verma');

-- =========================================
-- INSERT USERS
-- =========================================

INSERT INTO users
(username, email, password_hash, branch_id, role)

VALUES

('superadmin',
'[superadmin@gmail.com](mailto:superadmin@gmail.com)',
'admin123',
NULL,
'Super Admin'),

('chennai_admin',
'[chennai@gmail.com](mailto:chennai@gmail.com)',
'admin123',
1,
'Admin'),

('bangalore_admin',
'[bangalore@gmail.com](mailto:bangalore@gmail.com)',
'admin123',
2,
'Admin');

-- =========================================
-- INSERT SALES
-- =========================================

INSERT INTO customer_sales
(branch_id,
sale_date,
customer_name,
mobile_number,
product_name,
gross_sales,
received_amount,
status)

VALUES

(1,
'2026-05-28',
'Vijay',
'9876543210',
'Data Science',
50000,
20000,
'Open'),

(2,
'2026-05-28',
'Ajith',
'9876543211',
'Full Stack',
75000,
75000,
'Close'),

(3,
'2026-05-28',
'Suriya',
'9876543212',
'AI & ML',
60000,
10000,
'Open');

-- =========================================
-- INSERT PAYMENT SPLITS
-- =========================================

INSERT INTO payment_splits
(sale_id,
payment_date,
amount_paid,
payment_method)

VALUES

(1,
'2026-05-28',
10000,
'UPI'),

(1,
'2026-05-28',
10000,
'Cash'),

(2,
'2026-05-28',
75000,
'Card'),

(3,
'2026-05-28',
10000,
'UPI');
