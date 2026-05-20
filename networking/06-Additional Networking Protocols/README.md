# Other Types of Communication Protocols

## Overview
In this lesson, I learned about additional communication protocols used in networking. The lab focused on understanding transport protocols, application protocols, network management protocols, and tools used to analyze network communication.

---

# Learning Objectives

By completing this lesson, I learned how to:

- Identify different communication protocols
- Describe common transport protocols
- Describe common application protocols
- Describe common network management protocols
- Use networking tools to discover information about network communications

---

# Understanding Communication Protocols

A communication protocol is a set of rules that devices use to communicate across a network.

Protocols define:
- How data is formatted
- How data is transmitted
- How devices identify each other
- How errors are handled

Protocols operate at different layers of the OSI model.

---

# Transport Protocols

Transport protocols are responsible for end-to-end communication between devices.

## TCP (Transmission Control Protocol)

TCP is:
- Connection-oriented
- Reliable
- Ordered
- Error-checked

### Features
- Guarantees delivery
- Performs retransmissions
- Uses acknowledgements
- Performs flow control

### Common TCP Applications
- HTTP / HTTPS
- SSH
- FTP
- SMTP

### Example Ports
| Protocol | Port |
|---|---|
| HTTP | 80 |
| HTTPS | 443 |
| SSH | 22 |
| FTP | 21 |

---

## UDP (User Datagram Protocol)

UDP is:
- Connectionless
- Faster than TCP
- Does not guarantee delivery

### Features
- Low latency
- Lightweight
- No acknowledgements

### Common UDP Applications
- DNS
- VoIP
- Video streaming
- Gaming

### Example Ports
| Protocol | Port |
|---|---|
| DNS | 53 |
| DHCP | 67/68 |
| SNMP | 161 |

---

# Application Protocols

Application layer protocols allow users and applications to communicate over the network.

---

## HTTP (Hypertext Transfer Protocol)

Used for:
- Web browsing
- Website communication

### Default Port
```bash
80