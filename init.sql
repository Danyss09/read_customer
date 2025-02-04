CREATE DATABASE CustomerCreateDb;
use CustomerCreateDb;
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100) UNIQUE,
    PhoneNumber VARCHAR(15),
    Address VARCHAR(200),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
INSERT INTO Customers (FirstName, LastName, Email, PhoneNumber, Address)
VALUES
('John', 'Doe', 'john.doe@example.com', '1234567890', '1234 Elm St'),
('Jane', 'Smith', 'jane.smith@example.com', '0987654321', '5678 Oak Ave');