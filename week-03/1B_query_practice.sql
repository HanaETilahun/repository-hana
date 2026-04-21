USE northwind;
/* List product id, product name, and unit price */
SELECT ProductID, ProductName, UnitPrice
FROM Products;
/* Products where unit price is $7.50 or less */

SELECT ProductID, ProductName, UnitPrice
FROM Products
WHERE UnitPrice <= 7.50;

/* Products with 0 units in stock but on backorder */
SELECT ProductID, ProductName, UnitsInStock, UnitsOnOrder
FROM Products
WHERE UnitsInStock = 0
AND UnitsOnOrder > 0;
/*How products identify their category
 The Products table uses a column called CategoryID
This is a foreign key that links to the Categories table.
Where to find all categories
 In the Categories table
It contains:
CategoryID
CategoryName
Description*/
SELECT * 
FROM Products;
SELECT * 
FROM Categories;

SELECT p.ProductID, p.ProductName, p.UnitPrice, c.CategoryName
FROM Products p
JOIN Categories c
ON p.CategoryID = c.CategoryID;

/*List OF all Seafood products*/
SELECT p.ProductID, p.ProductName, p.UnitPrice, c.CategoryName
FROM Products p
JOIN Categories c
ON p.CategoryID = c.CategoryID
WHERE c.CategoryName = 'Seafood';

/*Examine the products table again. How do you know what supplier each product comes from? Where can you find info on suppliers? Write a set of queries to find thespecific identifier for "Tokyo Traders" and then find all products from that supplier.*/
SELECT SupplierID, CompanyName
FROM Suppliers
WHERE CompanyName = 'Tokyo Traders'

SELECT ProductID, ProductName, UnitPrice, SupplierID
FROM Products
WHERE SupplierID = (
    SELECT SupplierID
    FROM Suppliers
    WHERE CompanyName = 'Tokyo Traders'
);
/*Products use SupplierID to identify suppliers, and supplier details are stored in the Suppliers table.*/


/*ow many employees work at northwind? What employees have "manager"somewhere in their job title? Write queries to answer each question.*/

SELECT COUNT(*) AS TotalEmployees
FROM Employees;
/*There are 9 employees from employees table */

