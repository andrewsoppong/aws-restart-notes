# 🔧 Troubleshooting the Creation of an EC2 Instance

## 📖 Lab Overview

In this activity, I used the **AWS CLI** to launch an EC2 instance 
running a **LAMP stack** (Linux, Apache, MariaDB, PHP) for the 
Café Web Application. The provided shell script contained 
intentional bugs that I identified and fixed using troubleshooting 
techniques including **nmap** port scanning.

---

## 🏗️ Architecture

- **CLI Host** EC2 instance — used to run AWS CLI commands
- **cafeserver** EC2 instance — LAMP stack web server running 
the Café Web Application
- **Cafe VPC** — existing VPC where the instance was deployed
- **cafeSG** Security Group — allows SSH (22) and HTTP (80)

---

## 🎯 Objectives

- [x] Launch an EC2 instance using the AWS CLI
- [x] Troubleshoot AWS CLI commands and EC2 settings
- [x] Use nmap to diagnose port accessibility issues
- [x] Verify LAMP stack installation via cloud-init logs

---

## 🛠️ AWS Services Used

| Service | Purpose |
|---|---|
| Amazon EC2 | LAMP stack web server instance |
| AWS CLI | Launching and managing instances |
| AWS Systems Manager | Retrieving latest AMI ID |
| Security Groups | Firewall rules for SSH and HTTP |
| EC2 Instance Connect | Browser-based SSH connection |

---

## 📋 Step-by-Step Summary

### Task 1 & 2: Connect and Configure
- Connected to **CLI Host** via EC2 Instance Connect
- Configured AWS CLI with AccessKey, SecretKey, LabRegion

### Task 3: Run and Fix the Script

#### Backup the Script
```bash
cd ~/sysops-activity-files/starters
cp create-lamp-instance-v2.sh create-lamp-instance.backup
```

#### Issue #1 — Wrong AMI ID / Region Mismatch
- **Error:** `InvalidAMIID.NotFound`
- **Cause:** Script was referencing an AMI ID that didn't 
exist in the correct region
- **Fix:** Found the correct region where Cafe VPC exists 
and updated the script to use the right region
- **Result:** Script ran successfully and assigned a 
public IP ✅

#### Issue #2 — Webpage Not Loading
- **Error:** Browser could not connect to the web server
- **Diagnosis:** Used nmap to scan open ports:
```bash
sudo yum install -y nmap
nmap -Pn <public-ip>
```
- **Cause:** Security group was missing HTTP (port 80) 
inbound rule
- **Fix:** Added HTTP rule to cafeSG security group
- **Result:** `http://<public-ip>` showed 
**"Hello From Your Web Server!"** ✅

#### Verified User Data Script
```bash
sudo tail -f /var/log/cloud-init-output.log
```
- Confirmed MariaDB, PHP, and Café website files 
installed successfully with no errors ✅

### Task 4: Verify Café Website
- Accessed `http://<public-ip>/cafe` — home page loaded ✅
- Placed orders via the Menu page ✅
- Verified orders in Order History page ✅

---

## 💡 Key Concepts Learned

- **Shell scripts** can automate EC2 instance creation 
but must use the correct region and AMI ID
- **AMI IDs are region-specific** — an AMI from one region 
cannot be used in another
- **nmap** is a powerful tool for diagnosing port 
accessibility issues
- **Security groups** must have explicit inbound rules 
for each port — HTTP (80) must be added separately from SSH (22)
- **cloud-init logs** at `/var/log/cloud-init-output.log` 
show whether user data scripts ran successfully
- **LAMP stacks** combine Linux, Apache, MySQL/MariaDB, 
and PHP to create full web application environments
- Backing up scripts before editing is a 
**best practice** to avoid data loss

---

## ✅ Lab Outcome

Successfully identified and fixed two issues in the EC2 
launch script — an incorrect AMI ID and a missing HTTP 
security group rule. The Café Web Application was deployed 
and fully functional, with menu ordering and order history 
working correctly.

---

*Lab completed as part of the **AWS re/Start Program** — 
Cloud Practitioner track.*