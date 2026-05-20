# Lab: Create Subnets and Allocate IP Addresses in Amazon VPC

## Lab Objective

In this lab, I learned how to create an Amazon Virtual Private Cloud (Amazon VPC), configure subnets, allocate IP address ranges using CIDR notation, and understand private IP addressing in AWS cloud networking.

---

# Scenario

As a Cloud Support Engineer at AWS, I assisted a startup customer who needed help creating a VPC environment in AWS.

The customer required:
- A VPC using a private `192.x.x.x` IP range
- Approximately 15,000 private IP addresses
- A public subnet with at least 50 available IP addresses
- Guidance on subnetting and CIDR allocation

---

# Services Used

- Amazon VPC
- Subnets
- Internet Gateway
- CIDR Block Addressing
- AWS Management Console

---

# Key Concepts Learned

- Virtual Private Cloud (VPC)
- CIDR notation
- Private IP address ranges
- Public subnets
- IP allocation
- Subnetting
- VPC networking design

---

# Understanding Amazon VPC

Amazon VPC is a logically isolated virtual network in AWS where cloud resources can be securely launched and managed.

A VPC allows:
- Custom IP address ranges
- Subnet creation
- Internet connectivity configuration
- Secure communication between AWS resources

---

# Private IP Address Ranges (RFC1918)

The recommended private IP ranges are:

| Private Range | CIDR |
|---|---|
| 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 |
| 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 |
| 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 |

---

# Why Private IP Addresses Are Used

Private IP addresses:
- Are not accessible from the public internet
- Improve security
- Prevent public routing conflicts
- Allow internal communication within the VPC

---

# CIDR Block Analysis

The customer required approximately 15,000 IP addresses.

To satisfy this requirement:
- A `/18` CIDR block was selected

Example:

```text
192.168.0.0/18
```

---

# Why /18 Was Chosen

A `/18` subnet provides:

| CIDR | Total IP Addresses |
|---|---|
| /18 | 16,384 |

This meets the customer's requirement for approximately 15,000 IP addresses.

---

# Public Subnet Configuration

The customer also required at least 50 IP addresses for the public subnet.

The following subnet CIDR was selected:

```text
192.168.1.0/26
```

---

# Why /26 Was Chosen

A `/26` subnet provides:

| CIDR | Total IP Addresses |
|---|---|
| /26 | 64 |

This satisfies the requirement for at least 50 IP addresses.

---

# VPC Configuration

| Setting | Value |
|---|---|
| VPC Name | First VPC |
| VPC CIDR | 192.168.0.0/18 |
| IPv6 CIDR | None |
| Subnet Name | Public subnet |
| Public Subnet CIDR | 192.168.1.0/26 |
| Availability Zone | No Preference |

---

# VPC Architecture

The architecture included:
- One VPC
- One public subnet
- Internet Gateway
- Public IP allocation capability

---

# Public and Private Subnets

## Public Subnet

A public subnet:
- Has internet access
- Uses an Internet Gateway
- Hosts publicly accessible resources

Examples:
- Web servers
- Bastion hosts

---

## Private Subnet

A private subnet:
- Does not allow direct internet access
- Is used for internal systems

Examples:
- Databases
- Internal applications

---

# Why Subnetting Matters

Subnetting helps:
- Organize networks
- Improve security
- Control traffic flow
- Efficiently allocate IP addresses

---

# Internet Gateway (IGW)

An Internet Gateway allows communication between:
- The VPC
- The public internet

Without an IGW:
- Resources inside the subnet cannot access the internet

---

# Steps Performed

## Step 1: Opened Amazon VPC Console

Navigated to:
- AWS Management Console
- Amazon VPC Dashboard

---

## Step 2: Launched VPC Wizard

Selected:
```text
VPC with a Single Public Subnet
```

---

## Step 3: Configured VPC

Configured:
- VPC CIDR block
- Public subnet CIDR block
- VPC name
- Subnet name

---

## Step 4: Created the VPC

AWS automatically created:
- VPC
- Public subnet
- Route table
- Internet Gateway

---

# Skills Practiced

- Creating Amazon VPCs
- CIDR block planning
- Subnetting
- IP allocation
- AWS networking design
- VPC architecture planning

---

# What I Learned

- VPCs provide isolated cloud networking environments
- CIDR notation determines available IP addresses
- Subnets divide networks into smaller sections
- Public subnets allow internet communication
- Private IP ranges are recommended for AWS VPCs
- Proper subnetting improves scalability and security

---

# Challenges

- Choosing the correct CIDR block size
- Understanding subnet calculations
- Determining available IP ranges
- Relating subnetting concepts to AWS networking

---

# Screenshots

