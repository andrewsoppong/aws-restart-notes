# AWS Systems Manager Lab — Markdown README

## Overview

AWS Systems Manager is a collection of tools that help you manage and automate operations across AWS resources. It allows you to:

* Configure EC2 instances
* Run commands remotely
* Store application settings
* Access instances securely without SSH

---

# Objectives

By the end of this lab, you will be able to:

* Verify configurations and permissions
* Run tasks on multiple servers
* Update application settings or configurations
* Access the command line on an instance

---

# Lab Duration

Approximate completion time: **30 minutes**

---

# Prerequisites

* AWS Academy / Vocareum lab access
* AWS Management Console access
* Active lab environment

---

# Access the AWS Management Console

1. Choose **Start Lab**
2. Wait until the lab status changes to **Ready**
3. Choose **AWS** to open the AWS Console
4. Keep the lab instructions open beside the console

> **Important:** Do not change the AWS Region unless instructed.

---

# Task 1 — Generate Inventory Lists for Managed Instances

## Open Systems Manager

1. In the AWS Console search bar, search for:

```text
Systems Manager
```

2. Open **Systems Manager**

---

## Configure Inventory Collection

1. In the left navigation pane:

```text
Node Management → Fleet Manager
```

2. Choose:

```text
Set up inventory
```

---

## Inventory Configuration

### Provide Inventory Details

| Setting | Value                 |
| ------- | --------------------- |
| Name    | Inventory-Association |

---

### Targets

| Setting            | Value                        |
| ------------------ | ---------------------------- |
| Specify targets by | Manually selecting instances |
| Instance           | Managed Instance             |

---

3. Choose:

```text
Setup Inventory
```

---

## Review Inventory Data

1. Choose the **Node ID**
2. Open the **Inventory** tab
3. Review:

   * Installed applications
   * OS information
   * Inventory types

---

# Task 2 — Install a Custom Application Using Run Command

## Open Run Command

1. In Systems Manager:

```text
Node Management → Run Command
```

2. Choose:

```text
Run command
```

---

## Select the Command Document

1. Use the filter dropdown:

| Filter | Value       |
| ------ | ----------- |
| Owner  | Owned by me |

2. Select the available document.

### Document Information

| Setting     | Value                 |
| ----------- | --------------------- |
| Description | Install Dashboard App |
| Version     | 1 (Default)           |

---

## Configure Targets

1. Under **Target selection**, choose:

```text
Choose instances manually
```

2. Select:

```text
Managed Instance
```

---

## Configure Output Options

Clear:

```text
Enable an S3 bucket
```

---

## Execute the Command

1. Choose:

```text
Run
```

2. Wait until the command status becomes:

```text
Success
```

---

## Validate the Installation

1. Open the **Details** dropdown in Vocareum
2. Copy the:

```text
ServerIP
```

3. Paste the IP into a browser

### Result

The **Widget Manufacturing Dashboard** loads successfully.

---

# Task 3 — Use Parameter Store

Parameter Store stores application configuration values securely.

---

## Open Parameter Store

1. In Systems Manager:

```text
Application Management → Parameter Store
```

2. Choose:

```text
Create parameter
```

---

## Create a Parameter

| Setting     | Value                         |
| ----------- | ----------------------------- |
| Name        | /dashboard/show-beta-features |
| Description | Display beta features         |
| Tier        | Standard                      |
| Type        | String                        |
| Value       | True                          |

3. Choose:

```text
Create parameter
```

---

## Validate the Feature

1. Refresh the dashboard webpage

### Result

A third beta chart appears.

---

## Optional

Delete the parameter and refresh the page.

### Result

The beta chart disappears.

---

# Task 4 — Use Session Manager

Session Manager allows secure shell access without SSH.

---

## Start a Session

1. Navigate to:

```text
Node Management → Session Manager
```

2. Choose:

```text
Start session
```

3. Select:

```text
Managed Instance
```

4. Choose:

```text
Start session
```

---

# Run Commands

## List Application Files

```bash
ls /var/www/html
```

---

## Retrieve EC2 Instance Information

```bash
# Get region
AZ=`curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone`
export AWS_DEFAULT_REGION=${AZ::-1}

# Describe EC2 instances
aws ec2 describe-instances
```

---

# Benefits of Session Manager

* No SSH keys required
* No inbound SSH ports required
* Secure browser-based access
* IAM-controlled permissions
* CloudTrail auditing support

---

# AWS Systems Manager Features Used

| Feature         | Purpose                           |
| --------------- | --------------------------------- |
| Fleet Manager   | Inventory and instance management |
| Run Command     | Remote command execution          |
| Parameter Store | Configuration management          |
| Session Manager | Secure instance access            |

---

# Conclusion

You successfully completed the following tasks:

* Verified configurations and permissions
* Ran tasks remotely on EC2 instances
* Updated application settings
* Accessed the command line securely

---

# Useful Commands

## List EC2 Instances

```bash
aws ec2 describe-instances
```

## List Installed Application Files

```bash
ls /var/www/html
```

---

# Cleanup

1. Choose:

```text
End Lab
```

2. Confirm by choosing:

```text
Yes
```

AWS resources will terminate automatically.
