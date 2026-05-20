# Build Your VPC and Launch a Web Server

## Overview

In this lab, you will create a fully functional Amazon Virtual Private Cloud (VPC) environment from scratch. You will configure:

- Public and private subnets
- Route tables
- Internet Gateway
- NAT Gateway
- Security groups
- Amazon EC2 instance
- Apache Web Server

At the end of the lab, you will have a working web server hosted inside your custom AWS VPC.

---

# Lab Objectives

After completing this lab, you will be able to:

- Create a Virtual Private Cloud (VPC)
- Create public and private subnets
- Configure route tables
- Configure security groups
- Launch an Amazon EC2 instance
- Install and run Apache Web Server
- Verify web server accessibility

---

# Duration

Estimated Time: **45 Minutes**

---

# Architecture Diagram

```text
                         AWS CLOUD
┌──────────────────────────────────────────────────────┐
│                                                      │
│                   Lab VPC                            │
│                 10.0.0.0/16                          │
│                                                      │
│   ┌──────────────────────────────────────────────┐   │
│   │              Internet Gateway               │   │
│   └──────────────────────────────────────────────┘   │
│                         │                            │
│                Public Route Table                   │
│                         │                            │
│      ┌───────────────────────────────┐              │
│      │                               │              │
│ Public Subnet 1              Public Subnet 2        │
│ 10.0.0.0/24                  10.0.2.0/24            │
│                                      │               │
│                                      │               │
│                              EC2 Web Server          │
│                              Apache HTTPD            │
│                                                      │
│                                                      │
│                Private Route Table                   │
│                         │                            │
│      ┌───────────────────────────────┐              │
│      │                               │              │
│ Private Subnet 1             Private Subnet 2       │
│ 10.0.1.0/24                  10.0.3.0/24            │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

# AWS Services Used

- Amazon VPC
- Amazon EC2
- Security Groups
- Route Tables
- Internet Gateway
- NAT Gateway

---

# Task 1 — Create Your VPC

## Step 1: Open the VPC Console

1. Sign in to AWS Management Console
2. Search for **VPC**
3. Open the **VPC Dashboard**

---

## Step 2: Create the VPC

Click:

```text
Create VPC
```

Configure the following settings:

| Setting | Value |
|---|---|
| Resources to create | VPC and more |
| Name tag auto-generation | Disabled |
| IPv4 CIDR | 10.0.0.0/16 |
| IPv6 CIDR | No IPv6 CIDR |
| Tenancy | Default |
| Number of AZs | 1 |
| Public subnets | 1 |
| Private subnets | 1 |
| NAT gateways | In 1 AZ |
| VPC endpoints | None |

---

## Customize Subnet CIDR Blocks

### Public Subnet

| Setting | Value |
|---|---|
| CIDR | 10.0.0.0/24 |

### Private Subnet

| Setting | Value |
|---|---|
| CIDR | 10.0.1.0/24 |

---

## Configure Resource Names

| Resource | Name |
|---|---|
| VPC | Lab VPC |
| Public Subnet | Public Subnet 1 |
| Private Subnet | Private Subnet 1 |
| Public Route Table | Public Route Table |
| Private Route Table | Private Route Table |

Click:

```text
Create VPC
```

Then choose:

```text
View VPC
```

---

# Task 2 — Create Additional Subnets

Navigate to:

```text
VPC → Subnets
```

---

## Create Public Subnet 2

Click:

```text
Create subnet
```

Configure:

| Setting | Value |
|---|---|
| VPC | Lab VPC |
| Subnet name | Public Subnet 2 |
| Availability Zone | No preference |
| IPv4 CIDR block | 10.0.2.0/24 |

Click:

```text
Create subnet
```

---

## Create Private Subnet 2

Again click:

```text
Create subnet
```

Configure:

| Setting | Value |
|---|---|
| VPC | Lab VPC |
| Subnet name | Private Subnet 2 |
| Availability Zone | No preference |
| IPv4 CIDR block | 10.0.3.0/24 |

Click:

```text
Create subnet
```

---

# Task 3 — Associate Route Tables

Navigate to:

```text
VPC → Route Tables
```

---

## Associate Public Subnet 2

Select:

```text
Public Route Table
```

Open:

```text
Subnet Associations
```

Click:

```text
Edit subnet associations
```

Select:

```text
Public Subnet 2
```

Save associations.

---

## Associate Private Subnet 2

Select:

```text
Private Route Table
```

Open:

```text
Subnet Associations
```

Click:

```text
Edit subnet associations
```

Select:

```text
Private Subnet 2
```

Save associations.

---

# Route Table Configuration

## Public Route Table

| Destination | Target |
|---|---|
| 0.0.0.0/0 | Internet Gateway |
| 10.0.0.0/16 | Local |

---

## Private Route Table

| Destination | Target |
|---|---|
| 0.0.0.0/0 | NAT Gateway |
| 10.0.0.0/16 | Local |

---

# Task 4 — Create a Security Group

Navigate to:

```text
VPC → Security Groups
```

Click:

```text
Create security group
```

Configure:

| Setting | Value |
|---|---|
| Security group name | Web Security Group |
| Description | Enable HTTP access |
| VPC | Lab VPC |

---

## Add Inbound Rule

Click:

```text
Add rule
```

Configure:

| Type | Protocol | Port | Source |
|---|---|---|---|
| HTTP | TCP | 80 | 0.0.0.0/0 |

Description:

```text
Permit web requests
```

Click:

```text
Create security group
```

---

# Task 5 — Launch a Web Server

## Open EC2 Console

Search for:

```text
EC2
```

Navigate to:

```text
Instances
```

Click:

```text
Launch Instance
```

---

# Configure EC2 Instance

## Basic Configuration

| Setting | Value |
|---|---|
| Name | Web Server 1 |
| AMI | Amazon Linux 2 |
| Instance Type | t3.micro |
| Key Pair | vockey |

---

# Configure Network Settings

Click:

```text
Edit
```

Configure:

| Setting | Value |
|---|---|
| VPC | Lab VPC |
| Subnet | Public Subnet 2 |
| Auto-assign Public IP | Enable |
| Firewall | Select existing security group |
| Security Group | Web Security Group |

---

# Configure User Data

Paste the following script under:

```text
Advanced Details → User Data
```

```bash
#!/bin/bash

# Install Apache Web Server and PHP
yum install -y httpd mysql php

# Download Lab Files
wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-RESTRT-1/267-lab-NF-build-vpc-web-server/s3/lab-app.zip

# Extract Website Files
unzip lab-app.zip -d /var/www/html/

# Enable Apache Service
chkconfig httpd on

# Start Apache Service
service httpd start
```

Click:

```text
Launch instance
```

---

# Verify the Instance

Wait until:

```text
2/2 checks passed
```

appears in the status checks column.

---

# Access the Web Server

1. Select the EC2 instance
2. Open the **Details** tab
3. Copy:

```text
Public IPv4 DNS
```

4. Open a browser
5. Paste the DNS address
6. Press Enter

---

# Expected Output

You should see the Apache web page successfully loaded in the browser.

---

# Security Group Configuration

Your security group should contain:

| Type | Protocol | Port | Source |
|---|---|---|---|
| HTTP | TCP | 80 | 0.0.0.0/0 |

---

# Important Concepts

## Internet Gateway

Allows communication between the VPC and the internet.

---

## NAT Gateway

Allows instances in private subnets to access the internet securely.

---

## Public Subnet

A subnet with a route to the internet gateway.

---

## Private Subnet

A subnet without direct internet access.

---

# Common Troubleshooting

## Problem: Website Not Loading

### Possible Causes

- HTTP rule missing in security group
- Apache service not running
- Wrong subnet association
- Missing internet gateway route
- Public IP not enabled
- Route table misconfiguration

---

# Troubleshooting Commands

## Check Apache Status

```bash
sudo systemctl status httpd
```

---

## Start Apache

```bash
sudo systemctl start httpd
```

---

## Enable Apache at Boot

```bash
sudo systemctl enable httpd
```

---

## Test Apache Locally

```bash
curl localhost
```

If HTML output appears, Apache is running correctly.

---

# Verify Apache Listening on Port 80

```bash
sudo ss -tulpn | grep httpd
```

Expected output:

```text
tcp LISTEN 0 128 *:80 *:*
```

---

# Verify Security Group Rules

Inbound rules should include:

| Type | Port |
|---|---|
| HTTP | 80 |
| HTTPS | 443 |
| SSH | 22 |

Source should be:

```text
0.0.0.0/0
```

---

# Verify Route Table

Public route table should contain:

| Destination | Target |
|---|---|
| 0.0.0.0/0 | igw-xxxxxxxx |

---

# Verify Network ACL

Inbound:

| Rule | Source | Allow/Deny |
|---|---|---|
| All Traffic | 0.0.0.0/0 | Allow |

Outbound:

| Rule | Destination | Allow/Deny |
|---|---|---|
| All Traffic | 0.0.0.0/0 | Allow |

---

# Final Architecture

```text
Internet
   │
   ▼
Internet Gateway
   │
   ▼
Public Route Table
   │
   ▼
Public Subnet
   │
   ▼
EC2 Web Server
   │
   ▼
Apache HTTPD
```

---

# Key Learning Outcomes

By completing this lab, you learned how to:

- Build a VPC from scratch
- Configure public and private networking
- Configure route tables
- Create security groups
- Launch EC2 instances
- Install Apache web server
- Troubleshoot web server connectivity
- Verify AWS networking configurations

---

# Conclusion

In this lab, you successfully:

- Created a custom VPC
- Created public and private subnets
- Configured route tables
- Configured security groups
- Launched an EC2 web server
- Installed Apache
- Verified web server accessibility
- Understood AWS networking fundamentals
