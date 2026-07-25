# 🪣 Challenge Lab: Amazon S3

## 📖 Lab Overview

In this challenge lab, I created an **Amazon S3 bucket**, uploaded 
an object, configured public access permissions, accessed the object 
via a web browser, and listed the bucket contents using the AWS CLI.

---

## 🎯 Objectives

- [x] Create an S3 bucket
- [x] Upload an object into the bucket
- [x] Attempt to access the object before making it public
- [x] Make the object publicly accessible
- [x] Access the object successfully via web browser
- [x] List the S3 bucket contents using the AWS CLI

---

## 🛠️ AWS Services Used

| Service | Purpose |
|---|---|
| Amazon S3 | Object storage bucket |
| AWS CLI | Bucket creation, upload, and listing |
| EC2 Instance Connect | Terminal access to CLI Host |

---

## 📋 Step-by-Step Summary

### Task 1 & 2: Connect and Configure
- Connected to **CLI Host** via EC2 Instance Connect
- Configured AWS CLI with AccessKey, SecretKey, 
and region `us-west-2`

### Task 3: Complete the Challenge

#### Step 1 — Create S3 Bucket
```bash
aws s3 mb s3://challenge-andrews2026 --region 'us-west-2'
```

#### Step 2 — Create and Upload a File
```bash
echo "Hello from Andrews S3 Challenge Lab!" > myfile.txt
aws s3 cp myfile.txt s3://challenge-andrews2026/myfile.txt
```

#### Step 3 — Test Access Before Making Public
- Copied the Object URL from S3 console
- Pasted in browser → received **Access Denied** error ✅

#### Step 4 — Make Object Publicly Accessible
- Disabled **Block Public Access** on the bucket via S3 console
- Applied public-read ACL via AWS CLI:
```bash
aws s3api put-object-acl --bucket challenge-andrews2026 \
--key myfile.txt --acl public-read
```

#### Step 5 — Access Object in Browser
- Pasted Object URL in browser
- File contents displayed successfully ✅

#### Step 6 — List Bucket Contents via CLI
```bash
aws s3 ls s3://challenge-andrews2026 --human-readable --summarize
```

---

## 💡 Key Concepts Learned

- S3 bucket names must be **globally unique** across all AWS accounts
- By default, all S3 objects are **private** — access must be 
explicitly granted
- **Block Public Access** settings must be disabled before 
objects can be made public
- The `--acl public-read` flag makes a specific object 
publicly accessible without making the entire bucket public
- `aws s3 ls` lists bucket contents from the command line
- `aws s3 cp` uploads files to S3
- `aws s3 mb` creates a new S3 bucket

---

## ✅ Lab Outcome

Successfully created an S3 bucket, uploaded an object, configured 
public access at the object level, verified browser access, and 
listed bucket contents via the AWS CLI.

---

*Lab completed as part of the **AWS re/Start Program** — 
Cloud Practitioner track.*