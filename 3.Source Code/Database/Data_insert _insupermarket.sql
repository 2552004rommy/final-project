DECLARE @i INT;

-- Fake Data Lists
DECLARE @FirstNames TABLE (Name NVARCHAR(50));
INSERT INTO @FirstNames VALUES ('John'), ('Jane'), ('Michael'), ('Sarah'), ('David'), ('Emily'), ('James'), ('Jessica'), ('Chris'), ('Ashley');

DECLARE @LastNames TABLE (Name NVARCHAR(50));
INSERT INTO @LastNames VALUES ('Smith'), ('Johnson'), ('Williams'), ('Brown'), ('Jones'), ('Garcia'), ('Miller'), ('Davis'), ('Rodriguez'), ('Martinez');

DECLARE @Categories TABLE (Category NVARCHAR(50));
INSERT INTO @Categories VALUES ('Electronics'), ('Clothing'), ('Toys'), ('Books'), ('Furniture'), ('Beauty'), ('Sports'), ('Automotive'), ('Music'), ('Grocery');

DECLARE @Branches TABLE (BranchName NVARCHAR(50));
INSERT INTO @Branches VALUES ('North Branch'), ('East Branch'), ('West Branch'), ('South Branch'), ('Central Branch'), ('Downtown Branch'), ('Suburban Branch'), ('Uptown Branch'), ('Tech Branch'), ('Retail Branch');

DECLARE @Departments TABLE (DeptName NVARCHAR(50));
INSERT INTO @Departments VALUES ('HR'), ('Finance'), ('Sales'), ('Marketing'), ('IT'), ('R&D'), ('Operations'), ('Logistics'), ('Legal'), ('Procurement');

DECLARE @Addresses TABLE (Address NVARCHAR(100));
INSERT INTO @Addresses VALUES ('123 Elm St'), ('456 Oak St'), ('789 Maple Ave'), ('101 Pine Ln'), ('202 Cedar Blvd'), ('303 Birch Rd'), ('404 Walnut Dr'), ('505 Ash Cir'), ('606 Cherry Ct'), ('707 Poplar St');

-- Balanced Suppliers (500 to 600 suppliers)
SET @i = 1;
DECLARE @randomSuppliers INT = (ABS(CHECKSUM(NEWID())) % 101) + 500; -- Random number between 500 and 600
WHILE @i <= @randomSuppliers
BEGIN
    INSERT INTO Suppliers (ID, NAME, Contact)
    VALUES (@i, CONCAT('Supplier ', (SELECT TOP 1 Name FROM @LastNames ORDER BY NEWID())), CONCAT('123-456-', RIGHT('000' + CAST(@i AS VARCHAR(3)), 3)));
    SET @i = @i + 1;
END;

-- Balanced Departments (500 departments with fake names)
SET @i = 1;
WHILE @i <= 500
BEGIN
    INSERT INTO Departments (ID, NAME, Budget, Head, Location, Contact, Creation_Date)
    VALUES (@i, (SELECT TOP 1 DeptName FROM @Departments ORDER BY NEWID()), 50000 + (@i * 1000) + (ABS(CHECKSUM(NEWID())) % 50000), CONCAT('Head ', @i), (SELECT TOP 1 Address FROM @Addresses ORDER BY NEWID()), CONCAT('111-111-', RIGHT('000' + CAST(@i AS VARCHAR(3)), 3)), DATEADD(DAY, -(ABS(CHECKSUM(NEWID())) % 365), GETDATE()));
    SET @i = @i + 1;
END;

-- Unbalanced Branches (500 to 550 branches with fake names)
SET @i = 1;
DECLARE @randomBranches INT = (ABS(CHECKSUM(NEWID())) % 51) + 500; -- Random number between 500 and 550
WHILE @i <= @randomBranches
BEGIN
    INSERT INTO Branches (ID, NAME, Contact, Location, Opening_Hours, Staff_Count)
    VALUES (@i, (SELECT TOP 1 BranchName FROM @Branches ORDER BY NEWID()), CONCAT('111-111-', RIGHT('000' + CAST(@i AS VARCHAR(3)), 3)), (SELECT TOP 1 Address FROM @Addresses ORDER BY NEWID()), CASE WHEN @i % 2 = 0 THEN '8AM - 4PM' ELSE '10AM - 6PM' END, 5 + (ABS(CHECKSUM(NEWID())) % 20));
    SET @i = @i + 1;
END;

-- Unbalanced Customers (550 to 600 customers with fake names)
SET @i = 1;
DECLARE @randomCustomers INT = (ABS(CHECKSUM(NEWID())) % 51) + 550; -- Random number between 550 and 600
WHILE @i <= @randomCustomers
BEGIN
    INSERT INTO Customer (id, name, mobile, Membership_status, Gender, Age, addres, Feedback)
    VALUES (@i, CONCAT((SELECT TOP 1 Name FROM @FirstNames ORDER BY NEWID()), ' ', (SELECT TOP 1 Name FROM @LastNames ORDER BY NEWID())), CONCAT('111111', RIGHT('0000' + CAST(@i AS VARCHAR(4)), 4)), CASE WHEN @i % 3 = 0 THEN 'Active' ELSE 'Inactive' END, CASE WHEN @i % 2 = 0 THEN 'M' ELSE 'F' END, 18 + (ABS(CHECKSUM(NEWID())) % 60), (SELECT TOP 1 Address FROM @Addresses ORDER BY NEWID()), 'Feedback text');
    SET @i = @i + 1;
END;

-- Balanced Products (500 products with fake categories)
SET @i = 1;
WHILE @i <= 500
BEGIN
    INSERT INTO Products (ID, NAME, Category, Brand, Weight, Description, Expiry_Date)
    VALUES (@i, CONCAT('Product ', @i), (SELECT TOP 1 Category FROM @Categories ORDER BY NEWID()), CONCAT('Brand ', CHAR(64 + @i % 26)), @i % 5 + 1.0, 'Description text', DATEADD(DAY, ABS(CHECKSUM(NEWID())) % 365, GETDATE()));
    SET @i = @i + 1;
END;

-- Balanced Delivery (500 deliveries with fake addresses)
SET @i = 1;
WHILE @i <= 500
BEGIN
    INSERT INTO Delivery (ID, Delivery_Date, Cost_OF_SERVICES, Address, Status)
    VALUES (@i, DATEADD(DAY, @i, GETDATE()), 50.00 + (@i % 50), (SELECT TOP 1 Address FROM @Addresses ORDER BY NEWID()), CASE WHEN @i % 2 = 0 THEN 'Delivered' ELSE 'Pending' END);
    SET @i = @i + 1;
END;

-- Balanced STOCKS (500 stocks)
SET @i = 1;
WHILE @i <= 500
BEGIN
    INSERT INTO STOCKS (ID, ProductInventory, proudect_id, Branch_id, Avaliable_Quantity)
    VALUES (@i, 100 + (@i % 100), @i, @i, 80 + (@i % 40));
    SET @i = @i + 1;
END;

-- Unbalanced Employees (550 to 600 employees with fake names)
SET @i = 1;
DECLARE @randomEmployees INT = (ABS(CHECKSUM(NEWID())) % 51) + 550; -- Random number between 550 and 600
WHILE @i <= @randomEmployees
BEGIN
    INSERT INTO Employees (ID, F_name, L_name, Salary, Age, Address, Work_hours, Marital_status, ratings, Number, Branch_id, Department_id)
    VALUES (@i, (SELECT TOP 1 Name FROM @FirstNames ORDER BY NEWID()), (SELECT TOP 1 Name FROM @LastNames ORDER BY NEWID()), 50000 + (@i * 100), 20 + (@i % 50), (SELECT TOP 1 Address FROM @Addresses ORDER BY NEWID()), 40 + (@i % 10), CASE WHEN @i % 2 = 0 THEN 'Married' ELSE 'Single' END, 3.0 + (@i % 2), CONCAT('111-111-', RIGHT('000' + CAST(@i AS VARCHAR(3)), 3)), @i % 10 + 1, @i % 10 + 1);
    SET @i = @i + 1;
END;

-- Unbalanced Promotions (550 to 600 promotions)
SET @i = 1;
DECLARE @randomPromotions INT = (ABS(CHECKSUM(NEWID())) % 51) + 550; -- Random number between 550 and 600
WHILE @i <= @randomPromotions
BEGIN
    INSERT INTO promotions (ID, NAME, Description, StartDate, EndDate, Percentage)
    VALUES (@i, CONCAT('Promotion ', CHAR(64 + @i % 26)), 'Description text', DATEADD(DAY, @i, GETDATE()), DATEADD(DAY, @i + 10, GETDATE()), @i % 50 + 5);
    SET @i = @i + 1;
END;

-- Balanced Payment (500 payments with fake billing addresses)
SET @i = 1;
WHILE @i <= 500
BEGIN
    INSERT INTO Payment (Billing_Address, Method, Transaction_ID, Payment_Status, CUSTOMER_ID, EMPLOYEES_ID, Suppliery_id)
    VALUES ((SELECT TOP 1 Address FROM @Addresses ORDER BY NEWID()), CASE WHEN @i % 3 = 0 THEN 'Cash' WHEN @i % 3 = 1 THEN 'Credit Card' ELSE 'Debit Card' END, RIGHT('0000000000' + CAST(@i AS VARCHAR(10)), 10), CASE WHEN @i % 2 = 0 THEN 'Paid' ELSE 'Pending' END, @i, @i, @i);
    SET @i = @i + 1;
END;

-- Balanced branch_manage_product (500 branch-product pairs)
SET @i = 1;
WHILE @i <= 500
BEGIN
    INSERT INTO branch_manage_product (branch_id, proudect_id)
    VALUES (@i, @i);
    SET @i = @i + 1;
END;

-- Unbalanced Orders (550 to 600 orders with fake delivery addresses)
SET @i = 1;
DECLARE @randomOrders INT = (ABS(CHECKSUM(NEWID())) % 51) + 550; -- Random number between 550 and 600
WHILE @i <= @randomOrders
BEGIN
    INSERT INTO Orders(order_id, order_Date, Delivery_Address, customer_id, Deliver_id, promotion_id)
    VALUES (@i, DATEADD(DAY, @i, GETDATE()), (SELECT TOP 1 Address FROM @Addresses ORDER BY NEWID()), @i, (ABS(CHECKSUM(NEWID())) % 120) + 1, (ABS(CHECKSUM(NEWID())) % 120) + 1);
    SET @i = @i + 1;
END;

-- Balanced order_made_proudect (500 order-product pairs)
SET @i = 1;
WHILE @i <= 500
BEGIN
    INSERT INTO order_made_proudect (proudect_id, order_id, Quantity, unit_price)
    VALUES (@i, @i, 1 + (@i % 10), 10 + (@i % 20));
    SET @i = @i + 1;
END;

-- Balanced Supplirs_supply_proudect (500 supplier-product relationships with fake product names)
SET @i = 1;
WHILE @i <= 500
BEGIN
    INSERT INTO Supplirs_supply_proudect (product_id, Supplier_id, PRODUCT, Quantity, total_cost, Uint_of_price)
    VALUES (@i, @i, CONCAT('Product ', (SELECT TOP 1 Category FROM @Categories ORDER BY NEWID())), 50 + (@i % 100), 500 + (@i * 10), 10 + (@i % 10));
    SET @i = @i + 1;
END;
