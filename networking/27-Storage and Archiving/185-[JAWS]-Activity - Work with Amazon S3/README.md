# 🪣 Working with Amazon S3

## 📖 Lab Overview

In this lab, I created and configured an **Amazon S3 bucket** for 
secure image sharing with an external media company user 
(mediacouser). I reviewed IAM permissions, configured **SNS email 
notifications** for bucket events, and tested all operations using 
both the AWS Management Console and AWS CLI.

---

## 🏗️ Lab Architecture

- An **S3 bucket** (`cafe-xxxnnn`) used for image sharing
- An **IAM user** (`mediacouser`) with scoped permissions to the 
`cafe-*/images/*` folder
- An **SNS topic** (`s3NotificationTopic`) that sends email 
notifications when bucket contents change
- A **CLI Host** EC2 instance used to run AWS CLI commands

---

## 🎯 Objectives

- [x] Use s3api and s3 AWS CLI commands to create and configure 
an S3 bucket
- [x] Verify write permissions for a user on an S3 bucket
- [x] Configure event notifications on an S3 bucket

---

## 🛠️ AWS Services Used

| Service | Purpose |
|---|---|
| Amazon S3 | Image storage and file sharing |
| AWS IAM | User and group permissions management |
| Amazon SNS | Email notifications for bucket events |
| Amazon EC2 | CLI Host for running AWS CLI commands |
| AWS CLI | All bucket operations performed via command line |

---

## 📋 Step-by-Step Summary

### Task 1: Connect and Configure CLI
- Connected to **CLI Host** via EC2 Instance Connect
- Configured AWS CLI with AccessKey, SecretKey, and 
region `us-west-2`

### Task 2: Create and Initialize S3 Bucket
- Created S3 bucket `cafe-xxxnnn` using `aws s3 mb`
- Uploaded sample images using `aws s3 sync`
- Verified uploads with `aws s3 ls`

```bash
aws s3 mb s3://cafe-xxxnnn --region 'us-west-2'
aws s3 sync ~/initial-images/ s3://cafe-xxxnnn/images
aws s3 ls s3://cafe-xxxnnn/images/ --human-readable --summarize
```

### Task 3: Review IAM Permissions

#### mediaco Group Policy (mediaCoPolicy):
- **AllowGroupToSeeBucketListInTheConsole** — view S3 bucket list
- **AllowRootLevelListingOfTheBucket** — view objects in bucket
- **AllowUserSpecificActionsOnlyInTheSpecificPrefix** — 
GetObject, PutObject, DeleteObject on `cafe-*/images/*`

#### mediacouser Tests (via Console):
- ✅ **View** — opened Donuts.jpg successfully
- ✅ **Upload** — uploaded a local image successfully
- ✅ **Delete** — deleted Cup-of-Hot-Chocolate.jpg successfully
- ✅ **Unauthorized** — could not change bucket permissions 
(Insufficient permissions error)

### Task 4: Configure Event Notifications

#### SNS Topic Setup:
- Created **s3NotificationTopic** SNS topic (Standard type)
- Configured access policy to allow S3 to publish to the topic
- Subscribed with email address and confirmed subscription

#### S3 Event Notification Config:
- Created `s3EventNotification.json` using `vi` editor
- Applied config to bucket using `put-bucket-notification-configuration`
- Received test notification email confirming setup ✅

### Task 5: Test Event Notifications (as mediacouser)

Reconfigured AWS CLI with mediacouser credentials, then tested:

```bash
# Upload (PUT) - triggers notification
aws s3api put-object --bucket cafe-xxxnnn \
--key images/Caramel-Delight.jpg \
--body ~/new-images/Caramel-Delight.jpg

# Download (GET) - no notification triggered
aws s3api get-object --bucket cafe-xxxnnn \
--key images/Donuts.jpg Donuts.jpg

# Delete - triggers notification
aws s3api delete-object --bucket cafe-xxxnnn \
--key images/Strawberry-Tarts.jpg

# Unauthorized - AccessDenied error expected
aws s3api put-object-acl --bucket cafe-xxxnnn \
--key images/Donuts.jpg --acl public-read
```

---

## 💡 Key Concepts Learned

- **Amazon S3** can be used as a secure file-sharing platform 
with scoped IAM permissions
- **IAM Groups** make it easy to manage permissions for 
multiple users with the same role
- **IAM Policies** can restrict access to specific S3 prefixes 
(folders) and specific actions
- **Amazon SNS** can send email notifications when S3 bucket 
events occur
- S3 event notifications are triggered by **ObjectCreated** 
and **ObjectRemoved** events but NOT by GET operations
- The **--delete** flag in `aws s3 sync` removes files from S3 
that no longer exist locally
- **Access Denied** errors confirm that unauthorized operations 
are correctly blocked by IAM policies
- Using a **separate browser session** or incognito window 
allows testing multiple IAM users simultaneously

---

## ✅ Lab Outcome

Successfully created and configured an Amazon S3 bucket for 
secure image sharing. Verified that mediacouser had the correct 
scoped permissions, set up SNS email notifications for bucket 
changes, and confirmed all authorized and unauthorized operations 
behaved as expected.

---

*Lab completed as part of the **AWS re/Start Program** — 
Cloud Practitioner track.*