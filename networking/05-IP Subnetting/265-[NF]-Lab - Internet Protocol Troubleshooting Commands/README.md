# IP Subnetting

## Overview

This lesson covered the fundamentals of IP subnetting, subnet masks, and CIDR notation. Subnetting is used to divide a large network into smaller and more manageable subnetworks. It improves network organization, performance, security, and efficient IP address allocation.

Subnetting is commonly used in cloud environments such as Amazon Virtual Private Cloud (Amazon VPC).

---

# What You Will Learn

At the core of this lesson, I learned how to:

- Define a subnet, its parts, and its purpose
- Describe the purpose of IP subnetting
- Use CIDR notation to specify subnet address ranges
- Describe the use of subnet masks

---

# What Is a Subnet?

A subnet (subnetwork) is a smaller section of a larger network.

Subnetting helps:

- Organize networks
- Reduce network congestion
- Improve performance
- Improve security
- Allocate IP addresses efficiently

---

# Parts of an IP Address

An IPv4 address has two main parts:

| Part | Purpose |
|---|---|
| Network Portion | Identifies the network |
| Host Portion | Identifies the device |

Example:

```text
192.168.1.10/24
```

- Network portion: `192.168.1`
- Host portion: `10`

---

# Purpose of IP Subnetting

Subnetting is used to:

- Divide large networks into smaller networks
- Improve network performance
- Reduce broadcast traffic
- Separate departments or environments
- Improve security
- Manage IP addresses efficiently

---

# CIDR Notation

CIDR stands for:

**Classless Inter-Domain Routing**

CIDR notation identifies how many bits belong to the network portion of an IP address.

Example:

```text
192.168.1.0/24
```

- `/24` means the first 24 bits are used for the network
- Remaining bits are used for hosts

---

# Common CIDR Ranges

| CIDR | Total IP Addresses | Usable Hosts |
|---|---|---|
| /30 | 4 | 2 |
| /29 | 8 | 6 |
| /28 | 16 | 14 |
| /27 | 32 | 30 |
| /26 | 64 | 62 |
| /25 | 128 | 126 |
| /24 | 256 | 254 |
| /16 | 65,536 | 65,534 |

---

# Subnet Masks

A subnet mask identifies the network and host portions of an IP address.

Example:

```text
255.255.255.0
```

Equivalent CIDR notation:

```text
/24
```

---

# CIDR and Subnet Mask Equivalents

| CIDR | Subnet Mask |
|---|---|
| /8 | 255.0.0.0 |
| /16 | 255.255.0.0 |
| /24 | 255.255.255.0 |
| /26 | 255.255.255.192 |
| /28 | 255.255.255.240 |

---

# Private IP Address Ranges (RFC 1918)

Private IP addresses are used inside internal networks and Amazon VPCs.

| Private Range | CIDR |
|---|---|
| 10.0.0.0 – 10.255.255.255 | /8 |
| 172.16.0.0 – 172.31.255.255 | /12 |
| 192.168.0.0 – 192.168.255.255 | /16 |

These addresses are not accessible from the public internet.

---

# Public vs Private IP Addresses

| Public IP | Private IP |
|---|---|
| Accessible on the internet | Used inside private networks |
| Globally unique | Reusable in different networks |
| Assigned publicly | Used internally in VPCs |

---

# Example of Subnetting

Original network:

```text
192.168.1.0/24
```

Possible subnets:

| Subnet | CIDR | Usable Hosts |
|---|---|---|
| 192.168.1.0/26 | /26 | 62 |
| 192.168.1.64/26 | /26 | 62 |
| 192.168.1.128/26 | /26 | 62 |
| 192.168.1.192/26 | /26 | 62 |

---

# Binary Representation of IPv4

IPv4 addresses are 32-bit binary numbers.

Example:

```text
192.168.1.1
```

Binary:

```text
11000000.10101000.00000001.00000001
```

---

# Network and Broadcast Addresses

Each subnet contains:

| Address Type | Purpose |
|---|---|
| Network Address | Identifies the subnet |
| Broadcast Address | Sends data to all devices in subnet |

Example:

Subnet:

```text
192.168.1.0/24
```

- Network address: `192.168.1.0`
- Broadcast address: `192.168.1.255`

---

# Usable Host Addresses

The first and last IP addresses in a subnet are reserved.

Formula:

```text
Usable Hosts = Total IPs - 2
```

---

# Subnetting in AWS

Subnetting is heavily used in Amazon VPC.

## Public Subnet

- Has internet access
- Uses an Internet Gateway
- Often hosts web servers

## Private Subnet

- No direct internet access
- Used for databases and internal resources

---

# Amazon VPC and CIDR

When creating a VPC, a CIDR block is assigned.

Example:

```text
192.168.0.0/18
```

This provides:

- 16,384 total IP addresses

Subnets can then be created inside the VPC.

Example:

```text
192.168.1.0/26
```

---

# Benefits of Subnetting

- Better network organization
- Improved security
- Reduced broadcast traffic
- Efficient IP allocation
- Easier troubleshooting
- Scalable cloud networking

---

# Key Takeaways

- Subnetting divides large networks into smaller subnetworks
- CIDR notation defines subnet size
- Subnet masks identify network and host portions
- Private IP ranges are used inside Amazon VPCs
- Public and private subnets serve different purposes
- Subnetting is essential in AWS cloud networking

---

# Conclusion

In this lesson, I learned the fundamentals of IP subnetting, CIDR notation, subnet masks, and private IP addressing. I also explored how subnetting is used in AWS cloud networking environments such as Amazon VPC to organize resources, improve security, and efficiently allocate IP addresses.