# Challenge Lab: Build Your DB Server and Interact With Your DB

## Lab Overview

This challenge lab demonstrates how to deploy and interact with a managed relational database using Amazon Relational Database Service (Amazon RDS).

Amazon RDS simplifies database administration tasks such as provisioning, patching, backups, scaling, and high availability, allowing developers to focus on applications instead of infrastructure management.

In this lab, you will:

* Create an Amazon RDS database instance
* Connect to a Linux server using SSH
* Install a MySQL client
* Connect to the database
* Create tables
* Insert records
* Query data
* Perform SQL joins

---

# Objectives

After completing this lab, you will be able to:

* Launch an Amazon RDS DB instance
* Connect to a remote Linux server using SSH
* Install and use a MySQL client
* Create relational database tables
* Insert and retrieve records
* Perform INNER JOIN operations
* Use SQL in a cloud-hosted database environment

---

# Duration

Approximate completion time: **45 minutes**

---

# AWS Services Used

* Amazon RDS
* Amazon EC2
* Amazon VPC
* Security Groups
* MySQL
* SSH

---

# Architecture Overview

```text id="x89o2l"
Local Computer
      │
      │ SSH
      ▼
LinuxServer (EC2)
      │
      │ MySQL Client
      ▼
Amazon RDS MySQL/Aurora Instance
```

---

# Prerequisites

Before starting:

* Start the AWS Lab environment
* Download the PEM or PPK key file
* Ensure SSH client availability
* Use the provided LabVPC

---

# Task 1: Create an Amazon RDS Database

## Step 1: Open Amazon RDS

1. Open the AWS Management Console
2. Search for **RDS**
3. Choose **Databases**
4. Click **Create database**

---

## Step 2: Configure the Database

### Database Engine

Choose one:

* Amazon Aurora Provisioned
  OR
* MySQL

---

## Step 3: Configure Required Settings

| Setting           | Value                       |
| ----------------- | --------------------------- |
| Template          | Dev/Test or Free tier       |
| Multi-AZ          | Disabled                    |
| DB Instance Class | db.t3.micro to db.t3.medium |
| Storage Type      | General Purpose SSD (gp2)   |
| Storage Size      | Up to 100 GB                |
| VPC               | LabVPC                      |
| Purchasing Option | On-Demand                   |

---

## Step 4: Configure Connectivity

| Setting        | Value                    |
| -------------- | ------------------------ |
| Public Access  | No                       |
| Security Group | Allow LinuxServer access |

---

## Step 5: Save Credentials

Make note of:

* DB endpoint
* Username
* Password
* Port number

You will need these later.

---

# Task 2: Download PEM/PPK Key

1. Choose **Details**
2. Choose **Show**
3. Download:

   * PEM for Linux/macOS
   * PPK for Windows
4. Copy the LinuxServer public IP address

---

# Task 3: Connect to LinuxServer Using SSH

## Linux/macOS

```bash id="0tgn2s"
chmod 400 labsuser.pem

ssh -i labsuser.pem ec2-user@<LinuxServer-IP>
```

---

## Windows (PuTTY)

1. Open PuTTY
2. Load the PPK file
3. Connect using:

   * Hostname = LinuxServer IP
   * Port = 22

---

# Task 4: Install MySQL Client

## Amazon Linux / Red Hat

```bash id="0fg8cs"
sudo yum install mariadb -y
```

Verify installation:

```bash id="xmj4rk"
mysql --version
```

---

# Task 5: Connect to the Database

```bash id="pcn64m"
mysql -u admin -p -h <RDS-ENDPOINT>
```

Example:

```bash id="v9ewfd"
mysql -u admin -p -h mydb.cluster-abcdefgh.us-west-2.rds.amazonaws.com
```

Enter the database password when prompted.

---

# Task 6: Create Database Tables

## Create Database

```sql id="f7e3v5"
CREATE DATABASE studentdb;

USE studentdb;
```

---

# Task 7: Create RESTART Table

```sql id="c76sml"
CREATE TABLE RESTART (
    StudentID INT,
    StudentName VARCHAR(100),
    RestartCity VARCHAR(100),
    GraduationDate DATETIME
);
```

---

# Task 8: Insert Sample Data into RESTART

```sql id="r85b4d"
INSERT INTO RESTART VALUES
(1, 'John Doe', 'Accra', '2025-06-01 10:00:00'),
(2, 'Jane Smith', 'Kumasi', '2025-06-02 10:00:00'),
(3, 'Michael Brown', 'Tamale', '2025-06-03 10:00:00'),
(4, 'Emily Davis', 'Cape Coast', '2025-06-04 10:00:00'),
(5, 'Daniel Wilson', 'Takoradi', '2025-06-05 10:00:00'),
(6, 'Sophia Taylor', 'Sunyani', '2025-06-06 10:00:00'),
(7, 'James Anderson', 'Ho', '2025-06-07 10:00:00'),
(8, 'Olivia Thomas', 'Bolgatanga', '2025-06-08 10:00:00'),
(9, 'William Jackson', 'Wa', '2025-06-09 10:00:00'),
(10, 'Emma White', 'Koforidua', '2025-06-10 10:00:00');
```

---

# Task 9: Query RESTART Table

```sql id="kts6v7"
SELECT * FROM RESTART;
```

---

# Task 10: Create CLOUD_PRACTITIONER Table

```sql id="rlzqow"
CREATE TABLE CLOUD_PRACTITIONER (
    StudentID INT,
    CertificationDate DATETIME
);
```

---

# Task 11: Insert Data into CLOUD_PRACTITIONER

```sql id="p0zclq"
INSERT INTO CLOUD_PRACTITIONER VALUES
(1, '2025-07-01 09:00:00'),
(3, '2025-07-03 09:00:00'),
(5, '2025-07-05 09:00:00'),
(7, '2025-07-07 09:00:00'),
(9, '2025-07-09 09:00:00');
```

---

# Task 12: Query CLOUD_PRACTITIONER Table

```sql id="t3c5hb"
SELECT * FROM CLOUD_PRACTITIONER;
```

---

# Task 13: Perform INNER JOIN

```sql id="jop3m6"
SELECT 
    RESTART.StudentID,
    RESTART.StudentName,
    CLOUD_PRACTITIONER.CertificationDate
FROM RESTART
INNER JOIN CLOUD_PRACTITIONER
ON RESTART.StudentID = CLOUD_PRACTITIONER.StudentID;
```

---

# Expected Output

| StudentID | StudentName     | CertificationDate |
| --------- | --------------- | ----------------- |
| 1         | John Doe        | 2025-07-01        |
| 3         | Michael Brown   | 2025-07-03        |
| 5         | Daniel Wilson   | 2025-07-05        |
| 7         | James Anderson  | 2025-07-07        |
| 9         | William Jackson | 2025-07-09        |

---

# SQL Concepts Practiced

## CREATE TABLE

Used to create relational database tables.

## INSERT INTO

Used to add records into tables.

## SELECT

Used to retrieve data.

## INNER JOIN

Combines rows from two tables based on matching column values.

---

# Screenshots to Capture

You should capture screenshots of:

* RESTART table creation
* RESTART inserted records
* RESTART SELECT query
* CLOUD_PRACTITIONER table creation
* CLOUD_PRACTITIONER inserted records
* CLOUD_PRACTITIONER SELECT query
* INNER JOIN query result

---

# Troubleshooting

## Cannot Connect to RDS

Check:

* Security group rules
* Correct endpoint
* Database status = Available

---

## Access Denied

Ensure:

* Correct username/password
* Proper VPC configuration
* Lab permissions are active

---

# Cleanup

After finishing:

1. End the lab
2. Delete resources if necessary
3. Close SSH sessions

---

# Summary

In this challenge lab, you successfully:

* Created an Amazon RDS database
* Connected using SSH
* Installed MySQL tools
* Created relational tables
* Inserted and queried records
* Performed INNER JOIN operations

---

# Author

AWS Cloud Lab Documentation Repository

Documented for GitHub learning and portfolio purposes.
