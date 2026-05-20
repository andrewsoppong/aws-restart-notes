# Amazon VPC and Cloud Networking

## Objective

Learn about networking in the cloud, Amazon Virtual Private Cloud (Amazon VPC), subnetting, CIDR block addressing, and the core networking components used in AWS cloud environments.

---

# Topics Covered

- Networking in the cloud
- Virtual networking with Amazon VPC
- VPC components
- Subnets
- CIDR block addressing
- Public and private networking in AWS

---

# Networking in the Cloud

Cloud networking is the process of managing communication between cloud resources and services over the internet or private networks.

Unlike traditional networking:
- Infrastructure is virtualized
- Resources are scalable
- Networks can be created and configured on demand

---

# Benefits of Cloud Networking

- Scalability
- High availability
- Flexibility
- Security
- Cost efficiency
- Global connectivity

---

# Amazon Virtual Private Cloud (Amazon VPC)

Amazon VPC is a logically isolated virtual network in AWS where resources can be launched securely.

A VPC allows users to:
- Create private cloud networks
- Control IP addressing
- Configure routing
- Manage internet access
- Secure AWS resources

---

# Features of Amazon VPC

- Isolated virtual network
- Custom IP address ranges
- Public and private subnets
- Route tables
- Internet gateways
- Security groups
- Network ACLs

---

# Key Components of a VPC

## 1. CIDR Block

A CIDR block defines the IP address range for the VPC.

Example:

```text
10.0.0.0/16
```

This provides:
- 65,536 IP addresses

---

# CIDR (Classless Inter-Domain Routing)

CIDR is a method used to allocate IP addresses efficiently.

## CIDR Structure

Example:

```text
10.0.0.0/16
```

Where:
- `10.0.0.0` = network address
- `/16` = subnet mask size

---

# Common CIDR Examples

| CIDR Block | Available IP Addresses |
|---|---|
| /8 | 16,777,216 |
| /16 | 65,536 |
| /24 | 256 |
| /32 | 1 |

---

# Subnets

A subnet is a smaller network inside a VPC.

Subnets help:
- Organize resources
- Improve security
- Separate workloads

---

# Types of Subnets

## Public Subnet

A public subnet:
- Has access to the internet
- Uses an Internet Gateway
- Hosts public-facing resources

Examples:
- Web servers
- Bastion hosts

---

## Private Subnet

A private subnet:
- Does not allow direct internet access
- Is used for internal resources

Examples:
- Databases
- Internal application servers

---

# Internet Gateway (IGW)

An Internet Gateway allows communication between:
- The VPC
- The public internet

Without an IGW:
- Instances cannot access the internet

---

# Route Tables

Route tables determine where network traffic is directed.

Example:
- Internal traffic stays inside the VPC
- Internet traffic routes through the Internet Gateway

---

# Security Groups

Security groups act as virtual firewalls for EC2 instances.

They control:
- Inbound traffic
- Outbound traffic

---

# Network Access Control Lists (NACLs)

NACLs provide subnet-level security.

They:
- Allow or deny traffic
- Apply rules to entire subnets

---

# Subnetting in Amazon VPC

Subnetting divides a VPC into smaller networks.

Example:

VPC CIDR:
```text
10.0.0.0/16
```

Possible subnets:
```text
10.0.1.0/24
10.0.2.0/24
10.0.3.0/24
```

---

# Why Subnetting Matters

Subnetting improves:
- Network organization
- Security isolation
- Traffic management
- Scalability

---

# Relationship Between CIDR and VPC

CIDR blocks define:
- The total IP range of the VPC
- The available subnet ranges

AWS uses CIDR blocks to:
- Allocate IP addresses
- Manage network segmentation

---

# Public vs Private Networking in AWS

| Feature | Public Subnet | Private Subnet |
|---|---|---|
| Internet Access | Yes | No |
| Uses IGW | Yes | No |
| Typical Resources | Web servers | Databases |
| Accessibility | Public | Internal only |

---

# What I Learned

- Amazon VPC creates isolated cloud networks
- CIDR blocks define VPC IP ranges
- Subnets divide networks into smaller segments
- Public subnets allow internet access
- Private subnets improve security
- Route tables and gateways control traffic flow

---

# Challenges

- Understanding CIDR notation
- Learning subnetting concepts
- Differentiating public and private subnets
- Understanding VPC networking components

---

# Screenshots

(Add screenshots here)

## Suggested Screenshots

