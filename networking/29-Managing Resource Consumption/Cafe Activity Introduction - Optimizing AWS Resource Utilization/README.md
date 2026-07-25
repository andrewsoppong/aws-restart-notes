# 💰 Optimize Utilization

## 📖 Lab Overview

In this activity, I optimized the Café EC2 instance to reduce 
AWS service costs. This involved uninstalling the decommissioned 
local MariaDB database and downsizing the instance type from 
**t3.small** to **t3.micro**. I then used the **AWS Pricing 
Calculator** to estimate and compare costs before and after 
the optimization.

---

## 🏗️ Architecture

### Before Optimization
- Café instance running on **t3.small**
- Local MariaDB database still installed (occupying 20 GB storage)
- Total EBS storage: **40 GB**

### After Optimization
- Café instance downsized to **t3.micro**
- Local MariaDB database removed
- Total EBS storage reduced to: **20 GB**

---

## 🎯 Objectives

- [x] Optimize an EC2 instance to reduce costs
- [x] Use the AWS Pricing Calculator to estimate AWS service costs
- [x] Calculate projected monthly cost savings

---

## 🛠️ AWS Services Used

| Service | Purpose |
|---|---|
| Amazon EC2 | Café web server instance |
| Amazon RDS | Managed MariaDB database |
| Amazon EBS | Block storage for EC2 instance |
| AWS CLI | Instance management commands |
| AWS Pricing Calculator | Cost estimation tool |

---

## 📋 Step-by-Step Summary

### Task 1: Optimize the Instance

#### Step 1 — Uninstall Local Database (on CafeInstance)
```bash
sudo systemctl stop mariadb
sudo yum -y remove mariadb-server
```
Output confirmed: `Complete!` ✅

#### Step 2 — Get CafeInstance ID (on CLI Host)
```bash
aws ec2 describe-instances \
--filters "Name=tag:Name,Values= CafeInstance" \
--query "Reservations[*].Instances[*].InstanceId"
```

#### Step 3 — Stop, Resize, and Restart Instance
```bash
# Stop the instance
aws ec2 stop-instances --instance-ids <Instance ID>

# Change instance type to t3.micro
aws ec2 modify-instance-attribute \
--instance-id <Instance ID> \
--instance-type "{\"Value\": \"t3.micro\"}"

# Start the instance
aws ec2 start-instances --instance-ids <Instance ID>

# Verify running state and get new DNS/IP
aws ec2 describe-instances \
--instance-ids <Instance ID> \
--query "Reservations[*].Instances[*].[InstanceType,PublicDnsName,PublicIpAddress,State.Name]"
```

#### Step 4 — Verify Website
- Accessed `http://<New Public DNS>/cafe`
- Confirmed website loaded and functioned correctly ✅

---

### Task 2: AWS Pricing Calculator

#### Before Optimization Configuration
| Service | Configuration | Cost |
|---|---|---|
| EC2 | t3.small, Linux, On-Demand, 40GB gp2 | ~$20.89/mo |
| RDS | db.t3.micro, MariaDB, 20GB gp2 | ~$14.71/mo |
| **Total** | | **~$35.60/mo** |

#### After Optimization Configuration
| Service | Configuration | Cost |
|---|---|---|
| EC2 | t3.micro, Linux, On-Demand, 20GB gp2 | ~$10.47/mo |
| RDS | db.t3.micro, MariaDB, 20GB gp2 | ~$14.71/mo |
| **Total** | | **~$25.18/mo** |

#### Projected Monthly Savings
```
Before Optimization:  ~$35.60/month
After Optimization:   ~$25.18/month
                      ---------------
Monthly Savings:      ~$10.42/month
Annual Savings:       ~$125.04/year
```

---

## 💡 Key Concepts Learned

- **Right-sizing** EC2 instances to match actual workload 
requirements is a key cost optimization strategy
- Removing unused software reduces both **CPU overhead** 
and **storage costs**
- The **AWS Pricing Calculator** helps estimate and compare 
costs before making infrastructure changes
- When an EC2 instance is **restarted**, it gets a new 
**Public IP and DNS name** (use Elastic IP to keep it static)
- The `modify-instance-attribute` CLI command can change 
instance type while the instance is **stopped**
- Small optimizations can add up to significant 
**annual savings**

---

## ✅ Lab Outcome

Successfully uninstalled the local MariaDB database, downsized 
the Café instance from t3.small to t3.micro, verified the 
website continued to work, and used the AWS Pricing Calculator 
to confirm monthly savings of approximately $10.42/month.

---

*Lab completed as part of the **AWS re/Start Program** — 
Cloud Practitioner track.*