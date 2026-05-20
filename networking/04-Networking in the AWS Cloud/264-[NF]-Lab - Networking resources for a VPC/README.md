# Lab: Creating Networking Resources in an Amazon VPC

## Lab Objective

In this lab, I learned how to build a fully routable Virtual Private Cloud (VPC) environment in AWS by creating networking resources such as:
- VPC
- Subnet
- Internet Gateway
- Route Table
- Network ACL
- Security Group
- EC2 Instance

The lab was successful once internet connectivity was verified using the `ping` command.

---

# Scenario

As a Cloud Support Engineer at AWS, I assisted a startup customer who could not connect their VPC to the internet.

The customer had:
- A VPC
- A public subnet
- An EC2 instance

However, the EC2 instance could not ping outside the VPC.

The goal was to:
- Build all required networking resources
- Configure routing correctly
- Enable internet connectivity

---

# Services Used

- Amazon VPC
- Internet Gateway (IGW)
- Route Tables
- Subnets
- Security Groups
- Network ACLs (NACLs)
- Amazon EC2

---

# Key Networking Concepts Learned

- VPC architecture
- Public subnet configuration
- Internet routing
- Route tables
- Internet Gateway (IGW)
- Security Groups
- Network ACLs
- Stateful vs Stateless firewalls
- Public IP addressing
- Internet connectivity testing

---

# Amazon VPC Overview

Amazon VPC is a logically isolated virtual network in AWS where resources can securely communicate.

A VPC allows:
- Custom IP ranges
- Subnet creation
- Route management
- Internet connectivity
- Traffic filtering

---

# VPC Configuration

| Resource | Configuration |
|---|---|
| VPC Name | Test VPC |
| VPC CIDR | 192.168.0.0/18 |
| Public Subnet CIDR | 192.168.1.0/28 |

---

# Components Created

## 1. Virtual Private Cloud (VPC)

Created:
```text
Test VPC
```

CIDR Block:
```text
192.168.0.0/18
```

Purpose:
- Provides isolated networking environment
- Hosts AWS resources securely

---

## 2. Public Subnet

Created:
```text
Public subnet
```

CIDR Block:
```text
192.168.1.0/28
```

Purpose:
- Hosts internet-accessible resources
- Allows public communication

---

# Understanding CIDR Blocks

## VPC CIDR

```text
192.168.0.0/18
```

Provides:
- 16,384 IP addresses

---

## Subnet CIDR

```text
192.168.1.0/28
```

Provides:
- 16 total IP addresses

---

# Internet Gateway (IGW)

Created:
```text
IGW test VPC
```

Purpose:
- Connects the VPC to the internet
- Enables outbound and inbound internet communication

The IGW was attached to:
```text
Test VPC
```

---

# Route Table

Created:
```text
Public route table
```

Purpose:
- Directs network traffic

---

# Route Added

| Destination | Target |
|---|---|
| 0.0.0.0/0 | Internet Gateway |

Meaning:
- Any traffic destined for the internet is sent to the IGW

---

# Route Table Association

The route table was associated with:
```text
Public subnet
```

This allowed subnet traffic to use the internet route.

---

# Network ACL (NACL)

Created:
```text
Public Subnet NACL
```

Purpose:
- Controls traffic at the subnet level

---

# NACL Rules

## Inbound Rule

| Rule # | Type | Source | Allow/Deny |
|---|---|---|---|
| 100 | All Traffic | 0.0.0.0/0 | Allow |

---

## Outbound Rule

| Rule # | Type | Destination | Allow/Deny |
|---|---|---|---|
| 100 | All Traffic | 0.0.0.0/0 | Allow |

---

# Understanding NACLs

Network ACLs are:
- Stateless
- Applied at subnet level
- Used to allow or deny traffic

If traffic is allowed inbound, outbound must also be allowed separately.

---

# Security Group

Created:
```text
public security group
```

Purpose:
- Acts as a virtual firewall for EC2 instances

---

# Inbound Rules Configured

| Type | Protocol | Port | Source |
|---|---|---|---|
| SSH | TCP | 22 | 0.0.0.0/0 |
| HTTP | TCP | 80 | 0.0.0.0/0 |
| HTTPS | TCP | 443 | 0.0.0.0/0 |

---

# Outbound Rules

| Type | Destination |
|---|---|
| All Traffic | 0.0.0.0/0 |

---

# Understanding Security Groups

Security Groups are:
- Stateful
- Applied at instance level
- Allow-only firewalls

Unlike NACLs:
- Return traffic is automatically allowed

---

# EC2 Instance Configuration

| Setting | Value |
|---|---|
| AMI | Amazon Linux 2023 |
| Instance Type | t3.micro |
| VPC | Test VPC |
| Subnet | Public subnet |
| Public IP | Enabled |
| Security Group | public security group |

---

# SSH Connection

Connected to the EC2 instance using:
```bash
ssh -i labsuser.pem ec2-user@<public-ip>
```

---

# Testing Internet Connectivity

Ran the command:

```bash
ping google.com
```

Successful replies confirmed:
- Internet Gateway worked correctly
- Route table was configured properly
- Security Group allowed traffic
- NACL rules allowed traffic
- Public subnet had internet connectivity

---

# Networking Flow in This Lab

Internet Traffic Flow:

```text
EC2 Instance
   ↓
Security Group
   ↓
Subnet
   ↓
Route Table
   ↓
Internet Gateway
   ↓
Internet
```

---

# Difference Between Security Groups and NACLs

| Feature | Security Group | NACL |
|---|---|---|
| Level | Instance | Subnet |
| Stateful | Yes | No |
| Allow Rules | Yes | Yes |
| Deny Rules | No | Yes |
| Default Behavior | Deny all inbound | Allow all |

---

# Skills Practiced

- Creating VPC networking resources
- Configuring route tables
- Configuring Internet Gateway
- Associating subnets
- Creating Security Groups
- Creating Network ACLs
- Launching EC2 instances
- SSH access
- Troubleshooting connectivity
- Testing internet access

---

# What I Learned

- A VPC requires multiple networking resources for internet connectivity
- Internet Gateway enables internet access
- Route tables determine traffic direction
- Public subnets require IGW routing
- Security Groups and NACLs protect resources
- Public IP addresses are required for external communication
- Successful ping responses validate connectivity

---

# Troubleshooting Knowledge Gained

To troubleshoot internet connectivity:
1. Verify public IP assignment
2. Verify Internet Gateway attachment
3. Verify route table configuration
4. Verify subnet association
5. Verify Security Group rules
6. Verify NACL rules

---

# Screenshots




