# Selecting Data from a Database

## Scenario

The database operations team has created a relational database named:

```text
world
```

The database contains three tables:

- city
- country
- countrylanguage

Your task is to query the database using SQL statements and common database operators.

---

# Lab Overview and Objectives

This lab demonstrates how to use:

- The `SELECT` statement
- Database comparison operators
- SQL filtering and sorting operations

After completing this lab, you should be able to:

- Use the `SELECT` statement to query a database
- Use the `COUNT()` function
- Use comparison operators such as:
  - `<`
  - `>`
  - `=`
- Use:
  - `WHERE`
  - `ORDER BY`
  - `AND`

---

# Existing Resources

The following resources are already created:

- A Command Host EC2 instance
- A database named `world`
- Three tables:
  - city
  - country
  - countrylanguage

---

# Estimated Duration

Approximately:

```text
45 minutes
```

---

# AWS Service Restrictions

In this lab environment:

- Only required AWS services may be available
- Other services might generate access errors

---

# Task 1: Connect to the Command Host

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

# Step 6: Connect to MySQL

Run:

```bash
mysql -u root --password='re:St@rt!9'
```

---

# Reconnect if Needed

If Session Manager becomes unresponsive:

```bash
sudo su
cd /home/ec2-user/
mysql -u root --password='re:St@rt!9'
```

---

# Task 2: Query the world Database

In this task, you query the database using SQL statements and operators.

---

# Step 1: Show Existing Databases

Run:

```sql
SHOW DATABASES;
```

Verify that the `world` database exists.

---

# Step 2: Display All Rows and Columns

Run:

```sql
SELECT * FROM world.country;
```

---

# Understanding SELECT

The `SELECT` statement retrieves data from a database table.

Syntax:

```sql
SELECT column_name
FROM table_name;
```

---

# Meaning of *

The `*` symbol means:

```text
All columns
```

---

# Step 3: Count Rows in a Table

Run:

```sql
SELECT COUNT(*) FROM world.country;
```

---

# COUNT() Function

The `COUNT()` function counts rows in a table.

Examples:

Count all rows:

```sql
SELECT COUNT(*) FROM table_name;
```

Count rows with values in a specific column:

```sql
SELECT COUNT(Population)
FROM world.country;
```

---

# Step 4: View Table Columns

Run:

```sql
SHOW COLUMNS FROM world.country;
```

---

# Purpose of SHOW COLUMNS

The `SHOW COLUMNS` statement displays:

- Column names
- Data types
- Key information
- NULL settings

---

# Step 5: Query Specific Columns

Run:

```sql
SELECT Name, Capital, Region, SurfaceArea, Population
FROM world.country;
```

---

# Selecting Specific Columns

Instead of retrieving all columns, you can select only required columns.

Benefits:

- Faster queries
- Cleaner output
- Easier analysis

---

# Step 6: Rename a Column Using AS

Run:

```sql
SELECT Name,
       Capital,
       Region,
       SurfaceArea AS "Surface Area",
       Population
FROM world.country;
```

---

# Understanding AS

The `AS` keyword renames a column in the query output.

Example:

```sql
SurfaceArea AS "Surface Area"
```

This changes the displayed column name.

---

# Step 7: Sort Results Using ORDER BY

Run:

```sql
SELECT Name,
       Capital,
       Region,
       SurfaceArea AS "Surface Area",
       Population
FROM world.country
ORDER BY Population;
```

---

# ORDER BY

The `ORDER BY` clause sorts query results.

Default order:

```text
Ascending
```

---

# Step 8: Sort in Descending Order

Run:

```sql
SELECT Name,
       Capital,
       Region,
       SurfaceArea AS "Surface Area",
       Population
FROM world.country
ORDER BY Population DESC;
```

---

# DESC Option

`DESC` sorts results in descending order.

Example:

```text
Largest to smallest
```

---

# Step 9: Filter Results Using WHERE

Run:

```sql
SELECT Name,
       Capital,
       Region,
       SurfaceArea AS "Surface Area",
       Population
FROM world.country
WHERE Population > 50000000
ORDER BY Population DESC;
```

---

# WHERE Clause

The `WHERE` clause filters rows based on conditions.

Syntax:

```sql
SELECT columns
FROM table
WHERE condition;
```

---

# Comparison Operators

| Operator | Meaning |
|---|---|
| = | Equal to |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal |
| <= | Less than or equal |
| != | Not equal |

---

# Step 10: Use Multiple Conditions with AND

Run:

```sql
SELECT Name,
       Capital,
       Region,
       SurfaceArea AS "Surface Area",
       Population
FROM world.country
WHERE Population > 50000000
AND Population < 100000000
ORDER BY Population DESC;
```

---

# AND Operator

The `AND` operator requires both conditions to be true.

Example:

```sql
WHERE condition1
AND condition2
```

---

# Challenge

Query the `country` table to answer the following question:

```text
Which country in Southern Europe has a population greater than 50,000,000?
```

---

# Challenge Solution

```sql
SELECT Name,
       Region,
       Population
FROM world.country
WHERE Region = 'Southern Europe'
AND Population > 50000000;
```

---

# Expected Result

The query should return:

```text
Italy
```

---

# SQL Commands Used in This Lab

| Command | Purpose |
|---|---|
| SELECT | Retrieve data |
| COUNT() | Count rows |
| SHOW DATABASES | Display databases |
| SHOW COLUMNS | Display column details |
| ORDER BY | Sort results |
| WHERE | Filter rows |
| AS | Rename columns |
| AND | Combine conditions |

---

# Database Operators Used

| Operator | Purpose |
|---|---|
| < | Less than |
| > | Greater than |
| = | Equal to |
| AND | Combine conditions |

---

# Important Database Concepts

---

# Result Set

A result set is the output returned by a query.

---

# Filtering

Filtering limits returned rows based on conditions.

---

# Sorting

Sorting arranges results in a specific order.

---

# Aggregate Function

Functions like `COUNT()` summarize data.

---

# Example Queries

---

# Query All Countries

```sql
SELECT * FROM world.country;
```

---

# Query Countries with Small Population

```sql
SELECT Name, Population
FROM world.country
WHERE Population < 1000000;
```

---

# Query Countries in Europe

```sql
SELECT Name, Region
FROM world.country
WHERE Continent = 'Europe';
```

---

# Query Largest Populations

```sql
SELECT Name, Population
FROM world.country
ORDER BY Population DESC;
```

---

# Common SQL Errors

| Error | Cause |
|---|---|
| Syntax Error | Invalid SQL syntax |
| Unknown Column | Column name incorrect |
| Unknown Table | Table does not exist |
| Access Denied | Invalid permissions |

---

# Best Practices

- Use WHERE clauses carefully
- Select only required columns
- Sort large datasets with ORDER BY
- Use meaningful aliases with AS
- Verify query output

---

# Lab Review Questions

1. What does the SELECT statement do?
2. What is the purpose of COUNT()?
3. What does ORDER BY do?
4. What is the purpose of WHERE?
5. What does the AND operator do?
6. What is the difference between ascending and descending order?

---

# Conclusion

Congratulations! You have successfully:

- Used the SELECT statement to query a database
- Used the COUNT() function
- Used comparison operators
- Used WHERE clauses to filter data
- Used ORDER BY to sort query results
- Used the AND operator to combine conditions

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

In this lab, you practiced querying relational databases using SQL SELECT statements and common database operators. You learned how to retrieve, filter, count, sort, and analyze data from the `world` database using SQL clauses such as WHERE, ORDER BY, and AND.