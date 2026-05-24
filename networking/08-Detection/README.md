# Detection Security Fundamentals

## Overview

In this lesson, you learn about detection mechanisms used in cybersecurity to identify threats, malicious activity, and unauthorized access. Detection tools help organizations monitor systems, analyze suspicious behavior, and respond to security incidents quickly.

---

# What You Will Learn

At the core of this lesson, you will learn how to:

- Describe how antivirus software is used to detect threats
- Define the benefits of an Intrusion Detection System (IDS)
- Identify how Amazon GuardDuty detects threats

---

# Antivirus Software

## What Is Antivirus Software?

Antivirus software is a security tool designed to detect, prevent, and remove malicious software (malware) from systems and devices.

---

## Common Threats Detected

Antivirus solutions can detect:

- Viruses
- Worms
- Trojans
- Ransomware
- Spyware
- Rootkits

---

## Detection Methods

### Signature-Based Detection

Compares files against a database of known malware signatures.

### Heuristic Analysis

Detects suspicious behavior or unknown malware patterns.

### Behavioral Detection

Monitors application activity to identify malicious actions.

---

## Benefits of Antivirus Software

- Protects systems from malware infections
- Scans files and applications automatically
- Provides real-time threat monitoring
- Helps prevent data loss and compromise

---

# Intrusion Detection System (IDS)

## What Is an IDS?

An Intrusion Detection System (IDS) monitors network or system activity for malicious actions, policy violations, or unauthorized access attempts.

---

## Types of IDS

### Network Intrusion Detection System (NIDS)

Monitors traffic across a network.

### Host Intrusion Detection System (HIDS)

Monitors activity on individual systems or hosts.

---

## Benefits of IDS

- Detects suspicious activity
- Monitors unauthorized access attempts
- Generates security alerts
- Improves visibility into network threats
- Helps security teams respond quickly

---

# Amazon GuardDuty

## What Is Amazon GuardDuty?

Amazon GuardDuty is a threat detection service that continuously monitors AWS accounts, workloads, and data for malicious or unauthorized activity.

---

## How GuardDuty Detects Threats

GuardDuty analyzes multiple AWS data sources, including:

- AWS CloudTrail logs
- VPC Flow Logs
- DNS logs

---

## Threats Detected by GuardDuty

GuardDuty can detect:

- Unauthorized API calls
- Compromised EC2 instances
- Malware activity
- Cryptocurrency mining
- Suspicious network traffic
- Reconnaissance attempts

---

## Benefits of GuardDuty

- Fully managed threat detection service
- Continuous monitoring
- Machine learning–based detection
- Integrates with AWS security services
- Provides actionable security findings

---

# Key Concepts

| Concept | Description |
|---|---|
| Antivirus | Detects and removes malware |
| IDS | Monitors systems and networks for suspicious activity |
| GuardDuty | AWS-managed threat detection service |
| Signature-Based Detection | Uses known malware signatures |
| Behavioral Detection | Detects suspicious actions and anomalies |

---

# Conclusion

In this lesson, you learned how detection technologies improve cybersecurity by identifying threats and malicious activity. You explored antivirus software, intrusion detection systems (IDS), and Amazon GuardDuty as important tools for monitoring and protecting systems and AWS environments.