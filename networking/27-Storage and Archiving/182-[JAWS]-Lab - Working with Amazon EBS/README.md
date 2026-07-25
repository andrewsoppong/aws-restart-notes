# 💾 Working with Amazon EBS

## 📖 Lab Overview

In this lab, I created and managed an **Amazon Elastic Block Store 
(EBS)** volume. I attached it to an EC2 instance, created a file 
system, stored data on it, took a snapshot backup, simulated data 
loss, and successfully restored the data from the snapshot.

---

## 🏗️ Lab Architecture

- An **EC2 instance** (Lab) already running in a public subnet
- A new **1 GiB EBS volume** (My Volume) created and attached 
to the instance
- A **snapshot** (My Snapshot) taken from the volume
- A **Restored Volume** created from the snapshot and attached 
to the same instance

---

## 🎯 Objectives

- [x] Create an EBS volume
- [x] Attach and mount an EBS volume to an EC2 instance
- [x] Create a snapshot of an EBS volume
- [x] Create an EBS volume from a snapshot and restore data

---

## 🛠️ AWS Services Used

| Service | Purpose |
|---|---|
| Amazon EBS | Block storage volumes for EC2 |
| Amazon EC2 | Virtual server the volumes are attached to |
| Amazon S3 | Where EBS snapshots are stored durably |
| EC2 Instance Connect | Terminal access to the EC2 instance |

---

## 📋 Step-by-Step Summary

### Task 1: Create a New EBS Volume
- Created a **1 GiB General Purpose SSD (gp2)** volume
- Set Availability Zone to match the Lab EC2 instance
- Tagged it as **My Volume**
- Confirmed status changed to **Available**

### Task 2: Attach the Volume
- Attached **My Volume** to the **Lab** EC2 instance
- Used device name `/dev/sdb`
- Confirmed status changed to **In-use**

### Task 3: Connect to the EC2 Instance
- Connected to the **Lab** instance via EC2 Instance Connect

### Task 4: Create and Configure the File System
- Ran `df -h` to view existing storage
- Formatted the new volume as **ext3** using `mkfs`
- Created mount point `/mnt/data-store`
- Mounted the volume and made it persistent via `/etc/fstab`
- Created a test file with text on the new volume
- Verified the file contents with `cat`

```bash
sudo mkfs -t ext3 /dev/sdb
sudo mkdir /mnt/data-store
sudo mount /dev/sdb /mnt/data-store
echo "/dev/sdb   /mnt/data-store ext3 defaults,noatime 1 2" | sudo tee -a /etc/fstab
sudo sh -c "echo some text has been written > /mnt/data-store/file.txt"
cat /mnt/data-store/file.txt
```

### Task 5: Create an EBS Snapshot
- Created a snapshot of **My Volume** tagged as **My Snapshot**
- Waited for snapshot status to show **Completed**
- Deleted the test file to simulate data loss
- Confirmed the file was gone

### Task 6: Restore the EBS Snapshot
- Created **Restored Volume** from **My Snapshot**
- Attached it to the Lab instance using device name `/dev/sdc`
- Created mount point `/mnt/data-store2` and mounted the volume
- Confirmed `file.txt` was restored successfully ✅

```bash
sudo mkdir /mnt/data-store2
sudo mount /dev/sdc /mnt/data-store2
ls /mnt/data-store2/file.txt
```

---

## 💡 Key Concepts Learned

- **Amazon EBS** volumes are like virtual hard drives that can be 
attached to EC2 instances
- EBS volumes must be in the **same Availability Zone** as the 
EC2 instance they are attached to
- A volume must be **formatted** with a file system before use
- Adding an entry to `/etc/fstab` ensures the volume is 
**automatically mounted** after a restart
- **EBS Snapshots** are point-in-time backups stored in Amazon S3
- Snapshots only store **used blocks** — empty space is not billed
- A new EBS volume can be created from a snapshot to **restore data** 
or **clone** a volume
- Snapshots can be shared across AWS accounts or copied to 
other regions

---

## ✅ Lab Outcome

Successfully created, attached, and configured an EBS volume on 
an EC2 instance. Demonstrated data backup and recovery using 
EBS snapshots by simulating data loss and restoring the file 
from a snapshot to a new volume.

---

*Lab completed as part of the **AWS re/Start Program** — 
Cloud Practitioner track.*