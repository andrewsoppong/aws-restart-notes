# Sorting and Grouping Data in SQL

## What You Will Learn

At the core of this lesson, you will learn how to:

- Use the `ORDER BY` clause to sort data
- Sort data in:
  - Ascending order
  - Descending order
- Use the `GROUP BY` clause to group records
- Use the `HAVING` clause to filter grouped data

---

# Key Terms

| Term | Description |
|---|---|
| Sorting | Arranging data in a specific order |
| ORDER BY clause | Sorts query results |
| GROUP BY clause | Groups rows with similar values |
| HAVING clause | Filters grouped results |

---

# Sorting Data in SQL

Sorting organizes query results in a meaningful order.

SQL uses the:

```sql
ORDER BY
```

clause to sort records.

---

# ORDER BY Clause

The `ORDER BY` clause sorts records returned by a query.

---

# Syntax

```sql
SELECT column_name
FROM table_name
ORDER BY column_name;
```

---

# Ascending Order

Ascending order sorts values from:

- Lowest to highest
- A to Z

Ascending order is the default sorting method.

---

# Example: Ascending Order

```sql
SELECT Name, Population
FROM world.country
ORDER BY Population;
```

---

# Descending Order

Descending order sorts values from:

- Highest to lowest
- Z to A

Use:

```sql
DESC
```

---

# Example: Descending Order

```sql
SELECT Name, Population
FROM world.country
ORDER BY Population DESC;
```

---

# Multiple Column Sorting

You can sort using more than one column.

---

# Example

```sql
SELECT Name, Region, Population
FROM world.country
ORDER BY Region, Population DESC;
```

---

# GROUP BY Clause

The `GROUP BY` clause groups rows that share the same value.

It is commonly used with aggregate functions such as:

- `COUNT()`
- `SUM()`
- `AVG()`
- `MAX()`
- `MIN()`

---

# Syntax

```sql
SELECT column_name, aggregate_function(column_name)
FROM table_name
GROUP BY column_name;
```

---

# Example: Count Countries Per Region

```sql
SELECT Region,
       COUNT(*) AS "Country Count"
FROM world.country
GROUP BY Region;
```

---

# Explanation

| Clause | Purpose |
|---|---|
| `COUNT(*)` | Counts rows |
| `GROUP BY Region` | Groups rows by region |

---

# Example: Average Population Per Region

```sql
SELECT Region,
       AVG(Population) AS "Average Population"
FROM world.country
GROUP BY Region;
```

---

# Aggregate Functions with GROUP BY

| Function | Purpose |
|---|---|
| `COUNT()` | Counts rows |
| `SUM()` | Adds values |
| `AVG()` | Calculates average |
| `MAX()` | Finds highest value |
| `MIN()` | Finds lowest value |

---

# HAVING Clause

The `HAVING` clause filters grouped records.

Unlike `WHERE`, `HAVING` works after grouping occurs.

---

# Syntax

```sql
SELECT column_name, aggregate_function(column_name)
FROM table_name
GROUP BY column_name
HAVING condition;
```

---

# Example: Regions with Population Greater Than 100 Million

```sql
SELECT Region,
       SUM(Population) AS "Total Population"
FROM world.country
GROUP BY Region
HAVING SUM(Population) > 100000000;
```

---

# WHERE vs HAVING

| Clause | Purpose |
|---|---|
| `WHERE` | Filters rows before grouping |
| `HAVING` | Filters groups after grouping |

---

# Example Using WHERE and HAVING Together

```sql
SELECT Region,
       COUNT(*) AS "Country Count"
FROM world.country
WHERE Population > 1000000
GROUP BY Region
HAVING COUNT(*) > 5;
```

---

# Explanation

1. `WHERE` filters rows first
2. `GROUP BY` groups remaining rows
3. `HAVING` filters grouped results

---

# Common SQL Examples

---

# Sort Countries by Name

```sql
SELECT Name
FROM world.country
ORDER BY Name;
```

---

# Sort Countries by Population Descending

```sql
SELECT Name, Population
FROM world.country
ORDER BY Population DESC;
```

---

# Group Countries by Continent

```sql
SELECT Continent,
       COUNT(*) AS "Number of Countries"
FROM world.country
GROUP BY Continent;
```

---

# Total Population by Region

```sql
SELECT Region,
       SUM(Population) AS "Total Population"
FROM world.country
GROUP BY Region;
```

---

# Regions with More Than 10 Countries

```sql
SELECT Region,
       COUNT(*) AS "Country Count"
FROM world.country
GROUP BY Region
HAVING COUNT(*) > 10;
```

---

# SQL Query Execution Order

SQL processes queries in this order:

1. FROM
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. ORDER BY

---

# Important Notes

- `ORDER BY` sorts final results
- `GROUP BY` combines similar rows
- `HAVING` filters grouped data
- Aggregate functions are often used with `GROUP BY`

---

# Common Errors

| Error | Cause |
|---|---|
| Unknown column | Incorrect column name |
| Invalid use of group function | Aggregate function used incorrectly |
| Missing GROUP BY | Non-aggregated columns not grouped |
| Syntax error | Incorrect SQL syntax |

---

# Best Practices

- Use aliases with aggregate functions
- Use `ORDER BY` for readable output
- Use `HAVING` only for grouped results
- Keep queries simple and readable

---

# Practice Queries

---

# Query 1

Sort all countries by surface area:

```sql
SELECT Name, SurfaceArea
FROM world.country
ORDER BY SurfaceArea DESC;
```

---

# Query 2

Count countries in each continent:

```sql
SELECT Continent,
       COUNT(*) AS "Country Count"
FROM world.country
GROUP BY Continent;
```

---

# Query 3

Show continents with average population above 20 million:

```sql
SELECT Continent,
       AVG(Population) AS "Average Population"
FROM world.country
GROUP BY Continent
HAVING AVG(Population) > 20000000;
```

---

# Summary

In this lesson, you learned how to:

- Sort data using `ORDER BY`
- Sort ascending and descending
- Group rows using `GROUP BY`
- Filter grouped results using `HAVING`
- Use aggregate functions with grouped data

These SQL features are essential for organizing, summarizing, and analyzing database information efficiently.