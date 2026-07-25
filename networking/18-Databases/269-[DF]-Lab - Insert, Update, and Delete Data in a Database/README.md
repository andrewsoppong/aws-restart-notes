# AWS Lab: Insert, Update, Delete, and Import Data in a Database

## Scenario

The database operations team has created a relational database named:

```text
world
```

The database contains three tables:

- city
- country
- countrylanguage

Your task is to validate the database configuration by running SQL statements that:

- Insert data
- Update data
- Delete data
- Import data from a backup file

---

# Lab Overview and Objectives

This lab demonstrates how to manipulate data using Structured Query Language (SQL).

After completing this lab, you will be able to:

- Insert rows into a table
- Update rows in a table
- Delete rows from a table
- Import rows from a database backup file

---

# Existing Resources

The following resources are already created:

- A Command Host EC2 instance
- A MySQL database named `world`
- Three tables:
  - city
  - country
  - countrylanguage

---

# Lab Architecture

A lab user connects to a database instance using a Command Host and performs SQL operations on the `world` database.

Operations include:

- INSERT
- UPDATE
- DELETE
- IMPORT

---

# Sample Data Source

Sample data used in this lab is based on:

```text
Statistics Finland, general regional statistics, February 4, 2022
```

---

# Estimated Duration

Approximately:

```text
45 minutes
```

---

# AWS Service Restrictions

In this lab environment:

- Access may be restricted to only required AWS services
- Other AWS services may generate access errors

---

# Accessing the AWS Management Console

---

# Step 1: Start the Lab

Choose:

```text
Start Lab
```

---

# Lab Status Indicators

| Color | Meaning |
|---|---|
| Red | Lab not started |
| Yellow | Lab starting |
| Green | Lab ready |

Wait for the green status before continuing.

---

# Step 2: Open AWS Console

Choose the green AWS icon to open the AWS Management Console.

---

# Important Notes

- Do not change the AWS Region unless instructed
- Allow pop-ups if blocked by your browser

---

# Task 1: Connect to a Database

In this task, you connect to the Command Host instance.

---

# Step 1: Open EC2

In AWS Management Console:

```text
Services → Compute → EC2
```

---

# Step 2: Open Instances

In the left navigation pane:

```text
Instances
```

---

# Step 3: Connect to Command Host

1. Locate:

```text
Command Host
```

2. Select the checkbox
3. Choose:

```text
Connect
```

---

# Step 4: Use Session Manager

Choose the:

```text
Session Manager
```

tab.

Then choose:

```text
Connect
```

---

# Step 5: Configure the Terminal

Run:

```bash
sudo su
cd /home/ec2-user/
```

---

# Linux Command Explanation

| Command | Purpose |
|---|---|
| sudo su | Become root user |
| cd | Change directory |

---

# Step 6: Connect to MySQL

Run:

```bash
mysql -u root --password='re:St@rt!9'
```

---

# MySQL Command-Line Client

The MySQL command-line client is an SQL shell used to interact with databases.

---

# MySQL Connection Switches

| Switch | Description |
|---|---|
| -u | MySQL username |
| --password | MySQL password |

---

# Reconnecting if Session Fails

If the Session Manager becomes unresponsive:

```bash
sudo su
cd /home/ec2-user/
mysql -u root --password='re:St@rt!9'
```

---

# Step 7: View Existing Databases

Run:

```sql
SHOW DATABASES;
```

Make note of available databases.

---

# Task 2: Insert Data into a Table

In this task, you insert sample rows into the `country` table.

---

# Step 1: Verify country Table Exists

Run:

```sql
SELECT * FROM world.country;
```

---

# Understanding SELECT

The `SELECT` statement retrieves data from a table.

Syntax:

```sql
SELECT * FROM table_name;
```

---

# Meaning of *

The `*` symbol means:

```text
All columns
```

---

# Step 2: Insert Data into country Table

Run:

```sql
INSERT INTO world.country VALUES
('IRL','Ireland','Europe','British Islands',70273.00,1921,3775100,76.8,75921.00,73132.00,'Ireland/Éire','Republic',1447,'IE');
```

Run:

```sql
INSERT INTO world.country VALUES
('AUS','Australia','Oceania','Australia and New Zealand',7741220.00,1901,18886000,79.8,351182.00,392911.00,'Australia','Constitutional Monarchy, Federation',135,'AU');
```

---

# INSERT INTO Statement

The `INSERT INTO` statement adds rows to a table.

Syntax:

```sql
INSERT INTO table_name VALUES (...);
```

---

# Important Note About VALUES

Values must appear in the same order as defined in the table schema.

---

# Step 3: Verify Inserted Rows

Run:

```sql
SELECT * FROM world.country
WHERE Code IN ('IRL', 'AUS');
```

---

# Expected Output

| Code | Name | Continent | Region |
|---|---|---|---|
| AUS | Australia | Oceania | Australia and New Zealand |
| IRL | Ireland | Europe | British Islands |

---

# Task 3: Update Rows in a Table

In this task, you update rows using the `UPDATE` statement.

---

# Step 1: Update Population Column

Run:

```sql
UPDATE world.country
SET Population = 0;
```

---

# Important Warning

Because no `WHERE` clause is used:

```text
ALL rows are updated.
```

---

# Understanding WHERE

The `WHERE` clause filters rows.

Example:

```sql
UPDATE table_name
SET column = value
WHERE condition;
```

---

# Step 2: Verify Update

Run:

```sql
SELECT * FROM world.country;
```

---

# Step 3: Update Multiple Columns

Run:

```sql
UPDATE world.country
SET Population = 100,
SurfaceArea = 100;
```

---

# Step 4: Verify Changes

Run:

```sql
SELECT * FROM world.country;
```

---

# UPDATE Statement

The `UPDATE` statement modifies existing records.

Syntax:

```sql
UPDATE table_name
SET column1 = value1,
column2 = value2;
```

---

# Task 4: Delete Rows from a Table

In this task, you delete rows using the `DELETE` statement.

---

# Important Warning

DELETE operations may not be reversible.

Use caution.

---

# Step 1: Disable Foreign Key Checks

Run:

```sql
SET FOREIGN_KEY_CHECKS = 0;
```

---

# Foreign Keys

Foreign keys maintain relationships between tables.

Disabling checks allows deletion without constraint errors.

---

# Step 2: Delete All Rows

Run:

```sql
DELETE FROM world.country;
```

---

# Important Note

Because no `WHERE` clause is used:

```text
ALL rows are deleted.
```

---

# Step 3: Verify Deletion

Run:

```sql
SELECT * FROM world.country;
```

The table should now be empty.

---

# DELETE Statement

The `DELETE` statement removes rows from a table.

Syntax:

```sql
DELETE FROM table_name;
```

---

# Task 5: Import Data Using an SQL File

In this task, you import data from a backup SQL file.

---

# Step 1: Exit MySQL

Run:

```sql
QUIT;
```

---

# Step 2: Verify Backup File Exists

Run:

```bash
ls /home/ec2-user/world.sql
```

---

# SQL Script Files

SQL script files contain multiple SQL statements used to:

- Create tables
- Insert data
- Restore backups

---

# Step 3: Import SQL Backup File

Run:

```bash
mysql -u root --password='re:St@rt!9' < /home/ec2-user/world.sql
```

---

# What the Backup File Does

The script:

- Creates additional tables
- Inserts rows into:
  - city
  - country
  - countrylanguage

---

# Step 4: Reconnect to MySQL

Run:

```bash
mysql -u root --password='re:St@rt!9'
```

---

# Step 5: Verify Imported Tables

Run:

```sql
USE world;
SHOW TABLES;
```

Expected tables:

- city
- country
- countrylanguage

---

# Step 6: Verify Imported Rows

Run:

```sql
SELECT * FROM country;
```

You should now see more records.

---

# Step 7: Query Other Tables

Run:

```sql
SELECT * FROM city;
```

Run:

```sql
SELECT * FROM countrylanguage;
```

---

# SQL Commands Used in This Lab

| Command | Purpose |
|---|---|
| SHOW DATABASES | Lists databases |
| SELECT | Retrieves records |
| INSERT INTO | Inserts rows |
| UPDATE | Updates rows |
| DELETE | Deletes rows |
| SHOW TABLES | Displays tables |
| USE | Selects database |
| QUIT | Exits MySQL |

---

# Data Manipulation Language (DML)

The following SQL commands are examples of DML:

| Command | Purpose |
|---|---|
| INSERT | Add data |
| UPDATE | Modify data |
| DELETE | Remove data |
| SELECT | Retrieve data |

---

# Database Concepts

---

# Row

A row is a single record in a table.

---

# Column

A column stores a specific type of data.

---

# Table

A table stores related rows and columns.

---

# Schema

A schema defines a table structure.

---

# Foreign Key

A foreign key creates relationships between tables.

---

# Common SQL Errors

| Error | Cause |
|---|---|
| Syntax Error | Incorrect SQL syntax |
| Unknown Table | Table does not exist |
| Duplicate Entry | Duplicate primary key |
| Foreign Key Constraint | Related record missing |
| Access Denied | Incorrect credentials |

---

# Best Practices

- Always verify UPDATE and DELETE queries
- Use WHERE clauses carefully
- Backup databases before major changes
- Verify imported data
- Use meaningful table structures

---

# Example Using WHERE Clause

Update one specific row:

```sql
UPDATE world.country
SET Population = 5000
WHERE Code = 'IRL';
```

Delete one specific row:

```sql
DELETE FROM world.country
WHERE Code = 'AUS';
```

---

# Lab Review Questions

1. What is the purpose of the INSERT INTO statement?
2. What happens when UPDATE is used without WHERE?
3. Why should DELETE statements be used carefully?
4. What is the purpose of importing SQL backup files?
5. Why are foreign key checks sometimes disabled?

---

# Conclusion

Congratulations! You have successfully:

- Inserted rows into a table
- Updated rows in a table
- Deleted rows from a table
- Imported rows from a database backup file

---

# Lab Complete

To finish the lab:

1. Choose:

```text
End Lab
```

2. Select:

```text
Yes
```

to confirm.

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

AWS Training and Certification:

```text
https://aws.amazon.com/training/
```

---

# Summary

In this lab, you connected to a MySQL database hosted on a Command Host instance and practiced inserting, updating, deleting, and importing data using SQL statements. You also learned how SQL backup files can restore databases and populate tables efficiently.