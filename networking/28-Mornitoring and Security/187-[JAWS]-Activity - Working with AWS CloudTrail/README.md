# 🕵️ Working with AWS CloudTrail

## 📖 Lab Overview

In this lab, I acted as a security detective to investigate a hack 
on the Café website. I created a **CloudTrail trail** to audit AWS 
account activity, analyzed logs using **grep**, **AWS CLI**, and 
**Amazon Athena**, identified the hacker, and secured both the AWS 
account and the EC2 web server instance.

---

## 🏗️ Lab Architecture

- **Café Web Server** EC2 instance hosting the Café website
- **CloudTrail trail** (`monitor`) logging all API activity to S3
- **S3 bucket** (`monitoring####`) storing CloudTrail logs
- **Amazon Athena** for SQL-based log analysis
- **IAM user** (`chaos`) — the hacker who was discovered and removed

---

## 🎯 Objectives

- [x] Configure a CloudTrail trail
- [x] Analyze CloudTrail logs using grep and AWS CLI
- [x] Import CloudTrail log data into Athena
- [x] Run SQL queries in Athena to identify the hacker
- [x] Resolve security issues in the AWS account and EC2 instance

---

## 🛠️ AWS Services Used

| Service | Purpose |
|---|---|
| AWS CloudTrail | Audit trail of all API activity |
| Amazon S3 | Storage for CloudTrail logs |
| Amazon Athena | SQL queries on CloudTrail log data |
| Amazon EC2 | Café Web Server being investigated |
| AWS IAM | Removing the hacker's AWS user account |
| AWS Systems Manager | Instance metadata |

---

## 📋 Step-by-Step Summary

### Task 1: Modify Security Group and View Website
- Added SSH inbound rule (port 22) restricted to My IP
- Confirmed website looked normal at `http://WebServerIP/cafe/`

### Task 2: Create CloudTrail Trail
- Created trail named **monitor** with logs stored in 
`monitoring####` S3 bucket
- Observed the hacked website — wrong image appeared
- Discovered a new suspicious inbound rule allowing SSH 
from **0.0.0.0/0** (anywhere)

### Task 3: Analyze Logs with grep and AWS CLI
- SSH'd into the Café Web Server instance
- Downloaded and extracted CloudTrail logs from S3
- Used `grep` to filter log entries by `sourceIPAddress` 
and `eventName`
- Used AWS CLI `lookup-events` to filter security group events
- Identified the specific security group ID used by the web server

```bash
# Download logs
aws s3 cp s3://monitoring####/ . --recursive
gunzip *.gz

# Filter by event name
for i in $(ls); do echo $i && cat $i | python -m json.tool \
| grep eventName ; done

# Filter security group events
aws cloudtrail lookup-events \
--lookup-attributes AttributeKey=ResourceType,\
AttributeValue=AWS::EC2::SecurityGroup \
--region $region --output text | grep $sgId
```

### Task 4: Analyze Logs with Athena
- Created Athena table from CloudTrail S3 bucket
- Set query results location to `s3://monitoring####/results/`
- Ran SQL queries to identify the hacker:

```sql
-- Find all distinct user actions
SELECT DISTINCT useridentity.userName, eventName, eventSource
FROM cloudtrail_logs_monitoring####
WHERE from_iso8601_timestamp(eventtime) > date_add('day', -1, now())
ORDER BY eventSource;

-- Find security group changes
SELECT useridentity.userName, eventtime, eventsource, 
eventname, requestparameters
FROM cloudtrail_logs_monitoring####
WHERE eventsource = 'ec2.amazonaws.com'
AND eventname LIKE '%Security%';
```

**Challenge Result:** Identified the hacker as the **chaos** IAM 
user who ran `AuthorizeSecurityGroupIngress` to open port 22 
to 0.0.0.0/0

### Task 5: Secure the System

#### Task 5.1 — Remove Hacker from EC2 Instance
- Used `sudo aureport --auth` to confirm chaos-user had logged in
- Used `who` to confirm chaos-user was still active
- Killed their active session with `sudo kill -9 ProcNum`
- Deleted the chaos-user OS account with `sudo userdel -r chaos-user`

#### Task 5.2 — Fix SSH Security
- Found `PasswordAuthentication yes` enabled in `/etc/ssh/sshd_config`
- Commented out `PasswordAuthentication yes`
- Uncommented `PasswordAuthentication no`
- Restarted SSH service
- Removed the malicious `0.0.0.0/0` inbound rule from security group

#### Task 5.3 — Restore the Website
```bash
cd /var/www/html/cafe/images/
sudo mv Coffee-and-Pastries.backup Coffee-and-Pastries.jpg
```
Website restored to normal ✅

#### Task 5.4 — Delete Hacker's IAM User
- Deleted the **chaos** IAM user from the AWS account via IAM console

---

## 💡 Key Concepts Learned

- **AWS CloudTrail** records every API call made in your AWS account 
including who made it, when, and from where
- CloudTrail logs are stored in **JSON format** in S3 and can be 
analyzed with grep, AWS CLI, or Athena
- **Amazon Athena** makes it easy to run SQL queries on large 
CloudTrail log datasets stored in S3
- **PasswordAuthentication** should always be disabled in SSH 
config — key pair authentication is much more secure
- Security groups should **never** allow SSH (port 22) from 
`0.0.0.0/0` — always restrict to specific IPs
- **CloudTrail** is essential for security auditing, compliance, 
and incident response
- The `AuthorizeSecurityGroupIngress` event in CloudTrail is 
the key indicator of a security group rule being added

---

## ✅ Lab Outcome

Successfully created a CloudTrail trail, identified a hacker using 
Athena SQL queries on CloudTrail logs, removed the hacker from the 
EC2 instance and AWS account, restored the website, and hardened 
the security configuration to prevent future attacks.

---

*Lab completed as part of the **AWS re/Start Program** — 
Cloud Practitioner track.*