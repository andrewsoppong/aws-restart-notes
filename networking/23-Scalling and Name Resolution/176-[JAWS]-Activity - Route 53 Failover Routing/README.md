# Amazon Route 53 Failover Routing

## Overview

This lab demonstrates how to configure Amazon Route 53 failover routing for a highly available web application. Two Amazon EC2 instances hosting the same café application are deployed across separate Availability Zones. Amazon Route 53 health checks monitor the primary instance and automatically redirect traffic to the secondary instance if the primary becomes unavailable. :contentReference[oaicite:0]{index=0}

---

## Objectives

After completing this lab, you will be able to:

- Configure a Route 53 health check that sends email notifications when an HTTP endpoint becomes unhealthy
- Configure failover routing in Amazon Route 53

:contentReference[oaicite:1]{index=1}

---

## Architecture

### Initial Environment

The environment includes:

- Two Amazon EC2 instances
- Full LAMP stack installed on each instance
- Café web application deployed on both servers
- Instances running in different Availability Zones
- Route 53 hosted zone already configured

### Final Architecture

The completed architecture provides:

- Primary website hosted on Café Instance 1
- Secondary website hosted on Café Instance 2
- Route 53 health checks monitoring the primary server
- Automatic DNS failover to the secondary server
- Amazon SNS email notifications when failures occur

:contentReference[oaicite:2]{index=2}

---

## Duration

**Approximately 45 minutes**

:contentReference[oaicite:3]{index=3}

---

# Task 1: Confirm the Café Websites

## Purpose

Verify that both EC2 instances are serving the café application successfully before configuring failover.

### Resources Provided

Record the following values from the AWS Details panel:

- CafeInstance1IPAddress
- PrimaryWebSiteURL
- SecondaryWebsiteURL
- CafeInstance2IPAddress

:contentReference[oaicite:4]{index=4}

### Verification Steps

1. Open the EC2 Console.
2. Locate:
   - CafeInstance1
   - CafeInstance2
3. Open both website URLs.
4. Verify:
   - The café website loads correctly.
   - Server Information displays different Availability Zones.
5. Place a sample order to confirm application functionality.

### Expected Outcome

Both EC2 instances successfully host the café application and operate independently in separate Availability Zones.

:contentReference[oaicite:5]{index=5}

---

# Task 2: Configure a Route 53 Health Check

## Purpose

Monitor the health of the primary website and trigger alerts when failures occur.

### Create Health Check

Navigate to:

```text
Route 53 → Health Checks → Create Health Check
```

### Configuration

| Setting | Value |
|----------|---------|
| Name | Primary-Website-Health |
| Monitor | Endpoint |
| Endpoint Type | IP Address |
| IP Address | CafeInstance1 Public IP |
| Path | cafe |
| Request Interval | Fast (10 seconds) |
| Failure Threshold | 2 |

:contentReference[oaicite:6]{index=6}

### Configure Notifications

| Setting | Value |
|----------|---------|
| Create Alarm | Yes |
| Notification Type | New SNS Topic |
| Topic Name | Primary-Website-Health |
| Email | Your Email Address |

:contentReference[oaicite:7]{index=7}

### Verify

- Wait for the health check status to become **Healthy**
- Confirm the SNS subscription email
- Review health check monitoring metrics

:contentReference[oaicite:8]{index=8}

---

# Task 3: Configure Route 53 Failover Records

## Purpose

Create DNS records that support automatic failover.

---

## Create Primary Record

Navigate to:

```text
Route 53 → Hosted Zones
```

### Configuration

| Setting | Value |
|----------|---------|
| Record Name | www |
| Record Type | A |
| Value | CafeInstance1 IP Address |
| TTL | 15 |
| Routing Policy | Failover |
| Failover Type | Primary |
| Health Check | Primary-Website-Health |
| Record ID | FailoverPrimary |

:contentReference[oaicite:9]{index=9}

---

## Create Secondary Record

### Configuration

| Setting | Value |
|----------|---------|
| Record Name | www |
| Record Type | A |
| Value | CafeInstance2 IP Address |
| TTL | 15 |
| Routing Policy | Failover |
| Failover Type | Secondary |
| Health Check | Leave Blank |
| Record ID | FailoverSecondary |

:contentReference[oaicite:10]{index=10}

### Result

The hosted zone now contains:

- Primary failover record
- Secondary failover record

These records enable automatic DNS failover.

:contentReference[oaicite:11]{index=11}

---

# Task 4: Verify DNS Resolution

## Purpose

Confirm that Route 53 directs traffic to the primary server.

### Steps

1. Copy the Route 53 record name.
2. Open a browser.
3. Access:

```text
http://www.<your-domain>.vocareum.training/cafe/
```

### Expected Result

The website loads from:

```text
CafeInstance1
```

The Server Information section should display the primary Availability Zone.

:contentReference[oaicite:12]{index=12}

---

# Task 5: Verify Failover Functionality

## Purpose

Simulate a server failure and verify Route 53 failover behavior.

### Stop the Primary Server

Navigate to:

```text
EC2 → Instances
```

Select:

```text
CafeInstance1
```

Then:

```text
Instance State → Stop Instance
```

:contentReference[oaicite:13]{index=13}

---

## Monitor Health Check

Navigate to:

```text
Route 53 → Health Checks
```

Select:

```text
Primary-Website-Health
```

Monitor until the status becomes:

```text
Unhealthy
```

:contentReference[oaicite:14]{index=14}

---

## Verify Failover

Refresh the café website.

### Expected Results

- Website remains accessible.
- Server Information now displays:
  - Secondary Availability Zone
  - Café Instance 2

This confirms successful failover routing.

:contentReference[oaicite:15]{index=15}

---

## Verify Email Notification

Check your inbox for an SNS alert.

Example Subject:

```text
ALARM: Primary-Website-Health-awsroute53
```

This confirms health check alarms are functioning correctly.

:contentReference[oaicite:16]{index=16}

---

# Key Concepts Learned

## Route 53 Health Checks

Health checks continuously monitor endpoints and determine whether they are healthy or unhealthy.

### Benefits

- Detect endpoint failures
- Trigger CloudWatch alarms
- Send SNS notifications
- Support automated failover

---

## DNS Failover Routing

Failover routing allows Route 53 to:

1. Route traffic to the primary resource.
2. Monitor resource health.
3. Automatically redirect traffic if the primary fails.
4. Restore traffic when the primary becomes healthy again.

---

## High Availability

Deploying resources across multiple Availability Zones provides:

- Fault tolerance
- Improved uptime
- Automatic disaster recovery
- Better customer experience

---

# AWS Services Used

- Amazon Route 53
- Amazon EC2
- Amazon SNS
- AWS CloudFormation
- LAMP Stack

---

# Conclusion

In this lab, you configured Amazon Route 53 failover routing to improve application availability. You created a health check for the primary website, configured Amazon SNS email alerts, created primary and secondary DNS failover records, and verified automatic traffic redirection when the primary EC2 instance became unavailable. This solution demonstrates a common high-availability architecture used in production AWS environments.

---

## Lab Outcomes

Successfully completed:

- Route 53 health check configuration
- Amazon SNS notification setup
- Primary and secondary failover record creation
- DNS failover routing implementation
- Health monitoring and alerting
- High-availability website architecture validation

:contentReference[oaicite:17]{index=17}