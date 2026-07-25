# 🌐 Creating a Website on S3

## 📖 Lab Overview

In this lab, I used the **AWS CLI** from an EC2 instance to create 
an Amazon S3 bucket, configure an IAM user with S3 access, upload 
a static website, and create a reusable bash script to update the 
website efficiently.

---

## 🎯 Objectives

- [x] Run AWS CLI commands for IAM and Amazon S3 services
- [x] Deploy a static website to an S3 bucket
- [x] Create a script to copy files from local directory to S3
- [x] Use aws s3 sync for efficient updates

---

## 🛠️ AWS Services Used

| Service | Purpose |
|---|---|
| Amazon S3 | Static website hosting |
| AWS IAM | Creating user with S3 permissions |
| Amazon EC2 | Instance used to run AWS CLI commands |
| AWS CLI | All operations performed via command line |

---

## 📋 Step-by-Step Summary

### Task 1 & 2: Connect and Configure
- Connected to EC2 instance via **SSM Session Manager**
- Switched to ec2-user: `sudo su -l ec2-user`
- Configured AWS CLI with AccessKey, SecretKey, 
region `us-west-2`

### Task 3: Create S3 Bucket
```bash
aws s3api create-bucket --bucket <bucket-name> \
--region us-west-2 \
--create-bucket-configuration LocationConstraint=us-west-2
```

### Task 4: Create IAM User
```bash
# Create user
aws iam create-user --user-name awsS3user

# Set password
aws iam create-login-profile --user-name awsS3user \
--password Training123!

# Grant S3 full access
aws iam attach-user-policy \
--policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess \
--user-name awsS3user
```

### Task 5: Configure Bucket Permissions
- Disabled **Block Public Access** on the bucket
- Enabled **ACLs** under Object Ownership

### Task 6: Extract Website Files
```bash
cd ~/sysops-activity-files
tar xvzf static-website-v2.tar.gz
cd static-website
ls
```
Confirmed: `index.html`, `css/`, `images/` present ✅

### Task 7: Upload to S3
```bash
# Set as website
aws s3 website s3://<bucket-name>/ --index-document index.html

# Upload all files
aws s3 cp /home/ec2-user/sysops-activity-files/static-website/ \
s3://<bucket-name>/ --recursive --acl public-read

# Verify
aws s3 ls <bucket-name>
```
Website accessible at S3 bucket endpoint URL ✅

### Task 8: Create Update Script
```bash
# Create script
touch update-website.sh
vi update-website.sh
```

Script contents:
```bash
#!/bin/bash
aws s3 cp /home/ec2-user/sysops-activity-files/static-website/ \
s3://<bucket-name>/ --recursive --acl public-read
```

```bash
# Make executable
chmod +x update-website.sh

# Edit website colors in index.html
# aquamarine → gainsboro
# orange → cornsilk

# Run script
./update-website.sh
```
Website colors updated successfully ✅

### Optional Challenge: Use sync
```bash
aws s3 sync /home/ec2-user/sysops-activity-files/static-website/ \
s3://<bucket-name>/ --acl public-read
```
`sync` only uploads **changed files** — much more efficient 
than `cp --recursive` which uploads everything every time ✅

---

## 💡 Key Concepts Learned

- **Amazon S3** can host static websites accessible via 
a public endpoint URL
- **IAM users** need explicit permissions to access S3 — 
`AmazonS3FullAccess` grants full access
- **ACLs** must be enabled to make individual objects 
publicly readable
- The `--acl public-read` flag makes uploaded files 
publicly accessible
- `aws s3 cp --recursive` uploads all files in a directory
- `aws s3 sync` is more efficient — only uploads files 
that have changed
- **Bash scripts** can automate repetitive deployment tasks
- S3 static website hosting requires setting an 
**index document**

---

## ✅ Lab Outcome

Successfully created an S3 bucket, configured IAM permissions, 
uploaded a static website, modified website colors, and created 
a reusable deployment script. The website was publicly accessible 
via the S3 bucket endpoint URL.

---

*Lab completed as part of the **AWS re/Start Program** — 
Cloud Practitioner track.*