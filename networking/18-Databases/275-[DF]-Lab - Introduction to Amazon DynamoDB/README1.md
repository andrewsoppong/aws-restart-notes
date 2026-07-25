# Introduction to Amazon DynamoDB

## Lab Overview

Amazon DynamoDB is a fast and flexible NoSQL database service designed for applications that require consistent, single-digit millisecond latency at any scale. DynamoDB is fully managed and supports both document and key-value data models.

This lab demonstrates how to create and manage a DynamoDB table for storing music library information.

---

# Objectives

By completing this lab, you will learn how to:

* Create an Amazon DynamoDB table
* Add and manage items in a DynamoDB table
* Query and scan a DynamoDB table
* Modify existing records
* Delete a DynamoDB table

---

# Duration

Approximate completion time: **35 minutes**

---

# Prerequisites

Before starting this lab:

* Access to the AWS Management Console
* Basic understanding of databases
* AWS lab environment started and ready

---

# Accessing the AWS Management Console

1. Choose **Start Lab**
2. Wait until the lab status changes to **Ready**
3. Choose the green **AWS** button to open the AWS Management Console
4. Allow pop-ups if prompted
5. Ensure you remain in the assigned AWS Region

---

# Task 1: Create a DynamoDB Table

## Step 1: Open DynamoDB

1. In the AWS Management Console, open **Services**
2. Under **Database**, choose **DynamoDB**

## Step 2: Create the Table

1. Choose **Create table**
2. Configure the following settings:

| Setting       | Value           |
| ------------- | --------------- |
| Table name    | Music           |
| Partition key | Artist (String) |
| Sort key      | Song (String)   |

3. Leave all other settings as default
4. Choose **Create table**
5. Wait until the table status becomes **Active**

---

# Understanding DynamoDB Keys

## Partition Key

The partition key determines how data is distributed across DynamoDB partitions.

## Sort Key

The sort key organizes data within the same partition key.

Together, the partition key and sort key uniquely identify each item.

---

# Task 2: Add Data to the Table

## Item 1

Choose the **Music** table and then:

1. Choose **Actions**
2. Choose **Create item**

### Required Attributes

| Field  | Type   | Value      |
| ------ | ------ | ---------- |
| Artist | String | Pink Floyd |
| Song   | String | Money      |

### Additional Attributes

| Field | Type   | Value                     |
| ----- | ------ | ------------------------- |
| Album | String | The Dark Side of the Moon |
| Year  | Number | 1973                      |

Choose **Create item**

---

## Item 2

Create another item with the following values:

| Field  | Type   | Value       |
| ------ | ------ | ----------- |
| Artist | String | John Lennon |
| Song   | String | Imagine     |
| Album  | String | Imagine     |
| Year   | Number | 1971        |
| Genre  | String | Soft rock   |

This demonstrates DynamoDB schema flexibility because different items can contain different attributes.

---

## Item 3

Create another item:

| Field         | Type   | Value                     |
| ------------- | ------ | ------------------------- |
| Artist        | String | Psy                       |
| Song          | String | Gangnam Style             |
| Album         | String | Psy 6 (Six Rules), Part 1 |
| Year          | Number | 2011                      |
| LengthSeconds | Number | 219                       |

This demonstrates DynamoDB’s NoSQL flexibility.

---

# DynamoDB Concepts

## Items

Items are similar to rows in relational databases.

## Attributes

Attributes are similar to columns in relational databases.

## Schema Flexibility

Unlike relational databases, DynamoDB does not require every item to have the same attributes.

---

# Task 3: Modify an Existing Item

1. In the DynamoDB console, choose **Explore Items**
2. Select the **Music** table
3. Choose the item for **Psy**
4. Change:

| Field | Old Value | New Value |
| ----- | --------- | --------- |
| Year  | 2011      | 2012      |

5. Choose **Save changes**

---

# Task 4: Query the Table

## Query Operation

A query operation uses the primary key and is highly efficient.

### Steps

1. Expand **Scan/Query items**
2. Choose **Query**
3. Enter:

| Field  | Value         |
| ------ | ------------- |
| Artist | Psy           |
| Song   | Gangnam Style |

4. Choose **Run**

The matching item appears quickly because queries are indexed.

---

# Query vs Scan

| Operation | Performance | Usage              |
| --------- | ----------- | ------------------ |
| Query     | Fast        | Uses primary key   |
| Scan      | Slower      | Searches all items |

---

## Scan Operation

1. Choose **Scan**
2. Expand **Filters**
3. Enter:

| Field          | Value  |
| -------------- | ------ |
| Attribute name | Year   |
| Type           | Number |
| Value          | 1971   |

4. Choose **Run**

Only the song released in 1971 appears.

---

# Task 5: Delete the Table

1. In the DynamoDB dashboard, choose **Update settings**
2. Select the **Music** table
3. Choose **Actions**
4. Choose **Delete table**
5. Type:

```text
delete
```

6. Choose **Delete table**

The table and all data are permanently removed.

---

# Key DynamoDB Features Learned

## Fully Managed

AWS handles scaling, patching, and infrastructure management.

## High Performance

Provides low-latency responses at scale.

## Flexible Schema

Items can contain different attributes.

## Scalable

Automatically scales to workload demands.

## NoSQL Database

Optimized for key-value and document data models.

---

# Summary

In this lab, you successfully:

* Created a DynamoDB table
* Added multiple records
* Modified existing data
* Queried and scanned records
* Deleted a DynamoDB table

---

# Useful AWS Services Mentioned

* Amazon DynamoDB
* AWS Management Console

---

# Best Practices

* Use queries instead of scans whenever possible
* Design partition keys carefully for scalability
* Keep frequently accessed attributes lightweight
* Use sort keys for efficient filtering and organization

---

# Cleanup

At the end of the lab:

1. Choose **End Lab**
2. Confirm by choosing **Yes**
3. Wait for the AWS resources to terminate

---

# Author Notes

This repository documents AWS hands-on labs completed for learning and practice purposes.

Topics covered include:

* Amazon DynamoDB
* Amazon Aurora
* AWS Systems Manager
* AWS CLI
* Amazon RDS
* Amazon EC2
* SQL and NoSQL databases
