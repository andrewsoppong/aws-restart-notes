# 🗄️ Managing Storage

## 📖 Lab Overview

In this lab, I managed EBS snapshots using the AWS CLI, configured 
a cron job to automatically create snapshots every minute, ran a 
Python script to retain only the two most recent snapshots, and 
synced files between an EC2 instance and an Amazon S3 bucket. 
I also used S3 versioning to recover a deleted file.

---

## 🏗️ Lab Architecture

- A **VPC** with a public subnet
- **Command Host** EC2 instance — used to run AWS CLI commands 
and manage snapshots
- **Processor** EC2 instance — the instance whose EBS volume 
is being snapshotted
- An **S3 bucket** — used to sync files from the EBS volume

---

## 🎯 Objectives

- [x] Create and maintain snapshots for Amazon EC2 instances
- [x] Use Amazon S3 sync to copy files from an EBS volume 
to an S3 bucket
- [x] Use Amazon S3 versioning to retrieve deleted files

---

## 🛠️ AWS Services Used

| Service | Purpose |
|---|---|
| Amazon EBS | Block storage volume for the Processor instance |
| Amazon EC2 | Command Host and Processor instances |
| Amazon S3 | File storage and versioning |
| AWS CLI | All operations performed via command line |
| IAM | S3BucketAccess role attached to Processor instance |

---

## 📋 Step-by-Step Summary

### Task 1: Create and Configure Resources

#### Task 1.1 — Create S3 Bucket
- Created an S3 bucket with a unique name to store synced files

#### Task 1.2 — Attach IAM Role to Processor
- Attached the **S3BucketAccess** IAM role to the **Processor** 
instance via Actions → Security → Modify IAM role

---

### Task 2: Taking Snapshots

#### Task 2.1 — Connect to Command Host
- Connected to **Command Host** via EC2 Instance Connect

#### Task 2.2 — Take Initial Snapshot
- Retrieved the EBS Volume ID and Instance ID of the 
Processor instance
- Stopped the Processor instance before taking snapshot
- Created initial snapshot and waited for completion
- Restarted the Processor instance

```bash
# Get Volume ID
aws ec2 describe-instances --filter 'Name=tag:Name,Values=Processor' \
--query 'Reservations[0].Instances[0].BlockDeviceMappings[0].Ebs.{VolumeId:VolumeId}'

# Stop instance
aws ec2 stop-instances --instance-ids INSTANCE-ID
aws ec2 wait instance-stopped --instance-id INSTANCE-ID

# Create snapshot
aws ec2 create-snapshot --volume-id VOLUME-ID
aws ec2 wait snapshot-completed --snapshot-id SNAPSHOT-ID

# Restart instance
aws ec2 start-instances --instance-ids INSTANCE-ID
```

#### Task 2.3 — Schedule Automatic Snapshots
- Created a cron job to take a new snapshot every minute
- Verified multiple snapshots were being created

```bash
echo "* * * * *  aws ec2 create-snapshot --volume-id VOLUME-ID \
2>&1 >> /tmp/cronlog" > cronjob
crontab cronjob
```

#### Task 2.4 — Retain Only Last Two Snapshots
- Stopped the cron job with `crontab -r`
- Reviewed the `snapshotter_v2.py` Python script
- Ran the script to delete all but the 2 most recent snapshots
- Confirmed only 2 snapshot IDs remained

```bash
crontab -r
python3.8 snapshotter_v2.py
aws ec2 describe-snapshots --filters "Name=volume-id, \
Values=VOLUME-ID" --query 'Snapshots[*].SnapshotId'
```

---

### Task 3: Sync Files with Amazon S3

#### Task 3.1 — Download Sample Files on Processor
- Connected to **Processor** instance via EC2 Instance Connect
- Downloaded and unzipped sample files (file1.txt, file2.txt, 
file3.txt)

```bash
wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/\
CUR-TF-100-RSJAWS-3-124627/183-lab-JAWS-managing-storage/s3/files.zip
unzip files.zip
```

#### Task 3.2 — Sync, Delete, and Recover Files
- Enabled **S3 versioning** on the bucket
- Synced local files to S3 using `aws s3 sync`
- Deleted `file1.txt` locally and synced with `--delete` flag 
to remove it from S3
- Used `aws s3api list-object-versions` to find the old version
- Recovered deleted file using `aws s3api get-object` 
with the version ID
- Re-synced restored file back to S3

```bash
# Enable versioning
aws s3api put-bucket-versioning --bucket S3-BUCKET-NAME \
--versioning-configuration Status=Enabled

# Sync files to S3
aws s3 sync files s3://S3-BUCKET-NAME/files/

# Delete file locally and sync deletion to S3
rm files/file1.txt
aws s3 sync files s3://S3-BUCKET-NAME/files/ --delete

# List versions and recover deleted file
aws s3api list-object-versions --bucket S3-BUCKET-NAME \
--prefix files/file1.txt

aws s3api get-object --bucket S3-BUCKET-NAME \
--key files/file1.txt --version-id VERSION-ID files/file1.txt

# Re-sync restored file to S3
aws s3 sync files s3://S3-BUCKET-NAME/files/
```

---

## 💡 Key Concepts Learned

- **EBS Snapshots** are point-in-time backups of EBS volumes 
stored in Amazon S3
- Best practice is to **stop an instance** before taking a 
snapshot to ensure data consistency
- **Cron jobs** can automate recurring tasks like snapshot 
creation on Linux
- Python scripts can be used to **manage and clean up** 
old snapshots automatically
- **Amazon S3 sync** keeps a local folder and S3 bucket 
in sync efficiently
- The `--delete` flag in `aws s3 sync` removes files from S3 
that no longer exist locally
- **S3 Versioning** preserves previous versions of objects, 
allowing recovery of deleted files
- There is no direct restore command in S3 — recovery requires 
downloading the old version and re-syncing

---

## ✅ Lab Outcome

Successfully created and managed EBS snapshots using the AWS CLI, 
automated snapshot creation with cron, cleaned up old snapshots 
with a Python script, synced files to S3, simulated file deletion, 
and recovered the deleted file using S3 versioning.

---

*Lab completed as part of the **AWS re/Start Program** — 
Cloud Practitioner track.*