# Migrating to Amazon RDS

## Lab Overview

In this lab, the café web application is migrated from a locally hosted MariaDB database running on an Amazon EC2 instance to a fully managed Amazon Relational Database Service (Amazon RDS) MariaDB database instance.

The migration includes:

- Creating an Amazon RDS MariaDB instance using AWS CLI
- Creating private subnets and a database subnet group
- Configuring database security groups
- Exporting and importing existing database data
- Updating application configuration to use Amazon RDS
- Monitoring database performance with Amazon CloudWatch

---

## Architecture

### Initial Architecture

```text
Internet
    |
    v
+------------------------+
| Cafe EC2 Instance      |
|------------------------|
| Apache                 |
| PHP Application        |
| MariaDB Database       |
+------------------------+

+------------------------+
| CLI Host EC2 Instance  |
+------------------------+
```

### Final Architecture

```text
Internet
    |
    v
+------------------------+
| Cafe EC2 Instance      |
|------------------------|
| Apache                 |
| PHP Application        |
+------------------------+
           |
           |
           v
+------------------------+
| Amazon RDS MariaDB     |
+------------------------+

+------------------------+
| CLI Host EC2 Instance  |
+------------------------+
```

---

# Objectives

After completing this lab, you will be able to:

- Create an Amazon RDS MariaDB instance using AWS CLI
- Configure networking resources for RDS
- Migrate a MariaDB database from EC2 to Amazon RDS
- Update application configuration using AWS Systems Manager Parameter Store
- Verify application functionality after migration
- Monitor Amazon RDS performance using CloudWatch

---

# Prerequisites

Before beginning:

- Start the lab environment
- Open the AWS Management Console
- Record the following values from the lab details page:

```text
AccessKey
SecretKey
LabRegion
CafeInstanceURL
CafeVpcID
CafeSecurityGroupID
CafeInstanceAZ
```

---

# Task 1: Generate Sample Data

## Open the Café Application

Navigate to:

```text
http://<CafeInstanceURL>/cafe
```

## Place Orders

1. Open the Menu page.
2. Add at least one of each menu item.
3. Submit the order.

## Verify Order History

1. Open Order History.
2. Record the number of orders.

This data will be migrated later.

---

# Task 2: Create Amazon RDS Infrastructure

## Connect to CLI Host

Navigate to:

```text
EC2 → Instances
```

Select:

```text
CLI Host
```

Choose:

```text
Connect → EC2 Instance Connect
```

---

## Configure AWS CLI

```bash
aws configure
```

Provide:

```text
AWS Access Key ID
AWS Secret Access Key
Default Region
json
```

---

## Create Database Security Group

```bash
aws ec2 create-security-group \
--group-name CafeDatabaseSG \
--description "Security group for Cafe database" \
--vpc-id <CafeVpcID>
```

Save the returned:

```text
GroupId
```

---

## Create MySQL Access Rule

```bash
aws ec2 authorize-security-group-ingress \
--group-id <CafeDatabaseSG-ID> \
--protocol tcp \
--port 3306 \
--source-group <CafeSecurityGroupID>
```

Verify:

```bash
aws ec2 describe-security-groups \
--filters Name=group-name,Values='CafeDatabaseSG'
```

---

# Create Private Subnets

## Private Subnet 1

```bash
aws ec2 create-subnet \
--vpc-id <CafeVpcID> \
--cidr-block 10.200.2.0/23 \
--availability-zone <CafeInstanceAZ>
```

Save:

```text
SubnetId
```

---

## Private Subnet 2

Use a different Availability Zone.

```bash
aws ec2 create-subnet \
--vpc-id <CafeVpcID> \
--cidr-block 10.200.10.0/23 \
--availability-zone us-west-2b
```

Save:

```text
SubnetId
```

---

# Create Database Subnet Group

```bash
aws rds create-db-subnet-group \
--db-subnet-group-name "CafeDB Subnet Group" \
--db-subnet-group-description "DB subnet group for Cafe" \
--subnet-ids <Subnet1> <Subnet2> \
--tags Key=Name,Value=CafeDatabaseSubnetGroup
```

---

# Create Amazon RDS MariaDB Instance

```bash
aws rds create-db-instance \
--db-instance-identifier CafeDBInstance \
--engine mariadb \
--engine-version 10.11.11 \
--db-instance-class db.t3.micro \
--allocated-storage 20 \
--availability-zone <CafeInstanceAZ> \
--db-subnet-group-name "CafeDB Subnet Group" \
--vpc-security-group-ids <CafeDatabaseSG-ID> \
--no-publicly-accessible \
--master-username root \
--master-user-password 'Re:Start!9'
```

---

## Monitor Creation

```bash
aws rds describe-db-instances \
--db-instance-identifier CafeDBInstance \
--query "DBInstances[*].[Endpoint.Address,AvailabilityZone,PreferredBackupWindow,BackupRetentionPeriod,DBInstanceStatus]"
```

Wait until:

```text
available
```

Record:

```text
RDS Endpoint Address
```

Example:

```text
cafedbinstance.xxxxxx.us-west-2.rds.amazonaws.com
```

---

# Task 3: Migrate Database

## Connect to CafeInstance

Use EC2 Instance Connect.

---

## Create Database Backup

```bash
mysqldump \
--user=root \
--password='Re:Start!9' \
--databases cafe_db \
--add-drop-database \
> cafedb-backup.sql
```

Verify:

```bash
less cafedb-backup.sql
```

Press `q` to exit.

---

## Download RDS SSL Certificate

```bash
curl -o global-bundle.pem \
https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem
```

---

## Restore Database to Amazon RDS

```bash
mysql \
--user=root \
--password='Re:Start!9' \
--host=<RDS-ENDPOINT> \
--ssl-ca=./global-bundle.pem \
< cafedb-backup.sql
```

---

## Verify Migration

Connect:

```bash
mysql \
--user=root \
--password='Re:Start!9' \
--host=<RDS-ENDPOINT> \
--ssl-ca=./global-bundle.pem \
cafe_db
```

Run:

```sql
select * from product;
```

Verify records exist.

Exit:

```sql
exit
```

---

# Task 4: Update Application Configuration

Navigate to:

```text
Systems Manager → Parameter Store
```

Open:

```text
/cafe/dbUrl
```

Choose:

```text
Edit
```

Replace the value with:

```text
<RDS Endpoint Address>
```

Save changes.

---

# Verify Website

Open:

```text
http://<CafeInstanceURL>/cafe
```

Check:

```text
Order History
```

Verify:

- Previous orders are visible
- New orders can be created

---

# Task 5: Monitor Amazon RDS

Navigate to:

```text
RDS → Databases → CafeDBInstance
```

Open:

```text
Monitoring
```

Available metrics include:

- CPUUtilization
- DatabaseConnections
- FreeStorageSpace
- FreeableMemory
- ReadIOPS
- WriteIOPS

---

## Test DatabaseConnections Metric

Connect to RDS:

```bash
mysql \
--user=root \
--password='Re:Start!9' \
--host=<RDS-ENDPOINT> \
--ssl-ca=./global-bundle.pem \
cafe_db
```

Run:

```sql
select * from product;
```

Observe:

```text
DatabaseConnections = 1
```

Exit:

```sql
exit
```

After approximately one minute:

```text
DatabaseConnections = 0
```

---

# Key AWS Services Used

| Service | Purpose |
|----------|----------|
| Amazon EC2 | Hosts café application |
| Amazon RDS | Managed MariaDB database |
| Amazon VPC | Network isolation |
| Security Groups | Database access control |
| AWS CLI | Resource provisioning |
| Systems Manager Parameter Store | Application configuration |
| Amazon CloudWatch | Monitoring and metrics |

---

# Lab Summary

Successfully completed:

- Created an Amazon RDS MariaDB instance
- Built database networking components
- Migrated data from EC2 MariaDB to Amazon RDS
- Updated application configuration
- Verified application functionality
- Monitored RDS using CloudWatch

---

## Outcome

The café application now uses a fully managed Amazon RDS MariaDB database, improving:

- Availability
- Scalability
- Backup management
- Monitoring
- Operational efficiency
- Security
- Maintainability