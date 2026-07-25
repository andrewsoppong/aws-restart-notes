# 💻 Creating Amazon EC2 Instances

## 📖 Lab Overview

In this lab, I launched EC2 instances using two different methods — 
the **AWS Management Console** and the **AWS CLI**. I launched a 
**Bastion Host** via the console, connected to it using EC2 Instance 
Connect, and then used the **AWS CLI** from inside the bastion host 
to launch a **Web Server** instance with Apache installed automatically.

---

## 🏗️ Final Architecture

- **Bastion Host** — EC2 instance in public subnet, launched 
via AWS Console
- **Web Server** — EC2 instance in public subnet, launched 
via AWS CLI with user data script that installs Apache

---

## 🎯 Objectives

- [x] Launch an EC2 instance using the AWS Management Console
- [x] Connect to an EC2 instance using EC2 Instance Connect
- [x] Launch an EC2 instance using the AWS CLI
- [x] Troubleshoot EC2 security group misconfigurations (optional)

---

## 🛠️ AWS Services Used

| Service | Purpose |
|---|---|
| Amazon EC2 | Bastion host and web server instances |
| AWS CLI | Launching web server programmatically |
| AWS Systems Manager | Retrieving latest AMI ID |
| EC2 Instance Connect | Browser-based SSH to bastion host |
| Security Groups | Firewall rules for SSH and HTTP access |
| IAM | Bastion-Role for CLI permissions |

---

## 📋 Step-by-Step Summary

### Task 1: Launch Bastion Host via Console
- Created **Bastion host** instance with:
  - AMI: Amazon Linux 2
  - Instance type: t3.micro
  - VPC: Lab VPC / Public Subnet
  - Security group: `Bastion security group` (SSH)
  - IAM profile: `Bastion-Role`
  - No key pair (using EC2 Instance Connect)

### Task 2: Connect to Bastion Host
- Connected via **EC2 Instance Connect** in the browser ✅

### Task 3: Launch Web Server via AWS CLI

#### Step 1 — Get Latest AMI ID
```bash
AZ=`curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone`
export AWS_DEFAULT_REGION=${AZ::-1}
AMI=$(aws ssm get-parameters \
--names /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 \
--query 'Parameters[0].[Value]' --output text)
echo $AMI
```

#### Step 2 — Get Subnet ID
```bash
SUBNET=$(aws ec2 describe-subnets \
--filters 'Name=tag:Name,Values=Public Subnet' \
--query Subnets[].SubnetId --output text)
echo $SUBNET
```

#### Step 3 — Get Security Group ID
```bash
SG=$(aws ec2 describe-security-groups \
--filters Name=group-name,Values=WebSecurityGroup \
--query SecurityGroups[].GroupId --output text)
echo $SG
```

#### Step 4 — Download User Data Script
```bash
wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/\
CUR-TF-100-RSJAWS-1-23732/171-lab-JAWS-create-ec2/s3/UserData.txt
```

#### Step 5 — Launch Web Server
```bash
INSTANCE=$(\
aws ec2 run-instances \
--image-id $AMI \
--subnet-id $SUBNET \
--security-group-ids $SG \
--user-data file:///home/ec2-user/UserData.txt \
--instance-type t3.micro \
--tag-specifications \
'ResourceType=instance,Tags=[{Key=Name,Value=Web Server}]' \
--query 'Instances[*].InstanceId' \
--output text)
echo $INSTANCE
```

#### Step 6 — Wait for Running State
```bash
aws ec2 describe-instances \
--instance-ids $INSTANCE \
--query 'Reservations[].Instances[].State.Name' \
--output text
```

#### Step 7 — Get and Test Web Server URL
```bash
aws ec2 describe-instances \
--instance-ids $INSTANCE \
--query Reservations[].Instances[].PublicDnsName \
--output text
```
Pasted DNS name in browser — web page loaded successfully ✅

---

### Optional Challenge 1: Fix SSH Access
- **Problem:** Security group missing SSH inbound rule
- **Fix:** Added SSH rule (port 22) from Anywhere to 
the Misconfigured Web Server security group ✅

### Optional Challenge 2: Fix Web Server Access
- **Problem:** Security group missing HTTP inbound rule
- **Fix:** Added HTTP rule (port 80) from Anywhere to 
the Misconfigured Web Server security group ✅

---

## 💡 Key Concepts Learned

- The **AWS Console** is best for quickly launching 
one-off instances
- The **AWS CLI** is best for automating and scripting 
repeatable deployments
- **User data scripts** run automatically on first launch 
and can install software
- **AWS Systems Manager Parameter Store** stores the 
latest AMI IDs — always use this for automation
- **EC2 Instance Connect** allows browser-based SSH 
without key pairs
- **IAM instance profiles** give EC2 instances permission 
to call other AWS services
- **Security groups** must have the correct inbound rules 
for SSH (port 22) and HTTP (port 80)
- Environment variables store CLI command outputs 
for use in subsequent commands

---

## ✅ Lab Outcome

Successfully launched a Bastion Host via the AWS Console and 
a Web Server via the AWS CLI. The web server was automatically 
configured with Apache using a user data script. Also 
troubleshot and fixed security group misconfigurations on 
the optional challenge instances.

---

*Lab completed as part of the **AWS re/Start Program** — 
Cloud Practitioner track.*