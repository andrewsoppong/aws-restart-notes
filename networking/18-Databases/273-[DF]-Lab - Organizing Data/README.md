# Organizing Data

## Scenario

The database operations team has created a relational database named:

```text
world
```

The database contains three tables:

- city
- country
- countrylanguage

You will write SQL queries to organize and analyze data using:

- `GROUP BY`
- `OVER`
- `SUM()`
- `RANK()`

---

# Lab Overview and Objectives

This lab demonstrates how to use database grouping and window functions.

After completing this lab, you should be able to:

- Use the `GROUP BY` clause with `SUM()`
- Use the `OVER` clause with `RANK()`
- Use the `OVER` clause with:
  - `SUM()`
  - `RANK()`

---

# Existing Resources

The following resources are already available:

- A Command Host EC2 instance
- A relational database named `world`
- Three tables:
  - city
  - country
  - countrylanguage

---

# Estimated Duration

```text
45 minutes
```

---

# AWS Service Restrictions

In this lab environment:

- Access may be restricted to only required AWS services
- Attempting other services may generate access errors

---

# Task 1: Connect to the Command Host

---

# Step 1: Open EC2

In the AWS Management Console:

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

If the terminal becomes unresponsive:

```bash
sudo su
cd /home/ec2-user/
mysql -u root --password='re:St@rt!9'
```

---

# Task 2: Query the world Database

In this task, you use SQL grouping and window functions.

---

# Step 1: Show Databases

Run:

```sql
SHOW DATABASES;
```

Verify the `world` database exists.

---

# Step 2: Review the country Table

Run:

```sql
SELECT * FROM world.country;
```

---

# Example 1: Query Australia and New Zealand

Run:

```sql
SELECT Region,
       Name,
       Population
FROM world.country
WHERE Region = 'Australia and New Zealand'
ORDER BY Population DESC;
```

---

# Explanation

| Clause | Purpose |
|---|---|
| `WHERE` | Filters rows |
| `ORDER BY Population DESC` | Sorts largest to smallest |

---

# GROUP BY Clause

The `GROUP BY` clause groups rows sharing the same value.

It is commonly used with aggregate functions such as:

- `SUM()`
- `AVG()`
- `COUNT()`
- `MAX()`
- `MIN()`

---

# Example 2: GROUP BY with SUM()

Run:

```sql
SELECT Region,
       SUM(Population)
FROM world.country
WHERE Region = 'Australia and New Zealand'
GROUP BY Region
ORDER BY SUM(Population) DESC;
```

---

# Explanation

This query:

1. Filters rows for Australia and New Zealand
2. Groups records by region
3. Calculates total population

---

# SUM Function

The `SUM()` function adds numeric values.

Example:

```sql
SUM(Population)
```

---

# OVER Clause

The `OVER()` clause creates a window for calculations across related rows.

It is commonly used with:

- `SUM()`
- `RANK()`
- `ROW_NUMBER()`

---

# Window Function

A window function performs calculations across a group of rows without collapsing them into one result.

Unlike `GROUP BY`, window functions preserve individual rows.

---

# Example 3: Running Total Using OVER()

Run:

```sql
SELECT Region,
       Name,
       Population,
       SUM(Population)
       OVER(PARTITION BY Region ORDER BY Population)
       AS 'Running Total'
FROM world.country
WHERE Region = 'Australia and New Zealand';
```

---

# Explanation

| Function | Purpose |
|---|---|
| `OVER()` | Defines the calculation window |
| `PARTITION BY Region` | Groups rows by region |
| `ORDER BY Population` | Orders rows before calculation |
| `SUM()` | Creates running total |

---

# Running Total

A running total continuously adds values row by row.

Example:

| Country | Population | Running Total |
|---|---|---|
| Country A | 5M | 5M |
| Country B | 7M | 12M |
| Country C | 9M | 21M |

---

# RANK Function

The `RANK()` function assigns ranking numbers to rows.

It is commonly used with:

```sql
OVER()
```

---

# Example 4: Ranking Countries

Run:

```sql
SELECT Region,
       Name,
       Population,
       SUM(Population)
       OVER(PARTITION BY Region ORDER BY Population)
       AS 'Running Total',
       RANK()
       OVER(PARTITION BY Region ORDER BY Population)
       AS 'Ranked'
FROM world.country
WHERE Region = 'Australia and New Zealand';
```

---

# Explanation

| Function | Purpose |
|---|---|
| `RANK()` | Assigns ranking positions |
| `PARTITION BY Region` | Resets ranking per region |
| `ORDER BY Population` | Ranks by population |

---

# PARTITION BY

`PARTITION BY` divides rows into groups for window calculations.

Each partition is processed independently.

---

# GROUP BY vs OVER

| Feature | GROUP BY | OVER |
|---|---|---|
| Combines rows | Yes | No |
| Keeps individual rows | No | Yes |
| Used with aggregate functions | Yes | Yes |
| Supports running totals | No | Yes |
| Supports ranking | No | Yes |

---

# Challenge

Write a query to:

- Rank countries in each region
- Sort populations from largest to smallest

You must decide whether to use:

- `GROUP BY` or `OVER`
- `SUM()` or `RANK()`

---

# Challenge Solution

```sql
SELECT Region,
       Name,
       Population,
       RANK()
       OVER(PARTITION BY Region ORDER BY Population DESC)
       AS 'Population Rank'
FROM world.country;
```

---

# Challenge Explanation

| Clause / Function | Purpose |
|---|---|
| `RANK()` | Assigns ranking numbers |
| `OVER()` | Defines window calculations |
| `PARTITION BY Region` | Ranks countries inside each region |
| `ORDER BY Population DESC` | Largest population ranked first |

---

# Expected Output Example

| Region | Name | Population | Population Rank |
|---|---|---|---|
| Southern Europe | Italy | 57680000 | 1 |
| Southern Europe | Spain | 39441700 | 2 |

---

# Common SQL Functions Used

| Function | Purpose |
|---|---|
| `SUM()` | Adds values |
| `RANK()` | Assigns rankings |
| `OVER()` | Defines window |
| `PARTITION BY` | Creates groups |
| `ORDER BY` | Sorts rows |

---

# Additional Examples

---

# Total Population Per Region

```sql
SELECT Region,
       SUM(Population)
FROM world.country
GROUP BY Region;
```

---

# Rank Countries Globally

```sql
SELECT Name,
       Population,
       RANK() OVER(ORDER BY Population DESC) AS Ranking
FROM world.country;
```

---

# Running Population Total

```sql
SELECT Name,
       Population,
       SUM(Population)
       OVER(ORDER BY Population)
       AS RunningTotal
FROM world.country;
```

---

# Important Concepts

---

# Aggregate Function

Functions that summarize multiple rows.

Examples:

- SUM
- AVG
- COUNT

---

# Window Function

Functions that calculate across rows while keeping each row visible.

Examples:

- RANK
- SUM OVER

---

# Running Total

A cumulative total calculated row by row.

---

# Ranking

Assigning positions based on sorting criteria.

---

# Common Errors

| Error | Cause |
|---|---|
| Syntax error | Incorrect SQL syntax |
| Unknown column | Wrong column name |
| Invalid window function | Incorrect OVER usage |
| Missing ORDER BY | Ranking order undefined |

---

# Best Practices

- Use aliases for readability
- Use `PARTITION BY` carefully
- Use `DESC` for highest rankings first
- Use window functions for analytics
- Keep queries readable

---

# Lab Review Questions

1. What does `GROUP BY` do?
2. What is the purpose of `OVER()`?
3. What does `RANK()` return?
4. What is a running total?
5. What is the difference between `GROUP BY` and `OVER()`?
6. Why is `PARTITION BY` useful?

---

# Conclusion

Congratulations! You have successfully:

- Used `GROUP BY` with `SUM()`
- Used `OVER()` with `RANK()`
- Used running totals with window functions
- Ranked countries by population
- Organized data using SQL analytics functions

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

SQL Window Functions:

```text
https://www.w3schools.com/sql/sql_window_functions.asp
```

AWS Training and Certification:

```text
https://aws.amazon.com/training/
```

---

# Summary

In this lab, you learned how to organize and analyze SQL data using:

- GROUP BY
- OVER
- SUM()
- RANK()

You also learned how to create running totals, rank records within groups, and perform advanced analytics with SQL window functions.