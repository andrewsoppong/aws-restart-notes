# Troubleshooting a Network Issue

## Overview
This lab focused on troubleshooting networking connectivity issues inside an Amazon Virtual Private Cloud (Amazon VPC). The objective was to identify why an Apache web server running on an Amazon EC2 instance could not be reached through a web browser or by ping requests.

The lab involved reviewing VPC networking resources such as subnets, route tables, internet gateways, security groups, and network ACLs to identify and resolve the connectivity issue.

---

# Objectives

After completing this lab, I was able to:

- Analyze the customer networking issue
- Troubleshoot connectivity problems in AWS
- Verify Apache HTTP server functionality
- Investigate VPC networking configurations
- Validate internet connectivity
- Troubleshoot security group and network ACL configurations
- Successfully access a web server hosted on an EC2 instance

---

# Customer Scenario

A customer named Ana reported the following issue:

> "When I create an Apache server through the command line, I cannot ping it. I also get an error when I enter the IP address in the browser."

The customer environment included:

- Amazon VPC
- Internet Gateway (IGW)
- Public Subnet
- Amazon EC2 Instance running Apache HTTP Server

The customer suspected a networking issue preventing access to the Apache web server.

---

# AWS Resources Used

| Resource | Purpose |
|---|---|
| Amazon VPC | Provides isolated cloud networking |
| Public Subnet | Hosts internet-accessible resources |
| Internet Gateway | Enables internet connectivity |
| Route Table | Routes traffic to the internet |
| Security Group | Controls instance-level traffic |
| Network ACL | Controls subnet-level traffic |
| Amazon EC2 | Hosts the Apache web server |

---

# Architecture Overview

```text
Internet
   │
Internet Gateway
   │
Route Table
   │
Public Subnet
   │
EC2 Instance (Apache Server)
```

---

# Task 1 — Connect to the EC2 Instance

## SSH Connection

### Step 1 — Navigate to Downloads Directory

```bash
cd ~/Downloads
```

### Step 2 — Change PEM Key Permissions

```bash
chmod 400 labsuser.pem
```

### Step 3 — Connect to EC2 Instance

```bash
ssh -i labsuser.pem ec2-user@<public-ip>
```

### Result

Successfully connected to the Amazon Linux EC2 instance using SSH.

---

# Task 2 — Install and Start Apache HTTP Server

## Check Apache Service Status

```bash
sudo systemctl status httpd.service
```

### Observation

The Apache service status initially showed:

```text
inactive (dead)
```

This indicated that Apache was installed but not running.

---

## Start Apache Service

```bash
sudo systemctl start httpd.service
```

---

## Verify Apache Service Status Again

```bash
sudo systemctl status httpd.service
```

### Result

The Apache service changed to:

```text
active (running)
```

This confirmed that the Apache HTTP server was running successfully.

---

# Test Apache Web Server

## Open Browser and Enter Public IP

```text
http://<PUBLIC-IP>
```

### Initial Observation

The webpage failed to load even though Apache was running.

This confirmed that the issue was related to networking or firewall configuration rather than the Apache service itself.

---

# Task 3 — Investigate VPC Networking Configuration

To troubleshoot the issue, each networking component within the VPC was inspected.

---

# Step 1 — Verify Subnet Configuration

## Checks Performed

- Confirmed the subnet was a public subnet
- Verified the subnet was associated with the correct route table

### Result

The subnet configuration was correct.

---

# Step 2 — Verify Route Table Configuration

## Checks Performed

Verified the route table contained the following route:

```text
Destination: 0.0.0.0/0
Target: Internet Gateway
```

### Purpose

This route allows internet-bound traffic to leave the VPC through the Internet Gateway.

### Result

The route table was configured correctly.

---

# Step 3 — Verify Internet Gateway

## Checks Performed

- Confirmed Internet Gateway existed
- Confirmed Internet Gateway was attached to the VPC

### Result

Internet connectivity was properly configured.

---

# Step 4 — Verify Security Group Configuration

## Important Discovery

The EC2 instance security group did not allow:

- HTTP traffic (Port 80)
- ICMP traffic (Ping)

Without these inbound rules:

- Browsers cannot access the Apache server
- Ping requests fail

---

# Required Security Group Rules

## Inbound Rules

| Type | Protocol | Port | Source |
|---|---|---|---|
| HTTP | TCP | 80 | 0.0.0.0/0 |
| HTTPS | TCP | 443 | 0.0.0.0/0 |
| SSH | TCP | 22 | 0.0.0.0/0 |
| All ICMP IPv4 | ICMP | All | 0.0.0.0/0 |

### Explanation

- HTTP allows web browser access
- HTTPS allows secure web traffic
- SSH allows remote administration
- ICMP allows ping connectivity testing

---

# Step 5 — Verify Network ACL Configuration

## Checks Performed

- Verified inbound rules allowed traffic
- Verified outbound rules allowed traffic

### Result

The Network ACL was not blocking traffic.

---

# Connectivity Testing

## Test Internet Connectivity from EC2

```bash
ping www.amazon.com
```

### Result

Successful replies were received.

### What This Confirmed

- Internet Gateway worked correctly
- Route table configuration was correct
- The EC2 instance had internet connectivity

---

# Root Cause Analysis

The root cause of the issue was a misconfigured security group.

The security group was missing:

- HTTP inbound rule
- ICMP inbound rule

Because of this:

- The Apache web server could not be reached through the browser
- Ping requests were blocked

Even though Apache was running successfully, traffic could not reach the EC2 instance.

---

# Resolution

The issue was resolved by updating the EC2 security group inbound rules to allow:

- HTTP traffic on Port 80
- ICMP traffic

After updating the rules:

- The Apache webpage loaded successfully
- Ping requests succeeded

---

# Final Verification

## Ping Test

```bash
ping <public-ip>
```

### Result

Successful replies received.

---

## Browser Test

```text
http://<PUBLIC-IP>
```

### Result

The Apache Test Page loaded successfully in the browser.

---

# Troubleshooting Process Used

## Step-by-Step Method

1. Verify Apache service status
2. Start Apache service
3. Test local server functionality
4. Verify internet connectivity
5. Check subnet associations
6. Check route tables
7. Verify Internet Gateway attachment
8. Investigate security groups
9. Investigate Network ACLs
10. Retest connectivity

---

# Key Networking Concepts Learned

## Security Groups

- Stateful firewall
- Controls traffic at the instance level
- Denies inbound traffic by default

## Network ACLs (NACLs)

- Stateless firewall
- Controls subnet-level traffic

## Internet Gateway

- Provides internet connectivity for public resources

## Route Tables

- Control traffic routing within the VPC

## Public Subnets

- Allow resources to communicate with the internet

---

# Commands Used

## SSH Connection

```bash
ssh -i labsuser.pem ec2-user@<public-ip>
```

## Check Apache Status

```bash
sudo systemctl status httpd.service
```

## Start Apache Service

```bash
sudo systemctl start httpd.service
```

## Test Internet Connectivity

```bash
ping www.amazon.com
```

---

# Skills Gained

- AWS VPC troubleshooting
- Apache web server troubleshooting
- Security group configuration
- Network ACL troubleshooting
- Internet connectivity testing
- Linux server administration
- AWS networking fundamentals

---

# Conclusion

In this lab, I investigated and resolved a networking issue preventing access to an Apache web server hosted on an Amazon EC2 instance. I verified the Apache service, tested internet connectivity, and analyzed VPC networking resources. The issue was caused by missing inbound security group rules for HTTP and ICMP traffic. After correcting the security group configuration, the Apache server became fully accessible through both ping and a web browser.

---