# AWS Lab: Configuring a Virtual Private Cloud (VPC)

## Overview

This lab demonstrates how to create a custom Amazon Virtual Private Cloud (VPC) with both public and private subnets. The lab also covers configuring networking components such as Internet Gateways, NAT Gateways, Route Tables, and Bastion Hosts to enable secure communication between resources.

## Objectives

By completing this lab, you will learn how to:

* Create a custom VPC
* Create public and private subnets
* Configure Internet Gateway connectivity
* Configure Route Tables
* Create and configure a NAT Gateway
* Launch a Bastion Host in a public subnet
* Connect securely to instances in a private subnet
* Test internet connectivity from a private subnet

---

# Architecture

```text
                    Internet
                        |
                +----------------+
                | Internet Gateway|
                +----------------+
                        |
         +-------------------------------+
         |           Lab VPC             |
         |        10.0.0.0/16            |
         +-------------------------------+
                 |                |
                 |                |
        Public Subnet      Private Subnet
         10.0.0.0/24        10.0.2.0/23
                 |                |
         Bastion Server     Private EC2
                 |
           NAT Gateway
```

---

# Task 1: Create a VPC

## Configuration

| Setting   | Value       |
| --------- | ----------- |
| Name      | Lab VPC     |
| IPv4 CIDR | 10.0.0.0/16 |
| IPv6      | None        |
| Tenancy   | Default     |

## Steps

1. Open **VPC Console**
2. Select **Your VPCs**
3. Click **Create VPC**
4. Choose **VPC only**
5. Configure:

   * Name: `Lab VPC`
   * CIDR: `10.0.0.0/16`
6. Create VPC
7. Enable DNS Hostnames

---

# Task 2: Create Subnets

## Public Subnet

| Setting | Value                   |
| ------- | ----------------------- |
| Name    | Public Subnet           |
| AZ      | First Availability Zone |
| CIDR    | 10.0.0.0/24             |

### Additional Configuration

Enable:

```text
Auto-assign Public IPv4 Address
```

---

## Private Subnet

| Setting | Value                   |
| ------- | ----------------------- |
| Name    | Private Subnet          |
| AZ      | First Availability Zone |
| CIDR    | 10.0.2.0/23             |

The private subnet covers:

```text
10.0.2.0 - 10.0.3.255
```

---

# Task 3: Create Internet Gateway

## Configuration

| Setting | Value   |
| ------- | ------- |
| Name    | Lab IGW |

## Steps

1. Open Internet Gateways
2. Create Internet Gateway
3. Name it:

```text
Lab IGW
```

4. Attach it to:

```text
Lab VPC
```

---

# Task 4: Configure Route Tables

## Rename Default Route Table

Rename the automatically created route table:

```text
Private Route Table
```

---

## Create Public Route Table

### Configuration

| Setting | Value              |
| ------- | ------------------ |
| Name    | Public Route Table |
| VPC     | Lab VPC            |

### Add Route

| Destination | Target           |
| ----------- | ---------------- |
| 0.0.0.0/0   | Internet Gateway |

Target:

```text
Lab IGW
```

### Associate Route Table

Associate:

```text
Public Subnet
```

with:

```text
Public Route Table
```

---

# Task 5: Launch Bastion Server

## EC2 Configuration

| Setting       | Value             |
| ------------- | ----------------- |
| Name          | Bastion Server    |
| AMI           | Amazon Linux 2023 |
| Instance Type | t3.micro          |
| Key Pair      | None              |
| VPC           | Lab VPC           |
| Subnet        | Public Subnet     |
| Public IP     | Enabled           |

---

## Security Group

### Name

```text
Bastion Security Group
```

### Inbound Rules

| Type | Source   |
| ---- | -------- |
| SSH  | Anywhere |

---

# Task 6: Create NAT Gateway

## Configuration

| Setting    | Value           |
| ---------- | --------------- |
| Name       | Lab NAT Gateway |
| Subnet     | Public Subnet   |
| Elastic IP | Allocate New    |

---

## Update Private Route Table

Add:

| Destination | Target      |
| ----------- | ----------- |
| 0.0.0.0/0   | NAT Gateway |

This allows instances in the private subnet to access the internet without being publicly accessible.

---

# Optional Challenge

## Launch Private EC2 Instance

### Configuration

| Setting   | Value             |
| --------- | ----------------- |
| Name      | Private Instance  |
| AMI       | Amazon Linux 2023 |
| Type      | t3.micro          |
| Subnet    | Private Subnet    |
| Public IP | Disabled          |

---

## Security Group

### Name

```text
Private Instance SG
```

### Inbound Rule

| Type | Source      |
| ---- | ----------- |
| SSH  | 10.0.0.0/16 |

---

## User Data

```bash
#!/bin/bash

echo 'lab-password' | passwd ec2-user --stdin

sed -i 's|[#]*PasswordAuthentication no|PasswordAuthentication yes|g' /etc/ssh/sshd_config

systemctl restart sshd.service
```

---

# Connect to Bastion Server

1. Open EC2 Console
2. Select Bastion Server
3. Click:

```text
Connect
```

4. Use:

```text
EC2 Instance Connect
```

---

# Connect to Private Instance

From Bastion Host:

```bash
ssh PRIVATE-IP
```

Example:

```bash
ssh 10.0.2.123
```

Accept host key:

```text
yes
```

Password:

```text
lab-password
```

---

# Test NAT Gateway

From the private instance run:

```bash
ping -c 3 amazon.com
```

Expected output:

```text
64 bytes from amazon.com ...
```

Successful responses confirm:

* NAT Gateway works
* Private subnet has outbound internet access
* Route tables are configured correctly

---

# Key Concepts Learned

## Public Subnet

* Has route to Internet Gateway
* Can receive public IPs
* Internet accessible

## Private Subnet

* No direct internet access
* Uses NAT Gateway for outbound traffic

## Internet Gateway (IGW)

Provides inbound and outbound internet connectivity.

## NAT Gateway

Allows private instances to:

* Access software updates
* Download packages
* Reach internet services

Without exposing them publicly.

## Bastion Host

Acts as a secure jump server to access private resources.

---

# Verification Checklist

* [x] Created custom VPC
* [x] Created Public Subnet
* [x] Created Private Subnet
* [x] Attached Internet Gateway
* [x] Created Public Route Table
* [x] Associated Public Subnet
* [x] Created NAT Gateway
* [x] Updated Private Route Table
* [x] Launched Bastion Server
* [x] Connected to Bastion Host
* [x] Connected to Private Instance
* [x] Verified Internet Access Through NAT Gateway

---

# AWS Services Used

* Amazon VPC
* Amazon EC2
* Internet Gateway
* NAT Gateway
* Route Tables
* Security Groups
* EC2 Instance Connect

---

# Lab Outcome

Successfully built a secure AWS network architecture consisting of:

* One VPC
* One Public Subnet
* One Private Subnet
* Internet Gateway
* NAT Gateway
* Bastion Host
* Private EC2 Instance

and verified secure connectivity between all components.
