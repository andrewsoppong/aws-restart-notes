# Working with Functions

## Scenario

The database operations team has created a relational database named:

```text
world
```

The database contains three tables:

- city
- country
- countrylanguage

You will write SQL queries using database functions with:

- `SELECT`
- `WHERE`

to manipulate and summarize data.

---

# Lab Overview and Objectives

This lab demonstrates how to use common SQL functions with the `SELECT` statement and `WHERE` clause.

After completing this lab, you should be able to:

- Use aggregate functions:
  - `SUM()`
  - `MIN()`
  - `MAX()`
  - `AVG()`
- Use the `SUBSTRING_INDEX()` function to split strings
- Use the `LENGTH()` and `TRIM()` functions to determine string length
- Use the `DISTINCT()` function to remove duplicate records
- Use functions in both `SELECT` and `WHERE` clauses

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

# Estimated Duration

Approximately:

```text
45 minutes
```

---

# AWS Service Restrictions

In this lab environment:

- Access may be restricted to only required AWS services
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

In the navigation pane:

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

In this task, you use SQL functions to process and manipulate data.

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

# SQL Functions

SQL functions process and manipulate data returned by queries.

Functions can be used in:

- `SELECT`
- `WHERE`
- `ORDER BY`

---

# Step 3: Use Aggregate Functions

Run:

```sql
SELECT SUM(Population),
       AVG(Population),
       MAX(Population),
       MIN(Population),
       COUNT(Population)
FROM world.country;
```

---

# Aggregate Function Explanation

| Function | Purpose |
|---|---|
| `SUM()` | Adds all values |
| `AVG()` | Calculates average |
| `MAX()` | Finds highest value |
| `MIN()` | Finds lowest value |
| `COUNT()` | Counts rows |

---

# SUM Function

The `SUM()` function adds numeric values.

Example:

```sql
SELECT SUM(Population)
FROM world.country;
```

---

# AVG Function

The `AVG()` function calculates the average.

Example:

```sql
SELECT AVG(Population)
FROM world.country;
```

---

# MAX Function

The `MAX()` function finds the largest value.

Example:

```sql
SELECT MAX(Population)
FROM world.country;
```

---

# MIN Function

The `MIN()` function finds the smallest value.

Example:

```sql
SELECT MIN(Population)
FROM world.country;
```

---

# COUNT Function

The `COUNT()` function counts rows.

Example:

```sql
SELECT COUNT(Population)
FROM world.country;
```

---

# Step 4: Split Strings Using SUBSTRING_INDEX()

Run:

```sql
SELECT Region,
       SUBSTRING_INDEX(Region, " ", 1)
FROM world.country;
```

---

# SUBSTRING_INDEX Function

The `SUBSTRING_INDEX()` function splits strings using a delimiter.

Syntax:

```sql
SUBSTRING_INDEX(string, delimiter, count)
```

---

# SUBSTRING_INDEX Parameters

| Parameter | Meaning |
|---|---|
| string | Text to split |
| delimiter | Character to split by |
| count | Number of parts returned |

---

# Example

```sql
SUBSTRING_INDEX(Region, " ", 1)
```

Returns the first word before a space.

---

# Step 5: Use SUBSTRING_INDEX() in a WHERE Clause

Run:

```sql
SELECT Name,
       Region
FROM world.country
WHERE SUBSTRING_INDEX(Region, " ", 1) = "Southern";
```

---

# Explanation

This query:

- Splits the Region column
- Extracts the first word
- Returns rows beginning with:

```text
Southern
```

---

# Step 6: Use LENGTH() and TRIM()

Run:

```sql
SELECT Region
FROM world.country
WHERE LENGTH(TRIM(Region)) < 10;
```

---

# TRIM Function

The `TRIM()` function removes leading and trailing spaces.

Example:

```sql
TRIM(Region)
```

---

# LENGTH Function

The `LENGTH()` function returns the number of characters in a string.

Example:

```sql
LENGTH(Region)
```

---

# Explanation

This query returns regions with names shorter than 10 characters.

---

# Step 7: Remove Duplicate Records Using DISTINCT()

Run:

```sql
SELECT DISTINCT(Region)
FROM world.country
WHERE LENGTH(TRIM(Region)) < 10;
```

---

# DISTINCT Function

The `DISTINCT()` function removes duplicate rows.

Syntax:

```sql
SELECT DISTINCT(column_name)
FROM table_name;
```

---

# Benefit of DISTINCT

Without `DISTINCT`, duplicate values appear multiple times.

With `DISTINCT`, each value appears only once.

---

# Challenge

Write a query to:

- Return rows where the region is:

```text
Micronesian/Caribbean
```

- Split the region into:
  - Region Name 1
  - Region Name 2

---

# Challenge Solution

```sql
SELECT Region,
       SUBSTRING_INDEX(Region, "/", 1) AS "Region Name 1",
       SUBSTRING_INDEX(Region, "/", -1) AS "Region Name 2"
FROM world.country
WHERE Region = 'Micronesian/Caribbean';
```

---

# Challenge Explanation

| Function | Purpose |
|---|---|
| `SUBSTRING_INDEX(..., "/", 1)` | Returns text before `/` |
| `SUBSTRING_INDEX(..., "/", -1)` | Returns text after `/` |
| `AS` | Creates readable column names |

---

# Expected Output

| Region | Region Name 1 | Region Name 2 |
|---|---|---|
| Micronesian/Caribbean | Micronesian | Caribbean |

---

# SQL Functions Used in This Lab

| Function | Purpose |
|---|---|
| `SUM()` | Adds numeric values |
| `AVG()` | Calculates average |
| `MAX()` | Finds largest value |
| `MIN()` | Finds smallest value |
| `COUNT()` | Counts rows |
| `SUBSTRING_INDEX()` | Splits strings |
| `LENGTH()` | Counts characters |
| `TRIM()` | Removes spaces |
| `DISTINCT()` | Removes duplicates |

---

# Example Queries

---

# Total Population

```sql
SELECT SUM(Population)
FROM world.country;
```

---

# Largest Population

```sql
SELECT MAX(Population)
FROM world.country;
```

---

# Smallest Population

```sql
SELECT MIN(Population)
FROM world.country;
```

---

# Average Population

```sql
SELECT AVG(Population)
FROM world.country;
```

---

# Unique Regions

```sql
SELECT DISTINCT(Region)
FROM world.country;
```

---

# Regions Shorter Than 10 Characters

```sql
SELECT Region
FROM world.country
WHERE LENGTH(TRIM(Region)) < 10;
```

---

# Important Database Concepts

---

# Aggregate Function

Functions that summarize multiple rows into one result.

Examples:

- SUM
- AVG
- MAX
- MIN

---

# String Function

Functions that manipulate text data.

Examples:

- SUBSTRING_INDEX
- LENGTH
- TRIM

---

# Duplicate Records

Duplicate records contain repeated values.

`DISTINCT()` removes duplicates.

---

# Result Set

A result set is the output returned by a query.

---

# Common SQL Errors

| Error | Cause |
|---|---|
| Syntax Error | Incorrect SQL syntax |
| Unknown Column | Column name incorrect |
| Unknown Function | Invalid function name |
| Invalid Parameters | Incorrect function arguments |

---

# Best Practices

- Use aliases for readability
- Use DISTINCT to remove duplicates
- Use aggregate functions carefully
- Use TRIM before LENGTH for accurate counts
- Test string functions on sample data

---

# Lab Review Questions

1. What does the SUM() function do?
2. What is the purpose of AVG()?
3. What does MAX() return?
4. What is the purpose of SUBSTRING_INDEX()?
5. Why is TRIM() useful?
6. What does LENGTH() return?
7. What is the purpose of DISTINCT()?

---

# Conclusion

Congratulations! You have successfully:

- Used aggregate functions to summarize data
- Used SUBSTRING_INDEX() to split strings
- Used LENGTH() and TRIM() to measure strings
- Used DISTINCT() to remove duplicate records
- Used functions in SELECT and WHERE clauses

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

In this lab, you learned how to use SQL aggregate and string functions to summarize, manipulate, and filter data. You practiced using functions such as SUM(), AVG(), SUBSTRING_INDEX(), LENGTH(), TRIM(), and DISTINCT() to query and analyze data from the `world` database.