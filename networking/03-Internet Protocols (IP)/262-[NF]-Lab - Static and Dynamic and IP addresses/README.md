# Lab: Static and Dynamic IP Addresses

## Lab Objective

In this lab, I investigated the differences between static and dynamic IP addresses in AWS using Amazon EC2 instances. I also learned how to assign a persistent public IP address using an Elastic IP (EIP).

---

# Scenario

As a Cloud Support Engineer at AWS, I assisted a customer experiencing issues with an EC2 instance whose public IP address changed every time the instance was stopped and started.

The customer required:
- A permanent public IP address
- Stable connectivity for dependent resources
- A solution to prevent disruptions caused by changing IP addresses

---

# Services Used

- Amazon EC2
- Amazon VPC
- Elastic IP (EIP)
- Security Groups
- Public Subnets

---

# Key Concepts Learned

- Static IP addresses
- Dynamic IP addresses
- Public and private IPv4 addresses
- Elastic IPs (EIP)
- EC2 networking behavior
- IP persistence in AWS

---

# Understanding Dynamic IP Addresses

A dynamic IP address changes automatically over time.

In AWS:
- Public IPv4 addresses assigned automatically to EC2 instances are dynamic
- When an instance is stopped and started, AWS may assign a new public IP address

---

# Understanding Static IP Addresses

A static IP address remains permanently assigned.

In AWS:
- Elastic IP addresses provide static public IP functionality
- The IP remains consistent even after stopping and starting the instance

---

# Task 1: Launch EC2 Instance

I launched an Amazon EC2 instance using:

| Setting | Value |
|---|---|
| AMI | Amazon Linux 2 |
| Instance Type | t3.micro |
| Network | Lab VPC |
| Subnet | Public Subnet 1 |
| Auto-assign Public IP | Enabled |
| Security Group | Linux Instance SG |

---

# Instance Networking Investigation

After launching the instance, I reviewed the Networking tab and recorded:
- Public IPv4 address
- Private IPv4 address

---

# Stopping and Starting the Instance

I stopped the EC2 instance and started it again.

## Observation

| IP Type | Changed? |
|---|---|
| Public IPv4 Address | Yes |
| Private IPv4 Address | No |

---

# Analysis

## Public IP Address

The public IP address changed after restarting the instance because:
- AWS automatically assigns dynamic public IPs by default
- Dynamic IPs are temporary

---

## Private IP Address

The private IP address remained the same because:
- Private IPs stay associated with the instance inside the VPC

---

# Customer Issue Replication

I successfully replicated the customer's issue.

The customer's EC2 instance experienced:
- Dynamic public IP changes
- Connectivity disruptions
- Broken dependent services

This behavior matched the lab environment.

---

# Elastic IP (EIP)

AWS provides a solution called an Elastic IP (EIP).

An Elastic IP is:
- A static public IPv4 address
- Persistent across instance restarts
- Manually allocated and associated with an EC2 instance

---

# Allocating an Elastic IP

I navigated to:
- EC2 Dashboard
- Network & Security
- Elastic IPs

Then:
1. Allocated a new Elastic IP
2. Associated the EIP with the test instance

---

# Results After Associating the Elastic IP

After attaching the Elastic IP:
- The public IP address remained the same
- Restarting the instance no longer changed the IP address

---

# Final Observation

| Feature | Dynamic Public IP | Elastic IP |
|---|---|---|
| Changes on Restart | Yes | No |
| Persistent | No | Yes |
| Internet Accessible | Yes | Yes |
| Recommended for Stable Services | No | Yes |

---

# Root Cause Analysis

The customer's issue occurred because:
- The EC2 instance used a dynamically assigned public IP address
- Dynamic public IPs change after instance restarts

---

# Solution

The issue was resolved by:
- Allocating an Elastic IP
- Associating it with the EC2 instance

This provided:
- Persistent public connectivity
- Stable networking configuration
- Consistent access for dependent services

---

# Skills Practiced

- Launching EC2 instances
- Investigating instance networking
- Working with public and private IP addresses
- Allocating Elastic IPs
- Associating Elastic IPs with EC2 instances
- Troubleshooting AWS networking issues

---

# What I Learned

- Public IPs assigned automatically are dynamic
- Private IP addresses remain attached to the instance
- Elastic IPs provide persistent public connectivity
- Static IPs are important for production services
- AWS networking behavior changes depending on IP type

---

# Challenges

- Understanding the difference between static and dynamic public IPs
- Observing networking behavior after restarting the instance
- Associating the Elastic IP correctly

---

# Screenshots

(Add screenshots here)

## Suggested Screenshots

- EC2 instance configuration
- Networking tab before restart
- Networking tab after restart
- Elastic IP allocation
- Elastic IP association
- Final networking configuration
