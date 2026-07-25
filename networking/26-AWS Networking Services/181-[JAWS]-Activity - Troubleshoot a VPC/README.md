# 🔧 Troubleshooting a VPC

## 📖 Lab Overview

In this lab, I troubleshot virtual private cloud (VPC) configuration 
issues and analyzed VPC Flow Logs. The lab environment had a broken 
network configuration that prevented access to a café web server. 
I identified and fixed the issues using the AWS CLI, then analyzed 
the flow log data to observe captured traffic.

---

## 🏗️ Lab Architecture

- **VPC1** — Contains the café web server in a public subnet
- **VPC2** — Contains the CLI Host instance used for AWS CLI commands
- **S3 Bucket** — Stores VPC Flow Log data
- **Web Server** — EC2 instance running in VPC1's public subnet

---

## 🎯 Objectives

- [x] Create VPC Flow Logs and publish them to an S3 bucket
- [x] Troubleshoot and fix a missing internet gateway route
- [x] Troubleshoot and fix a blocking network ACL rule
- [x] Download and analyze VPC Flow Log data

---

## 🛠️ AWS Services Used

| Service | Purpose |
|---|---|
| Amazon VPC | Virtual network with subnets, route tables, ACLs |
| Amazon EC2 | Web server and CLI Host instances |
| Amazon S3 | Storage for VPC Flow Log data |
| VPC Flow Logs | Captures IP traffic through network interfaces |
| Security Groups | Instance-level firewall rules |
| Network ACLs | Subnet-level firewall rules |
| AWS CLI | All troubleshooting done programmatically |

---

## 📋 Step-by-Step Summary

### Task 1: Connect to CLI Host
- Connected to **CLI Host** instance via EC2 Instance Connect
- Configured AWS CLI with AccessKey, SecretKey, and region `us-west-2`

### Task 2: Create VPC Flow Logs
- Created an S3 bucket (`flowlog######`) to store flow log data
- Retrieved VPC1 ID using `aws ec2 describe-vpcs`
- Created flow logs on VPC1 with traffic type ALL
- Confirmed flow log status showed **ACTIVE**

### Task 3: Troubleshoot VPC Issues

#### Challenge #1 — Fix Web Access
- Confirmed web server was running but webpage was unreachable
- Checked security group — port 80 and 22 rules were present ✅
- Checked route table for VPC1's public subnet
- Found **missing route** — no `0.0.0.0/0 → Internet Gateway` entry
- Retrieved Internet Gateway ID using `describe-internet-gateways`
- Created the missing route using `aws ec2 create-route`
- Refreshed browser — **"Hello From Your Web Server!"** appeared ✅

#### Challenge #2 — Fix SSH Access
- Attempted EC2 Instance Connect — still failing
- Checked Network ACL for the public subnet
- Found a **DENY rule on port 22** blocking SSH traffic
- Deleted the blocking rule using `aws ec2 delete-network-acl-entry`
- Successfully connected via EC2 Instance Connect ✅
- Confirmed hostname showed **web-server** ✅

### Task 4: Analyze Flow Logs
- Created local `flowlogs` directory and downloaded logs from S3
- Extracted compressed `.gz` log files using `gunzip`
- Analyzed log structure using `head` command
- Used `grep` to filter for **REJECT** entries
- Filtered further for port **22** REJECT entries
- Found my local IP address via EC2 Security Groups console
- Filtered logs to isolate failed SSH attempts from my IP
- Verified network interface ID matched the web server
- Converted Unix timestamps to human-readable format using `date -d @`

---

## 💡 Key Concepts Learned

- **VPC Flow Logs** capture all IP traffic through network interfaces 
and are useful for security analysis and troubleshooting
- A **missing route** in a route table can prevent all internet access 
even if the security group is correctly configured
- **Network ACLs** are stateless subnet-level firewalls — a DENY rule 
can block traffic even if the security group allows it
- **Security Groups** are stateful instance-level firewalls
- The order of troubleshooting: check instance state → security groups 
→ route tables → network ACLs
- `grep`, `gunzip`, and `wc -l` are powerful Linux tools for 
analyzing log files
- Unix timestamps can be converted using the `date -d @` command
- **Amazon Athena** can be used for advanced SQL-based querying 
of VPC Flow Logs

---

## 🔍 Useful CLI Commands Used

```bash
# Create S3 bucket for flow logs
aws s3api create-bucket --bucket flowlog###### --region 'us-west-2' \
--create-bucket-configuration LocationConstraint='us-west-2'

# Create VPC Flow Logs
aws ec2 create-flow-logs --resource-type VPC --resource-ids <vpc-id> \
--traffic-type ALL --log-destination-type s3 \
--log-destination arn:aws:s3:::<flowlog######>

# Check route tables
aws ec2 describe-route-tables \
--filter "Name=association.subnet-id,Values='<SubnetID>'"

# Create missing route
aws ec2 create-route --route-table-id <rtb-id> \
--destination-cidr-block 0.0.0.0/0 --gateway-id <igw-id>

# Check Network ACLs
aws ec2 describe-network-acls \
--filter "Name=association.subnet-id,Values='<SubnetID>'" \
--query 'NetworkAcls[*].[NetworkAclId,Entries]'

# Delete blocking ACL rule
aws ec2 delete-network-acl-entry \
--network-acl-id <acl-id> --rule-number <number> --ingress

# Analyze flow logs
grep -rn REJECT .
grep -rn 22 . | grep REJECT | grep <ip-address>
```

---

## ✅ Lab Outcome

Successfully created VPC Flow Logs, identified and fixed two VPC 
configuration issues (missing internet gateway route and blocking 
network ACL rule), and analyzed flow log data to confirm that failed 
SSH attempts were captured and recorded.

---

*Lab completed as part of the **AWS re/Start Program** — 
Cloud Practitioner track.*