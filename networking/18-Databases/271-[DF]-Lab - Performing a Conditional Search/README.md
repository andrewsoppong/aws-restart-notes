# Performing a Conditional Search

## Scenario

The database operations team has created a relational database named:

```text
world
```

The database contains three tables:

- city
- country
- countrylanguage

Your task is to query the database by using:

- `SELECT`
- `WHERE`
- `BETWEEN`
- `LIKE`
- SQL functions
- Column aliases

to perform conditional searches.

---

# Lab Overview and Objectives

This lab demonstrates how to use:

- The `SELECT` statement
- The `WHERE` clause
- Conditional filtering
- SQL functions and operators

After completing this lab, you should be able to:

- Write search conditions using the `WHERE` clause
- Use the `BETWEEN` operator
- Use the `LIKE` operator with wildcard characters
- Use the `AS` operator to create column aliases
- Use functions in a `SELECT` statement
- Use functions in a `WHERE` clause

---

# Existing Resources

The following resources are already created:

- A Command Host EC2 instance
- A database named `world`
- Three tables:
  - city
  - country
  - countrylanguage

The Command Host includes a database client used to connect to MySQL.

---

# Estimated Duration

Approximately:

```text
45 minutes
```

---

# AWS Service Restrictions

In this lab environment:

- Access may be limited to required AWS services
- Other services may generate access errors

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

If the Session Manager becomes unresponsive:

```bash
sudo su
cd /home/ec2-user/
mysql -u root --password='re:St@rt!9'
```

---

# Task 2: Query the world Database

In this task, you query the database using conditional searches.

---

# Step 1: Show Existing Databases

Run:

```sql
SHOW DATABASES;
```

Verify that the `world` database exists.

---

# Step 2: Review the country Table

Run:

```sql
SELECT * FROM world.country;
```

---

# SELECT Statement

The `SELECT` statement retrieves data from a table.

Syntax:

```sql
SELECT column_name
FROM table_name;
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

# Step 3: Filter Records Using WHERE and AND

Run:

```sql
SELECT Name,
       Capital,
       Region,
       SurfaceArea,
       Population
FROM world.country
WHERE Population >= 50000000
AND Population <= 100000000;
```

---

# Explanation

This query returns countries where:

- Population is greater than or equal to 50 million
- AND population is less than or equal to 100 million

---

# Comparison Operators

| Operator | Meaning |
|---|---|
| = | Equal to |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal to |
| <= | Less than or equal to |

---

# AND Operator

The `AND` operator requires all conditions to be true.

Example:

```sql
WHERE condition1
AND condition2
```

---

# Step 4: Use the BETWEEN Operator

Run:

```sql
SELECT Name,
       Capital,
       Region,
       SurfaceArea,
       Population
FROM world.country
WHERE Population BETWEEN 50000000 AND 100000000;
```

---

# BETWEEN Operator

The `BETWEEN` operator checks whether a value falls within a range.

Syntax:

```sql
WHERE column BETWEEN value1 AND value2;
```

---

# Important Note About BETWEEN

`BETWEEN` is inclusive.

Meaning:

- Beginning value included
- Ending value included

---

# Step 5: Use the LIKE Operator

Run:

```sql
SELECT SUM(Population)
FROM world.country
WHERE Region LIKE "%Europe%";
```

---

# LIKE Operator

The `LIKE` operator searches for patterns in strings.

Syntax:

```sql
WHERE column LIKE pattern;
```

---

# Wildcard Characters

| Wildcard | Meaning |
|---|---|
| % | Any number of characters |
| _ | One character |

---

# Example of %

```sql
LIKE "%Europe%"
```

Matches:

- Southern Europe
- Eastern Europe
- Western Europe
- Northern Europe

---

# SUM Function

The `SUM()` function adds values in a column.

Example:

```sql
SELECT SUM(Population)
FROM table_name;
```

---

# Step 6: Create a Column Alias Using AS

Run:

```sql
SELECT SUM(Population) AS "Europe Population Total"
FROM world.country
WHERE Region LIKE "%Europe%";
```

---

# AS Operator

The `AS` operator renames output columns.

Syntax:

```sql
column_name AS "New Name"
```

---

# Benefit of Column Aliases

Aliases make query results easier to read.

Example:

```text
Europe Population Total
```

instead of:

```text
SUM(Population)
```

---

# SQL Is Not Case Sensitive

These are equivalent:

```sql
SELECT
```

```sql
select
```

However, database collations may affect text comparisons.

---

# Step 7: Perform a Case-Sensitive Search Using LOWER()

Run:

```sql
SELECT Name,
       Capital,
       Region,
       SurfaceArea,
       Population
FROM world.country
WHERE LOWER(Region) LIKE "%central%";
```

---

# LOWER Function

The `LOWER()` function converts text to lowercase.

Syntax:

```sql
LOWER(column_name)
```

---

# Purpose of LOWER()

Using `LOWER()` helps perform case-insensitive comparisons.

Example:

```sql
LOWER(Region) LIKE "%central%"
```

Matches:

- Central Europe
- CENTRAL EUROPE
- central europe

---

# Challenge

Write a query to return:

- The sum of the surface area
- The sum of the population

for:

```text
North America
```

---

# Challenge Solution

```sql
SELECT SUM(SurfaceArea) AS "Total Surface Area",
       SUM(Population) AS "Total Population"
FROM world.country
WHERE Region LIKE "%North America%";
```

---

# Challenge Explanation

| Clause | Purpose |
|---|---|
| SUM(SurfaceArea) | Adds all surface areas |
| SUM(Population) | Adds all population values |
| AS | Renames columns |
| LIKE | Searches for matching regions |

---

# SQL Functions Used in This Lab

| Function | Purpose |
|---|---|
| COUNT() | Counts rows |
| SUM() | Adds numeric values |
| LOWER() | Converts text to lowercase |

---

# SQL Operators Used

| Operator | Purpose |
|---|---|
| WHERE | Filters rows |
| BETWEEN | Filters ranges |
| LIKE | Searches patterns |
| AND | Combines conditions |
| AS | Renames columns |

---

# Example Queries

---

# Countries with Large Population

```sql
SELECT Name, Population
FROM world.country
WHERE Population > 100000000;
```

---

# European Countries

```sql
SELECT Name, Region
FROM world.country
WHERE Region LIKE "%Europe%";
```

---

# Countries Between Two Population Values

```sql
SELECT Name, Population
FROM world.country
WHERE Population BETWEEN 1000000 AND 5000000;
```

---

# Total Population of Asia

```sql
SELECT SUM(Population)
FROM world.country
WHERE Region LIKE "%Asia%";
```

---

# Common SQL Errors

| Error | Cause |
|---|---|
| Syntax Error | Incorrect SQL syntax |
| Unknown Column | Column does not exist |
| Unknown Table | Table does not exist |
| Invalid Function | Incorrect function usage |

---

# Best Practices

- Use WHERE to reduce unnecessary data
- Use aliases for readability
- Use BETWEEN for range conditions
- Use LOWER() for case-insensitive searches
- Use LIKE carefully with wildcard characters

---

# Important Database Concepts

---

# Conditional Search

A conditional search filters rows based on specified conditions.

---

# Aggregate Function

Functions such as `SUM()` and `COUNT()` summarize data.

---

# Pattern Matching

Pattern matching searches for text patterns using wildcards.

---

# Result Set

A result set is the data returned by a query.

---

# Lab Review Questions

1. What is the purpose of the WHERE clause?
2. What does the BETWEEN operator do?
3. What is the purpose of the LIKE operator?
4. What does `%` represent in a LIKE condition?
5. Why is the AS operator useful?
6. What does the LOWER() function do?
7. What is the purpose of SUM()?

---

# Conclusion

Congratulations! You have successfully:

- Written search conditions using WHERE
- Used the BETWEEN operator
- Used the LIKE operator with wildcard characters
- Used the AS operator to create aliases
- Used SQL functions in SELECT statements
- Used SQL functions in WHERE clauses

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

In this lab, you practiced conditional database searches using SQL. You learned how to filter records using WHERE, BETWEEN, and LIKE, create readable column aliases with AS, and use SQL functions such as SUM() and LOWER() to analyze and search data effectively.