# IP Addressing and Internet Protocol

## Objective
Learn about Internet Protocol (IP), IP addressing, IP classes, binary conversion, and port numbering.

---

# Topics Covered

- Internet Protocol (IP)
- IP address purpose and notation
- IPv4 address classes
- Binary conversion
- Port numbering

---

# What is Internet Protocol (IP)?

Internet Protocol (IP) is a set of rules used for addressing and routing data across networks and the Internet.

## Features of IP
- Provides logical addressing
- Enables communication between devices
- Routes packets across networks
- Supports network identification

---

# IP Address

An IP address is a unique identifier assigned to a device on a network.

## IPv4 Format

IPv4 addresses use four octets separated by dots.

Example:

```text
192.168.1.1
```

Each octet ranges from:
```text
0 - 255
```

---

# Purpose of an IP Address

- Identifies devices on a network
- Helps route data to the correct destination
- Enables communication between systems

---

# IP Address Classes

| Class | Range | Default Subnet Mask | Purpose |
|---|---|---|---|
| A | 1 - 126 | 255.0.0.0 | Large networks |
| B | 128 - 191 | 255.255.0.0 | Medium networks |
| C | 192 - 223 | 255.255.255.0 | Small networks |
| D | 224 - 239 | N/A | Multicasting |
| E | 240 - 255 | N/A | Experimental |

---

# IPv6

IPv6 is the newer version of the Internet Protocol designed to replace IPv4 and provide a much larger address space.

## Features of IPv6

- 128-bit address length
- Supports a massive number of devices
- Improved security and efficiency
- Simplified packet handling
- Better support for modern Internet growth

## Example IPv6 Address

```text
2001:0db8:85a3:0000:0000:8a2e:0370:7334
```

## IPv4 vs IPv6

| Feature | IPv4 | IPv6 |
|---|---|---|
| Address Size | 32-bit | 128-bit |
| Format | Decimal | Hexadecimal |
| Example | 192.168.1.1 | 2001:db8::1 |
| Address Capacity | Limited | Extremely large |

---

# Static and Dynamic IP Addresses

## Static IP Address

A static IP address does not change and is manually assigned.

### Advantages
- Reliable for servers
- Easier remote access
- Good for hosting services

### Disadvantages
- Requires manual configuration
- Less flexible

---

## Dynamic IP Address

A dynamic IP address changes automatically using DHCP.

### Advantages
- Easier management
- Automatic assignment
- More scalable

### Disadvantages
- IP may change over time

---

# IP Addresses in Amazon EC2

Amazon EC2 instances can have both private and public IP addresses.

## Private IP Address

- Used for internal AWS communication
- Assigned within the VPC
- Cannot directly access the Internet

---

## Public IP Address

- Allows Internet communication
- Reachable from outside AWS
- Can change after instance restart unless Elastic IP is used

---

# Elastic IP Address

An Elastic IP is a static public IPv4 address provided by AWS.

## Benefits

- Persistent public IP
- Useful for production servers
- Allows remapping between EC2 instances

---

# Binary Conversion

Computers use binary (0s and 1s) to process information.

## Example Conversion

Decimal:
```text
192
```

Binary:
```text
11000000
```

---

# Common Binary Values

| Decimal | Binary |
|---|---|
| 128 | 10000000 |
| 64 | 01000000 |
| 32 | 00100000 |
| 16 | 00010000 |
| 8 | 00001000 |
| 4 | 00000100 |
| 2 | 00000010 |
| 1 | 00000001 |

---

# Port Numbers

Ports are logical communication endpoints used by network services.

## Common Port Numbers

| Port | Protocol/Service |
|---|---|
| 20/21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |

---

# Why Port Numbers Matter

- Allow multiple services on one device
- Help identify network services
- Improve communication organization

---

# What I Learned

- IP addresses uniquely identify devices
- IPv4 uses dotted decimal notation
- Different IP classes support different network sizes
- Binary is the language computers use internally
- Ports allow devices to run multiple network services
- IPv6 solves IPv4 address exhaustion
- IP operates at Layer 3 of the OSI model
- Routers use IP addresses for routing
- Static IPs remain fixed while dynamic IPs change
- EC2 instances use both private and public IP addresses

---

# Challenges

- Understanding binary conversion
- Memorizing IP classes and port numbers

---

# Screenshots


