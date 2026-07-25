# 📊 Monitoring Infrastructure

## 📖 Lab Overview

In this lab, I set up comprehensive monitoring for an EC2 web server 
using **Amazon CloudWatch** and **AWS Config**. This included 
installing the CloudWatch agent, monitoring application logs, 
tracking system metrics, creating real-time notifications, and 
checking infrastructure compliance.

---

## 🎯 Objectives

- [x] Install the CloudWatch agent on an EC2 instance using 
AWS Systems Manager Run Command
- [x] Monitor application logs using CloudWatch Logs
- [x] Monitor system metrics using CloudWatch Metrics
- [x] Create real-time notifications using CloudWatch Events
- [x] Track infrastructure compliance using AWS Config

---

## 🛠️ AWS Services Used

| Service | Purpose |
|---|---|
| Amazon CloudWatch | Logs, metrics, alarms, and events |
| AWS Systems Manager | Installing and configuring CloudWatch agent |
| AWS Systems Manager Parameter Store | Storing CloudWatch agent config |
| Amazon SNS | Email notifications for alarms and events |
| AWS Config | Infrastructure compliance checking |
| Amazon EC2 | Web Server being monitored |

---

## 📋 Step-by-Step Summary

### Task 1: Install CloudWatch Agent
- Used **Systems Manager Run Command** with 
`AWS-ConfigureAWSPackage` to install `AmazonCloudWatchAgent`
- Created a **Parameter Store** parameter (`Monitor-Web-Server`) 
with JSON config to collect:
  - Web server access and error logs (`HttpAccessLog`, `HttpErrorLog`)
  - CPU, disk, memory, and swap metrics every 10 seconds
- Used **AmazonCloudWatch-ManageAgent** Run Command to start 
the agent with the Parameter Store config

### Task 2: Monitor Application Logs
- Generated 404 log data by accessing non-existent web pages
- Viewed logs in **CloudWatch Log Groups** under `HttpAccessLog`
- Created a **metric filter** to detect 404 errors:
```
  [ip, id, user, timestamp, request, status_code=404, size]
```
- Created a **CloudWatch Alarm** (`404 Errors`) to trigger when 
5+ errors occur in 1 minute
- Triggered the alarm by accessing invalid pages 5+ times
- Received **ALARM email notification** ✅

### Task 3: Monitor Instance Metrics
- Viewed EC2 instance metrics in the **Monitoring tab**
- Explored **CloudWatch Metrics → CWAgent** for:
  - Disk space metrics (device, fstype, host, path)
  - Memory metrics (mem_used_percent)

### Task 4: Create Real-Time Notifications
- Created a **CloudWatch Events rule** 
(`Instance_Stopped_Terminated`) to detect EC2 state changes
- Configured it to trigger for **stopped** and **terminated** states
- Set **SNS topic** as the target for notifications
- Stopped the Web Server instance and received 
**JSON email notification** ✅

### Task 5: Infrastructure Compliance with AWS Config
- Configured AWS Config for initial use
- Added **required-tags** rule to check for `project` tag on resources
- Added **ec2-volume-inuse-check** rule to find unattached EBS volumes
- Reviewed compliance results:
  - Web Server instance — **Compliant** (has project tag) ✅
  - Attached EBS volume — **Compliant** ✅
  - Other resources — **Non-compliant** (missing project tag)

---

## 💡 Key Concepts Learned

- The **CloudWatch agent** collects metrics and logs from inside 
EC2 instances (memory, disk) that standard CloudWatch cannot see
- **Parameter Store** is a great way to store and retrieve 
configuration files securely
- **CloudWatch Logs** can automatically collect log files from 
EC2 instances without logging into each server
- **Metric filters** can parse log files and convert specific 
patterns into CloudWatch metrics
- **CloudWatch Alarms** can trigger SNS notifications when 
metrics exceed thresholds
- **CloudWatch Events** provide near-real-time notifications 
when AWS resources change state
- **AWS Config** continuously monitors resource configurations 
and checks compliance against defined rules
- AWS Config has a large library of pre-built compliance rules 
covering tagging, security, and resource usage

---

## ✅ Lab Outcome

Successfully installed and configured the CloudWatch agent, 
monitored web server logs and system metrics, created a 404 error 
alarm, set up real-time EC2 state change notifications, and 
verified infrastructure compliance using AWS Config rules.

---

*Lab completed as part of the **AWS re/Start Program** — 
Cloud Practitioner track.*