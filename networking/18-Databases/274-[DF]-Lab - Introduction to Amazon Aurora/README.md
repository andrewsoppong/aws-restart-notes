# AWS Database & Management Labs Documentation

Author: Andrews Oppong  
Platform: AWS Academy / AWS Labs  
Purpose: Personal GitHub Documentation Repository

---

# Table of Contents

1. Amazon RDS and Aurora Overview
2. Introduction to Amazon DynamoDB
3. Install and Configure the AWS CLI
4. Using AWS Systems Manager
5. Introduction to Amazon Aurora

---

# 1. Amazon RDS and Aurora Overview

## Overview

This lab introduces Amazon Relational Database Service (Amazon RDS) and Amazon Aurora. You will learn how managed relational databases work in AWS and explore database engines, backup options, and Aurora architecture.

---

## Objectives

After completing this lab, you will be able to:

- Explain Amazon RDS
- Describe Amazon RDS database options
- Identify supported database engines
- Understand Amazon RDS backup options
- Explore Amazon Aurora architecture and benefits

---

## Key Terms

- Amazon RDS
- DB Instance
- DB Engine
- Aurora
- Aurora Cluster
- Cluster Volume

---

## Amazon RDS Overview

Amazon RDS is a managed relational database service that simplifies:

- Database provisioning
- Scaling
- Backups
- Patching
- Monitoring
- High availability

### Supported Database Engines

Amazon RDS supports:

1. Aurora
2. MySQL
3. PostgreSQL
4. MariaDB
5. Oracle
6. Microsoft SQL Server

---

## Amazon Aurora Overview

Amazon Aurora is a MySQL and PostgreSQL-compatible relational database engine designed for:

- High performance
- Scalability
- Reliability
- Cost efficiency

### Aurora Benefits

- Up to 5x MySQL performance
- Automated backups
- High availability
- Fault-tolerant storage
- Automatic failover
- Scalability

---

## Backup Options

### Automated Backups

- Point-in-time recovery
- Automatic snapshots

### Manual Snapshots

- User-managed backups
- Long-term retention

---

## Aurora Architecture

### Aurora Cluster Components

- Writer Instance
- Reader Instances
- Cluster Volume

### Endpoints

#### Writer Endpoint

Used for:
- INSERT
- UPDATE
- DELETE
- DDL operations

#### Reader Endpoint

Used for:
- Read-only queries
- Load balancing

---

## Conclusion

In this lab, you learned:

- Amazon RDS fundamentals
- Supported database engines
- Backup options
- Aurora architecture
- Aurora benefits and use cases

---

# 2. Introduction to Amazon DynamoDB

## Overview

Amazon DynamoDB is a fully managed NoSQL database service that provides:

- Fast performance
- Single-digit millisecond latency
- Automatic scaling
- High availability

This lab demonstrates how to create and manage a DynamoDB table.

---

## Objectives

After completing this lab, you will be able to:

- Create a DynamoDB table
- Insert data into a table
- Query table data
- Modify table items
- Delete a table

---

## Services Used

- Amazon DynamoDB

---

# Task 1: Create a DynamoDB Table

## Steps

1. Open the AWS Management Console
2. Navigate to **DynamoDB**
3. Choose **Create table**

### Configuration

| Setting | Value |
|---|---|
| Table Name | Music |
| Partition Key | Artist |
| Sort Key | Song |

4. Choose **Create table**

---

# Task 2: Add Data to the Table

## First Item

| Attribute | Value |
|---|---|
| Artist | Pink Floyd |
| Song | Money |
| Album | The Dark Side of the Moon |
| Year | 1973 |

---

## Second Item

| Attribute | Value |
|---|---|
| Artist | John Lennon |
| Song | Imagine |
| Album | Imagine |
| Year | 1971 |
| Genre | Soft rock |

---

## Third Item

| Attribute | Value |
|---|---|
| Artist | Psy |
| Song | Gangnam Style |
| Album | Psy 6 (Six Rules), Part 1 |
| Year | 2011 |
| LengthSeconds | 219 |

---

# Task 3: Modify an Existing Item

## Steps

1. Open the Music table
2. Choose **Explore Items**
3. Select the item for **Psy**
4. Change:

```text
Year: 2011 → 2012
```

5. Save changes

---

# Task 4: Query the Table

## Query by Primary Key

```text
Artist: Psy
Song: Gangnam Style
```

## Scan Example

Filter by:

```text
Year = 1971
```

---

# Task 5: Delete the Table

## Steps

1. Select the Music table
2. Choose:

```text
Actions → Delete table
```

3. Enter:

```text
delete
```

4. Confirm deletion

---

## Key Concepts Learned

### Table
Collection of items

### Item
Equivalent to a row

### Attribute
Equivalent to a column

### Partition Key
Primary identifier

### Sort Key
Secondary identifier

---

## Conclusion

You successfully:

- Created a DynamoDB table
- Inserted data
- Queried items
- Updated items
- Deleted the table

---

# 3. Install and Configure the AWS CLI

## Overview

This lab demonstrates how to install and configure the AWS Command Line Interface (AWS CLI) on a Red Hat Linux EC2 instance.

---

## Objectives

After completing this lab, you will be able to:

- Install AWS CLI
- Configure AWS CLI
- Connect AWS CLI to AWS
- Use AWS CLI with IAM

---

## Services Used

- Amazon EC2
- AWS CLI
- IAM

---

# Task 1: Connect to EC2 Instance

## Linux/macOS SSH Command

```bash
ssh -i labsuser.pem ec2-user@<PUBLIC-IP>
```

---

# Task 2: Install AWS CLI

## Download AWS CLI

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
```

## Extract Installer

```bash
unzip -u awscliv2.zip
```

## Install AWS CLI

```bash
sudo ./aws/install
```

## Verify Installation

```bash
aws --version
```

---

# Task 3: Configure AWS CLI

## Run Configuration Wizard

```bash
aws configure
```

### Example Inputs

| Setting | Example |
|---|---|
| AWS Access Key ID | Provided by lab |
| AWS Secret Access Key | Provided by lab |
| Region | us-west-2 |
| Output Format | json |

---

# Task 4: Test AWS CLI

## List IAM Users

```bash
aws iam list-users
```

---

# Challenge Solution

## List Local Policies

```bash
aws iam list-policies --scope Local
```

## Download Policy JSON

```bash
aws iam get-policy-version \
--policy-arn arn:aws:iam::ACCOUNT-ID:policy/lab_policy \
--version-id v1 > lab_policy.json
```

---

## Key Concepts Learned

- AWS CLI installation
- IAM integration
- CLI authentication
- IAM policy retrieval

---

## Conclusion

You successfully:

- Installed AWS CLI
- Configured AWS credentials
- Used AWS CLI commands
- Downloaded IAM policies

---

# 4. Using AWS Systems Manager

## Overview

AWS Systems Manager helps manage and automate AWS infrastructure operations.

This lab demonstrates how to:

- Manage EC2 instances
- Run commands remotely
- Store configuration values
- Access instances securely

---

## Objectives

After completing this lab, you will be able to:

- Verify configurations and permissions
- Run tasks remotely
- Update application settings
- Access EC2 instances securely

---

## Services Used

- AWS Systems Manager
- Fleet Manager
- Run Command
- Parameter Store
- Session Manager
- Amazon EC2

---

# Task 1: Generate Inventory Lists

## Steps

1. Open **Systems Manager**
2. Navigate to:

```text
Fleet Manager
```

3. Choose:

```text
Set up inventory
```

4. Configure:

| Setting | Value |
|---|---|
| Name | Inventory-Association |
| Target | Managed Instance |

5. Choose:

```text
Setup Inventory
```

---

# Task 2: Install Application Using Run Command

## Steps

1. Open:

```text
Run Command
```

2. Choose the custom document
3. Select:

```text
Managed Instance
```

4. Run the command

### Installed Components

- Apache
- PHP
- AWS SDK
- Widget Dashboard

---

# Task 3: Use Parameter Store

## Create Parameter

| Setting | Value |
|---|---|
| Name | /dashboard/show-beta-features |
| Value | True |

---

## Result

Refreshing the application enables beta features.

---

# Task 4: Use Session Manager

## Start Session

1. Open:

```text
Session Manager
```

2. Choose:

```text
Start session
```

3. Select the managed instance

---

## Example Commands

### List Web Files

```bash
ls /var/www/html
```

### Describe EC2 Instances

```bash
aws ec2 describe-instances
```

---

## Benefits of Session Manager

- No SSH required
- No open inbound ports
- Secure access
- Auditable sessions

---

## Conclusion

You successfully:

- Collected inventory data
- Installed applications remotely
- Managed application settings
- Accessed instances securely

---

# 5. Introduction to Amazon Aurora

## Overview

This lab introduces Amazon Aurora and demonstrates how to:

- Create an Aurora database
- Connect from EC2
- Configure database access
- Run SQL queries

---

## Objectives

After completing this lab, you will be able to:

- Create an Aurora instance
- Connect using EC2
- Configure MariaDB client
- Query Aurora databases

---

## Services Used

- Amazon Aurora
- Amazon RDS
- Amazon EC2
- AWS Systems Manager

---

# Task 1: Create an Aurora Database

## Configuration

| Setting | Value |
|---|---|
| Creation Method | Standard Create |
| Engine Type | Aurora MySQL Compatible |
| Version | MySQL 8.0 |
| Template | Dev/Test |
| DB Identifier | aurora |
| Username | admin |
| Password | admin123 |

---

## Networking Configuration

| Setting | Value |
|---|---|
| VPC | LabVPC |
| Subnet Group | dbsubnetgroup |
| Public Access | No |
| Security Group | DBSecurityGroup |

---

## Additional Settings

| Setting | Value |
|---|---|
| Initial Database | world |
| Encryption | Disabled |
| Enhanced Monitoring | Disabled |

---

# Task 2: Connect to EC2

## Steps

1. Open EC2 Console
2. Select:

```text
Command Host
```

3. Choose:

```text
Connect → Session Manager
```

---

# Task 3: Install MariaDB Client

## Install Command

```bash
sudo yum install mariadb -y
```

---

# Task 4: Connect to Aurora

## MySQL Connection Command

```bash
mysql -u admin --password='admin123' -h <AURORA-ENDPOINT>
```

---

# Task 5: Query Aurora Database

## Show Databases

```sql
SHOW DATABASES;
```

---

## Use Database

```sql
USE world;
```

---

## Create Table

```sql
CREATE TABLE country (
  Code CHAR(3) NOT NULL,
  Name CHAR(52) NOT NULL,
  Population INT(11) NOT NULL,
  PRIMARY KEY (Code)
);
```

---

## Insert Data

```sql
INSERT INTO country VALUES ('AUS','Australia',18886000);
```

---

## Query Data

```sql
SELECT * FROM country;
```

---

## Aurora Endpoints

### Writer Endpoint

Used for:

- INSERT
- UPDATE
- DELETE

### Reader Endpoint

Used for:

- Read-only queries
- Load balancing

---

## Key Concepts Learned

- Aurora cluster creation
- EC2 database connectivity
- SQL database management
- Aurora endpoints
- MariaDB client usage

---

## Conclusion

You successfully:

- Created an Aurora instance
- Connected from EC2
- Configured MariaDB client
- Queried Aurora databases