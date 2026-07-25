# Importing CSV Files and Inserting Data into Database Tables

## What You Will Learn

At the core of this lesson, you will learn how to:

- Import a comma-separated values (`.csv`) file into a table
- List common reasons for cleaning data before importing it into a database
- Insert rows into an existing table

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Understand the purpose of CSV files
- Import CSV data into database tables
- Clean and prepare data before importing
- Use SQL INSERT statements
- Understand NULL values
- Describe table structures using SQL commands

---

# Introduction to Data Importing

Databases often receive data from external sources.

Common sources include:

- CSV files
- Excel spreadsheets
- Web applications
- APIs
- Other databases

Before importing data, it is important to ensure the data is:

- Correct
- Complete
- Consistent
- Properly formatted

---

# What is a CSV File?

CSV stands for:

```text
Comma-Separated Values
```

A CSV file stores data in plain text format where values are separated by commas.

Example CSV file:

```csv
StudentID,FirstName,LastName,Age
1,Andrews,Oppong,20
2,Linda,Mensah,22
```

---

# Advantages of CSV Files

CSV files are widely used because they are:

- Simple
- Lightweight
- Easy to read
- Supported by many applications
- Easy to transfer between systems

---

# Importing CSV Files into a Database

Importing CSV data allows databases to quickly load large amounts of information.

Typical import process:

1. Create a database table
2. Prepare and clean the CSV file
3. Import the CSV data
4. Verify imported records

---

# Example Table Creation

Before importing data, a table must already exist.

Example:

```sql
CREATE TABLE Students (

    StudentID INT PRIMARY KEY,

    FirstName VARCHAR(50),

    LastName VARCHAR(50),

    Age INT

);
```

---

# Common Reasons for Cleaning Data

Data cleaning improves data quality before importing.

Common reasons include:

| Reason | Description |
|---|---|
| Remove duplicates | Prevent repeated records |
| Fix spelling errors | Improve consistency |
| Standardize formats | Ensure consistent formatting |
| Handle missing values | Prevent incomplete data |
| Remove invalid entries | Improve data integrity |

---

# Examples of Dirty Data

| Problem | Example |
|---|---|
| Duplicate records | Same student entered twice |
| Missing values | Blank age field |
| Inconsistent formatting | "USA" vs "U.S.A." |
| Typographical errors | "Andrwes" instead of "Andrews" |

---

# Benefits of Data Cleaning

Data cleaning helps:

- Improve database accuracy
- Increase consistency
- Reduce errors
- Improve reporting
- Support better decision-making

---

# SQL INSERT INTO Statement

The `INSERT INTO` statement adds records to an existing table.

Basic syntax:

```sql
INSERT INTO table_name
(column1, column2, column3)

VALUES
(value1, value2, value3);
```

---

# Example: Insert a Record

```sql
INSERT INTO Students
(StudentID, FirstName, LastName, Age)

VALUES
(1, 'Andrews', 'Oppong', 20);
```

---

# Inserting Multiple Rows

Multiple records can be inserted at once.

Example:

```sql
INSERT INTO Students
(StudentID, FirstName, LastName, Age)

VALUES
(1, 'Andrews', 'Oppong', 20),
(2, 'Linda', 'Mensah', 22),
(3, 'Kofi', 'Asare', 19);
```

---

# Verifying Inserted Data

Use the `SELECT` statement to verify records.

Example:

```sql
SELECT * FROM Students;
```

---

# DESCRIBE Statement

The `DESCRIBE` statement displays a table structure.

Basic syntax:

```sql
DESCRIBE table_name;
```

---

# Example: DESCRIBE Table

```sql
DESCRIBE Students;
```

---

# Information Displayed by DESCRIBE

The `DESCRIBE` command shows:

- Column names
- Data types
- NULL settings
- Keys
- Default values

Example output:

| Field | Type | Null | Key |
|---|---|---|---|
| StudentID | int | NO | PRI |
| FirstName | varchar(50) | YES | |
| Age | int | YES | |

---

# NULL Values

A `NULL` value represents missing or unknown data.

Important:

```text
NULL is not the same as zero or an empty string.
```

---

# Example of NULL Values

| StudentID | Name | Email |
|---|---|---|
| 1 | Andrews | NULL |

This means the email value is unknown or missing.

---

# Inserting NULL Values

Example:

```sql
INSERT INTO Students
(StudentID, FirstName, LastName, Age)

VALUES
(4, 'Ama', 'Boateng', NULL);
```

---

# Why NULL Values Matter

NULL values help databases represent:

- Missing information
- Unknown values
- Optional fields

---

# Importing CSV Data in MySQL

MySQL can import CSV files using:

```sql
LOAD DATA INFILE
```

---

# Example CSV Import

```sql
LOAD DATA INFILE '/path/students.csv'

INTO TABLE Students

FIELDS TERMINATED BY ','

LINES TERMINATED BY '\n'

IGNORE 1 ROWS;
```

---

# Explanation of Import Options

| Option | Purpose |
|---|---|
| FIELDS TERMINATED BY ',' | Values separated by commas |
| LINES TERMINATED BY '\n' | New line for each record |
| IGNORE 1 ROWS | Skips CSV header row |

---

# Example CSV File

```csv
StudentID,FirstName,LastName,Age
1,Andrews,Oppong,20
2,Linda,Mensah,22
3,Kofi,Asare,19
```

---

# Checking Imported Data

After importing, verify records:

```sql
SELECT * FROM Students;
```

---

# Common Data Import Errors

| Error | Cause |
|---|---|
| Duplicate entry | Repeated primary key |
| Incorrect data type | Invalid values |
| Missing columns | CSV format mismatch |
| NULL constraint error | Missing required values |
| File not found | Incorrect file path |

---

# Best Practices for Data Importing

- Clean data before importing
- Verify table structure
- Use correct data types
- Backup important databases
- Validate imported records

---

# SQL Commands Used

| Command | Purpose |
|---|---|
| INSERT INTO | Adds records |
| SELECT | Retrieves records |
| DESCRIBE | Displays table structure |
| LOAD DATA INFILE | Imports CSV data |

---

# Database Concepts

---

# Table

A table stores related records in rows and columns.

---

# Record

A record is a single row of data.

---

# Field

A field is a single column in a table.

---

# Schema

A schema defines the structure of a table.

---

# Primary Key

A primary key uniquely identifies each record.

---

# Example Complete Workflow

---

# Step 1: Create Table

```sql
CREATE TABLE Employees (

    EmployeeID INT PRIMARY KEY,

    FirstName VARCHAR(50),

    LastName VARCHAR(50),

    Salary DECIMAL(10,2)

);
```

---

# Step 2: Import CSV Data

```sql
LOAD DATA INFILE '/path/employees.csv'

INTO TABLE Employees

FIELDS TERMINATED BY ','

LINES TERMINATED BY '\n'

IGNORE 1 ROWS;
```

---

# Step 3: Verify Records

```sql
SELECT * FROM Employees;
```

---

# Advantages of Importing CSV Files

- Faster bulk data loading
- Easy data migration
- Improved productivity
- Compatible with many systems

---

# Key Terms

| Term | Meaning |
|------|---------|
| INSERT INTO Statement | SQL command used to insert records |
| DESCRIBE Statement | SQL command used to display table structure |
| NULL Value | Represents missing or unknown data |
| CSV File | Comma-separated values file |

---

# Review Questions

1. What does CSV stand for?
2. Why is data cleaning important?
3. What is the purpose of the INSERT INTO statement?
4. What information does DESCRIBE provide?
5. What is a NULL value?
6. Why should imported data be verified?

---

# Additional Resources

MySQL Documentation:

```text
https://dev.mysql.com/doc/
```

SQL Tutorial:

```text
https://www.w3schools.com/sql/
```

CSV File Format Reference:

```text
https://datatracker.ietf.org/doc/html/rfc4180
```

---

# Summary

CSV files provide a simple way to transfer and import data into relational databases. Before importing, data should be cleaned to improve consistency and accuracy. SQL commands such as INSERT INTO, DESCRIBE, and LOAD DATA INFILE help users manage and verify imported data efficiently.