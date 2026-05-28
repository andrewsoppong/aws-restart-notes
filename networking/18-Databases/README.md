# Introduction to Databases and Database Management Systems

## What You Will Learn

At the core of this lesson, you will learn how to:

- Identify different components of a database
- Differentiate between relational databases and nonrelational databases
- List the elements of a well-designed database
- Describe the purpose and functions of a Database Management System (DBMS)

---

# Introduction to Data and Databases

Modern organizations collect and manage large amounts of information. Databases help store, organize, retrieve, and manage this information efficiently.

Databases are used in:

- Banking systems
- Online shopping platforms
- Hospitals
- Schools
- Social media applications
- Cloud computing systems

---

# What is Data?

Data refers to raw facts, figures, and information that can be processed and stored.

Examples of data include:

- Names
- Numbers
- Dates
- Addresses
- Product prices

Example:

| Student ID | Name | Age |
|---|---|---|
| 101 | Andrews | 20 |
| 102 | Linda | 22 |

---

# What is a Database?

A database is an organized collection of related data stored electronically.

Databases allow users to:

- Store information
- Retrieve information quickly
- Update records
- Delete records
- Manage large amounts of data efficiently

---

# Components of a Database

A database contains several important components.

| Component | Description |
|---|---|
| Tables | Store data in rows and columns |
| Records | Individual rows of data |
| Fields | Individual columns in a table |
| Keys | Unique identifiers for records |
| Queries | Requests used to retrieve data |
| Relationships | Connections between tables |

---

# Example Database Table

| CustomerID | CustomerName | City |
|---|---|---|
| 1 | Andrews | Accra |
| 2 | Linda | Kumasi |

In this example:

- Each row is a **record**
- Each column is a **field**
- `CustomerID` can serve as a **primary key**

---

# Data Models

A data model defines how data is structured, stored, and related within a database.

Data models help:

- Organize information
- Maintain consistency
- Improve efficiency

---

# Relational Data Model

The relational data model organizes data into tables related to one another.

Characteristics include:

- Rows and columns
- Relationships between tables
- Structured schemas
- Use of SQL

Example:

## Students Table

| StudentID | Name |
|---|---|
| 1 | Andrews |

## Courses Table

| CourseID | CourseName |
|---|---|
| 101 | Python |

## Enrollment Table

| StudentID | CourseID |
|---|---|
| 1 | 101 |

---

# Schema

A schema is the structure or blueprint of a database.

It defines:

- Tables
- Fields
- Data types
- Relationships
- Constraints

Example schema definition:

```sql id="y2v8mr"
CREATE TABLE Students (
    StudentID INT,
    Name VARCHAR(50),
    Age INT
);