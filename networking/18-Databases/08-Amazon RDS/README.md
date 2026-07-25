# Amazon RDS and Aurora

## What You Will Learn

At the core of this lesson, you will learn how to:

- Provide an overview of Amazon Relational Database Service (Amazon RDS)
- Describe some of the options that Amazon RDS offers
- List the six database types on Amazon RDS
- Identify backup options for Amazon RDS
- Examine a few use cases for Amazon RDS
- Describe details about one Amazon RDS database type, Amazon Aurora
- Explore the key benefits of Aurora

---

# Key Terms

| Term | Description |
|---|---|
| Amazon RDS | Managed relational database service provided by AWS |
| DB instance | An isolated database environment running in the cloud |
| DB engine | The specific database software running on the instance |
| Aurora | High-performance relational database engine from AWS |
| Aurora cluster | Group of Aurora DB instances sharing storage |
| Cluster volume | Shared distributed storage used by Aurora |

---

# Overview of Amazon RDS

Amazon Relational Database Service (Amazon RDS) is a managed cloud database service provided by AWS. It simplifies the setup, operation, scaling, and maintenance of relational databases in the cloud.

With Amazon RDS, AWS handles many administrative tasks automatically, including:

- Hardware provisioning
- Database setup
- Backups
- Software patching
- Monitoring
- Scaling
- Recovery

This allows developers and database administrators to focus more on applications and less on infrastructure management.

---

# Benefits of Amazon RDS

## Fully Managed Service

AWS manages:

- Database installation
- Maintenance
- Updates
- Backup scheduling
- High availability configuration

---

## Scalability

You can:

- Increase storage
- Upgrade compute power
- Add read replicas
- Scale resources with minimal downtime

---

## Security

Amazon RDS supports:

- Encryption at rest
- Encryption in transit
- IAM integration
- Virtual Private Cloud (VPC) isolation
- Security groups

---

## High Availability

Amazon RDS supports Multi-AZ deployments that automatically create standby database replicas for failover protection.

---

# Amazon RDS Database Engines

Amazon RDS supports six major relational database engines:

| Database Engine | Description |
|---|---|
| MySQL | Popular open-source relational database |
| PostgreSQL | Advanced open-source object-relational database |
| MariaDB | Community-developed MySQL-compatible database |
| Oracle | Enterprise relational database system |
| Microsoft SQL Server | Relational database developed by Microsoft |
| Amazon Aurora | AWS-designed cloud-native relational database |

---

# Amazon RDS Deployment Options

## Single-AZ Deployment

- One database instance
- Lower cost
- Suitable for development and testing

---

## Multi-AZ Deployment

- Primary and standby database instances
- Automatic failover
- Improved reliability and disaster recovery

---

## Read Replicas

- Read-only copies of a database
- Improve application performance
- Reduce load on primary database

---

# Backup Options in Amazon RDS

Amazon RDS provides multiple backup mechanisms.

## Automated Backups

Automatically creates:

- Daily snapshots
- Transaction logs

Allows point-in-time recovery.

---

## Manual Snapshots

User-created backups that remain until manually deleted.

Useful for:

- Long-term backup
- Testing
- Migration

---

## Point-in-Time Recovery

Restores the database to a specific second within the backup retention period.

---

# Common Use Cases for Amazon RDS

## Web Applications

Applications requiring:

- User accounts
- Transactions
- Structured data

---

## Enterprise Applications

Business systems such as:

- ERP
- CRM
- Financial applications

---

## E-commerce Platforms

Supports:

- Product catalogs
- Customer information
- Orders and payments

---

## Analytics and Reporting

Can integrate with analytics tools for business reporting.

---

# Introduction to Amazon Aurora

Amazon Aurora is a cloud-native relational database engine developed by AWS.

Aurora is compatible with:

- MySQL
- PostgreSQL

It combines:

- Enterprise-level performance
- High availability
- Cost efficiency

---

# Aurora Architecture

## Aurora Cluster

An Aurora cluster consists of:

- One primary DB instance
- Multiple read replicas
- Shared cluster storage

---

## Cluster Volume

Aurora stores data in a distributed cluster volume that automatically replicates data across multiple Availability Zones.

This improves:

- Durability
- Fault tolerance
- Performance

---

# Key Benefits of Aurora

## High Performance

Aurora delivers:

- Up to 5× MySQL performance
- Up to 3× PostgreSQL performance

---

## Fault Tolerance

Aurora automatically replicates data across:

- Multiple Availability Zones
- Multiple storage nodes

---

## Automatic Scaling

Aurora storage automatically scales up to large capacities without downtime.

---

## Fast Recovery

Aurora recovers quickly after failures because it continuously backs up data to Amazon S3.

---

## Read Replicas

Aurora supports multiple read replicas for improved read performance.

---

# Comparing Amazon RDS and Aurora

| Feature | Amazon RDS | Amazon Aurora |
|---|---|---|
| Managed Service | Yes | Yes |
| Performance | Standard | Higher |
| Storage Scaling | Manual/Auto | Automatic |
| MySQL Compatibility | Yes | Yes |
| PostgreSQL Compatibility | Yes | Yes |
| Read Replicas | Supported | Enhanced |
| High Availability | Multi-AZ | Built-in |

---

# Example SQL Commands

## Create a Database

```sql
CREATE DATABASE world;