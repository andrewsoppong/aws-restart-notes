# Creating Tables and Using Data Types in Databases

## What You Will Learn

At the core of this lesson, you will learn how to:

- Describe how to create a new table in a database
- Describe how to use data types when creating a table

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Understand the structure of relational database tables
- Use SQL commands to create database tables
- Identify different SQL language categories
- Apply appropriate data types to database columns
- Understand the importance of primary keys and foreign keys
- Create relationships between tables
- Design well-structured database tables

---

# Introduction to Database Tables

A database table stores related information in rows and columns.

Tables help organize data efficiently and make it easier to:

- Store records
- Retrieve information
- Update data
- Delete data
- Maintain relationships between data

Example table:

| StudentID | Name | Age |
|---|---|---|
| 101 | Andrews | 20 |
| 102 | Linda | 22 |

---

# Structure of a Table

A database table contains:

| Component | Description |
|---|---|
| Row | A single record |
| Column | A field containing a data type |
| Table | Collection of related records |
| Key | Identifier used to manage relationships |

---

# Relational Databases

Relational databases organize data into tables that are related to each other.

Examples include:

- MySQL
- PostgreSQL
- Oracle Database
- Microsoft SQL Server
- SQLite

Relational databases commonly use SQL for database management.

---

# Structured Query Language (SQL)

SQL stands for:

```text
Structured Query Language
```

SQL is the standard language used to interact with relational databases.

SQL is used to:

- Create tables
- Insert data
- Retrieve data
- Update data
- Delete data
- Manage permissions

---

# Categories of SQL Commands

SQL commands are grouped into categories:

| Category | Meaning |
|---|---|
| DML | Data Manipulation Language |
| DDL | Data Definition Language |
| DCL | Data Control Language |

---

# Data Manipulation Language (DML)

DML commands manipulate data inside database tables.

Common DML commands include:

| Command | Purpose |
|---|---|
| INSERT | Add new records |
| UPDATE | Modify existing records |
| DELETE | Remove records |
| SELECT | Retrieve records |

---

# Example: SELECT Statement

```sql
SELECT * FROM Students;
```

This retrieves all records from the `Students` table.

---

# Example: INSERT Statement

```sql
INSERT INTO Students
(StudentID, FirstName, LastName, Age)

VALUES
(1, 'Andrews', 'Oppong', 20);
```

This inserts a new student record.

---

# Example: UPDATE Statement

```sql
UPDATE Students
SET Age = 21
WHERE StudentID = 1;
```

This updates a student's age.

---

# Example: DELETE Statement

```sql
DELETE FROM Students
WHERE StudentID = 1;
```

This removes a student record.

---

# Data Definition Language (DDL)

DDL commands define and manage database structures.

Common DDL commands include:

| Command | Purpose |
|---|---|
| CREATE | Create database objects |
| ALTER | Modify database objects |
| DROP | Delete database objects |
| TRUNCATE | Remove all table records |

---

# Example: CREATE TABLE

```sql
CREATE TABLE Students (

    StudentID INT,

    FirstName VARCHAR(50),

    LastName VARCHAR(50),

    Age INT

);
```

---

# Example: ALTER TABLE

```sql
ALTER TABLE Students
ADD Email VARCHAR(100);
```

Adds a new column to the table.

---

# Example: DROP TABLE

```sql
DROP TABLE Students;
```

Deletes the table completely.

---

# Data Control Language (DCL)

DCL commands manage database permissions and security.

Common DCL commands include:

| Command | Purpose |
|---|---|
| GRANT | Gives permissions |
| REVOKE | Removes permissions |

---

# Example: GRANT Permission

```sql
GRANT SELECT ON Students TO user1;
```

Allows `user1` to read records from the table.

---

# Example: REVOKE Permission

```sql
REVOKE SELECT ON Students FROM user1;
```

Removes permission from the user.

---

# Creating a New Table

Tables are created using the `CREATE TABLE` statement.

Basic syntax:

```sql
CREATE TABLE table_name (

    column1 datatype,

    column2 datatype,

    column3 datatype

);
```

---

# Example: Creating a Students Table

```sql
CREATE TABLE Students (

    StudentID INT PRIMARY KEY,

    FirstName VARCHAR(50),

    LastName VARCHAR(50),

    Age INT,

    Email VARCHAR(100)

);
```

---

# Understanding Data Types

Data types define the kind of data stored in a column.

Choosing the correct data type helps:

- Improve database performance
- Maintain data accuracy
- Reduce storage usage
- Prevent invalid entries

---

# Categories of Data Types

Common categories include:

- Numeric data types
- Character string types
- Date and time types
- Boolean data types

---

# Numeric Data Types

Numeric data types store numbers.

Examples:

| Data Type | Description |
|---|---|
| INT | Whole numbers |
| FLOAT | Decimal values |
| DECIMAL | Exact decimal values |
| BIGINT | Large whole numbers |

---

# Example: Numeric Data Types

```sql
Age INT,
Salary DECIMAL(10,2)
```

---

# Character String Types

Character string types store text information.

Examples:

| Data Type | Description |
|---|---|
| CHAR | Fixed-length text |
| VARCHAR | Variable-length text |
| TEXT | Large text content |

---

# Example: Character String Types

```sql
FirstName VARCHAR(50),
Description TEXT
```

---

# Date and Time Data Types

Date and time types store temporal information.

Examples:

| Data Type | Description |
|---|---|
| DATE | Stores dates |
| TIME | Stores time |
| DATETIME | Stores date and time |

---

# Example: Date Data Type

```sql
DateOfBirth DATE
```

---

# Boolean Data Types

Boolean types store true or false values.

Example:

```sql
IsActive BOOLEAN
```

---

# Primary Key (PK)

A primary key uniquely identifies each record in a table.

Characteristics:

- Must contain unique values
- Cannot contain NULL values
- Only one primary key per table

---

# Example: Primary Key

```sql
StudentID INT PRIMARY KEY
```

---

# Importance of Primary Keys

Primary keys help:

- Prevent duplicate records
- Identify records uniquely
- Improve data integrity
- Support table relationships

---

# Foreign Key (FK)

A foreign key creates a relationship between two tables.

A foreign key references the primary key in another table.

---

# Example Tables

## Students Table

| StudentID | Name |
|---|---|
| 1 | Andrews |

---

## Courses Table

| CourseID | StudentID |
|---|---|
| 101 | 1 |

In this example:

- `StudentID` in `Students` is the primary key
- `StudentID` in `Courses` is the foreign key

---

# Example: Creating Tables with Foreign Keys

```sql
CREATE TABLE Students (

    StudentID INT PRIMARY KEY,

    Name VARCHAR(50)

);

CREATE TABLE Courses (

    CourseID INT PRIMARY KEY,

    StudentID INT,

    CourseName VARCHAR(100),

    FOREIGN KEY (StudentID)
    REFERENCES Students(StudentID)

);
```

---

# Benefits of Foreign Keys

Foreign keys help:

- Maintain relationships between tables
- Improve consistency
- Prevent invalid references
- Support relational database design

---

# Well-Designed Database Characteristics

A good database design should:

- Avoid duplicate data
- Use meaningful names
- Use correct data types
- Include proper keys
- Maintain relationships efficiently
- Improve query performance

---

# Database Relationships

Common relationship types include:

| Relationship | Description |
|---|---|
| One-to-One | One record matches one record |
| One-to-Many | One record matches many records |
| Many-to-Many | Multiple records match multiple records |

---

# Example: One-to-Many Relationship

One customer can place many orders.

## Customers Table

| CustomerID | CustomerName |
|---|---|
| 1 | Andrews |

---

## Orders Table

| OrderID | CustomerID |
|---|---|
| 1001 | 1 |
| 1002 | 1 |

---

# Common SQL Errors

| Error | Cause |
|---|---|
| Syntax Error | Incorrect SQL formatting |
| Duplicate Key Error | Repeated primary key |
| NULL Constraint Error | Missing required data |
| Foreign Key Constraint Error | Invalid relationship reference |

---

# Best Practices for Table Creation

- Use descriptive table names
- Use descriptive column names
- Select proper data types
- Use primary keys
- Use foreign keys carefully
- Normalize data when appropriate

---

# SQL Table Creation Workflow

1. Plan the database structure
2. Define table names
3. Define columns
4. Choose data types
5. Assign primary keys
6. Create relationships
7. Test queries

---

# Example Complete Database Workflow

## Step 1: Create Table

```sql
CREATE TABLE Employees (

    EmployeeID INT PRIMARY KEY,

    FirstName VARCHAR(50),

    LastName VARCHAR(50),

    Salary DECIMAL(10,2)

);
```

---

## Step 2: Insert Data

```sql
INSERT INTO Employees
VALUES
(1, 'Andrews', 'Oppong', 5000.00);
```

---

## Step 3: Retrieve Data

```sql
SELECT * FROM Employees;
```

---

# Advantages of Relational Databases

- Organized data storage
- Strong relationships
- Data consistency
- Efficient querying
- Reliable transactions
- Better security

---

# Key Terms

| Term | Meaning |
|------|---------|
| DML | Commands used to manipulate data |
| DDL | Commands used to define structures |
| DCL | Commands used to control permissions |
| Data Type | Defines the type of stored data |
| Numeric Data Type | Stores numbers |
| Character String Type | Stores text |
| Primary Key (PK) | Unique identifier for records |
| Foreign Key (FK) | Creates relationships between tables |

---

# Review Questions

1. What is the purpose of a database table?
2. What is the difference between DML and DDL?
3. Why are data types important?
4. What is the purpose of a primary key?
5. What is the purpose of a foreign key?
6. What are the benefits of relational databases?

---

# Additional Resources

SQL Tutorial:

```text
https://www.w3schools.com/sql/
```

MySQL Documentation:

```text
https://dev.mysql.com/doc/
```

PostgreSQL Documentation:

```text
https://www.postgresql.org/docs/
```

---

# Summary

Database tables organize related information into rows and columns. SQL provides commands for defining structures, manipulating data, and controlling access. Data types ensure information is stored correctly, while primary keys and foreign keys help maintain relationships and data integrity in relational databases.