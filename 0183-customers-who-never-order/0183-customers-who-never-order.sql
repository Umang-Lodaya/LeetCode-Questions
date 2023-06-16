SELECT name as Customers FROM Customers
where id NOT IN (SELECT customerId FROM Orders);