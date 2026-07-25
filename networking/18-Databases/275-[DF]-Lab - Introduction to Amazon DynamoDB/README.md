# Introduction to Amazon DynamoDB

## Lab Overview

Amazon DynamoDB is a fast and flexible NoSQL database service for applications that need consistent, single-digit millisecond latency at any scale. It is a fully managed database service that supports both document and key-value data models.

Its flexible schema and high performance make DynamoDB suitable for:

- Mobile applications
- Web applications
- Gaming platforms
- Ad-tech systems
- Internet of Things (IoT)
- Serverless applications

In this lab, you will create a DynamoDB table to store information about a music library. You will then add data, query the table, modify records, and delete the table.

---

# Topics Covered

In this lab, you will:

- Create an Amazon DynamoDB table
- Enter data into a DynamoDB table
- Query a DynamoDB table
- Modify existing items
- Delete a DynamoDB table

---

# Duration

This lab requires approximately **35 minutes** to complete.

---

# Key Terms

| Term | Description |
|---|---|
| DynamoDB | Fully managed NoSQL database service |
| Table | Collection of related data |
| Item | A single record in a table |
| Attribute | A property or field within an item |
| Partition Key | Primary key used to distribute data |
| Sort Key | Secondary key used to sort items |
| Query | Efficient retrieval using keys |
| Scan | Searches all items in a table |
| NoSQL | Non-relational database model |

---

# Accessing the AWS Management Console

1. Choose **Start Lab**
2. Wait for the lab status to turn green
3. Choose the green AWS button
4. The AWS Management Console opens automatically

> Do not change the AWS Region unless instructed.

---

# Task 1: Create a New Table

In this task, you create a DynamoDB table named `Music`.

---

## Step 1: Open DynamoDB

Navigate to:

```text
Services → Database → DynamoDB