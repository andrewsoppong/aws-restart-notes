# Lab: Managing Resources with Tagging

## Overview

This lab demonstrates how to use AWS resource tags to organize, locate, and manage Amazon EC2 instances. You will use the AWS Command Line Interface (AWS CLI) and AWS SDK for PHP to identify resources based on tags, update tags in bulk, and automate instance lifecycle operations.

The lab consists of:

1. Managing EC2 resources using tags.
2. Stopping and starting EC2 instances based on tag values.
3. Implementing a "tag-or-terminate" compliance policy.

---

## Objectives

After completing this lab, you will be able to:

* Apply tags to AWS resources.
* Locate AWS resources using tags.
* Use AWS CLI queries with JMESPath.
* Modify resource tags programmatically.
* Stop and start EC2 instances based on tags.
* Identify and terminate non-compliant EC2 instances.

---

## Architecture

The environment contains:

* Amazon VPC (Lab VPC)
* Public Subnet
* Private Subnet
* CommandHost EC2 instance
* 8 Linux EC2 instances

### Custom Tags

| Tag         | Description                      |
| ----------- | -------------------------------- |
| Project     | ERPSystem or Experiment1         |
| Version     | Application version              |
| Environment | development, staging, production |

---

# Task 1: Using Tags to Manage Resources

## Connect to Command Host

### Windows

1. Download the PPK key.
2. Open PuTTY.
3. Connect using the provided Public IP.

### macOS/Linux

```bash
chmod 400 labsuser.pem

ssh -i labsuser.pem ec2-user@<public-ip>
```

---

## Find Instances by Tag

Find all instances with Project=ERPSystem:

```bash
aws ec2 describe-instances \
--filter "Name=tag:Project,Values=ERPSystem"
```

---

## Return Only Instance IDs

```bash
aws ec2 describe-instances \
--filter "Name=tag:Project,Values=ERPSystem" \
--query 'Reservations[*].Instances[*].InstanceId'
```

---

## Return Multiple Properties

```bash
aws ec2 describe-instances \
--filter "Name=tag:Project,Values=ERPSystem" \
--query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone}'
```

---

## Include Tag Values

```bash
aws ec2 describe-instances \
--filter "Name=tag:Project,Values=ERPSystem" \
--query 'Reservations[*].Instances[*].{
ID:InstanceId,
AZ:Placement.AvailabilityZone,
Project:Tags[?Key==`Project`] | [0].Value}'
```

---

## Include Project, Environment, and Version

```bash
aws ec2 describe-instances \
--filter "Name=tag:Project,Values=ERPSystem" \
--query 'Reservations[*].Instances[*].{
ID:InstanceId,
AZ:Placement.AvailabilityZone,
Project:Tags[?Key==`Project`] | [0].Value,
Environment:Tags[?Key==`Environment`] | [0].Value,
Version:Tags[?Key==`Version`] | [0].Value}'
```

---

## Filter Development Instances

```bash
aws ec2 describe-instances \
--filter "Name=tag:Project,Values=ERPSystem" \
"Name=tag:Environment,Values=development" \
--query 'Reservations[*].Instances[*].{
ID:InstanceId,
AZ:Placement.AvailabilityZone,
Project:Tags[?Key==`Project`] | [0].Value,
Environment:Tags[?Key==`Environment`] | [0].Value,
Version:Tags[?Key==`Version`] | [0].Value}'
```

---

## Update Version Tags

Open script:

```bash
nano change-resource-tags.sh
```

Contents:

```bash
#!/bin/bash

ids=$(aws ec2 describe-instances \
--filter "Name=tag:Project,Values=ERPSystem" \
"Name=tag:Environment,Values=development" \
--query 'Reservations[*].Instances[*].InstanceId' \
--output text)

aws ec2 create-tags \
--resources $ids \
--tags 'Key=Version,Value=1.1'
```

Run script:

```bash
./change-resource-tags.sh
```

Verify changes:

```bash
aws ec2 describe-instances \
--filter "Name=tag:Project,Values=ERPSystem" \
--query 'Reservations[*].Instances[*].{
ID:InstanceId,
AZ:Placement.AvailabilityZone,
Project:Tags[?Key==`Project`] | [0].Value,
Environment:Tags[?Key==`Environment`] | [0].Value,
Version:Tags[?Key==`Version`] | [0].Value}'
```

---

# Task 2: Stop and Start Resources by Tag

## Examine stopinator.php

Navigate to directory:

```bash
cd aws-tools
```

Open file:

```bash
nano stopinator.php
```

### Parameters

| Parameter | Purpose                             |
| --------- | ----------------------------------- |
| -t        | Tag filter                          |
| -s        | Start instances instead of stopping |

Example:

```bash
Project=ERPSystem;Environment=development
```

---

## Stop Development Instances

```bash
./stopinator.php \
-t"Project=ERPSystem;Environment=development"
```

Verify in EC2 Console.

---

## Start Development Instances

```bash
./stopinator.php \
-t"Project=ERPSystem;Environment=development" \
-s
```

Verify instances restart.

---

# Task 3: Challenge - Tag-or-Terminate Policy

## Goal

Terminate all instances in a subnet that do NOT have the Environment tag.

---

## Solution Approach

1. Find all instances with Environment tag.
2. Find all instances in subnet.
3. Compare lists.
4. Terminate non-compliant instances.

---

## Review Script

Open:

```bash
nano terminate-instances.php
```

### Parameters

| Parameter | Description   |
| --------- | ------------- |
| region    | AWS Region    |
| subnetid  | Target subnet |

---

## Prepare Environment

In EC2 Console:

1. Select two private subnet instances.
2. Remove Environment tag.
3. Save changes.

---

## Get Required Values

From EC2 Console:

* Region
* Subnet ID

---

## Run Compliance Script

```bash
./terminate-instances.php \
-region <region> \
-subnetid <subnet-id>
```

Example:

```bash
./terminate-instances.php \
-region us-west-2 \
-subnetid subnet-12345678
```

Expected output:

```text
Checking i-xxxxxxxx
Checking i-yyyyyyyy
Checking i-zzzzzzzz

Terminating instances...
Instances terminated.
```

---

# JMESPath Examples Used

### Return Instance IDs

```bash
Reservations[*].Instances[*].InstanceId
```

### Return Multiple Properties

```bash
Reservations[*].Instances[*].{
ID:InstanceId,
AZ:Placement.AvailabilityZone
}
```

### Return Project Tag

```bash
Tags[?Key==`Project`] | [0].Value
```

### Return Environment Tag

```bash
Tags[?Key==`Environment`] | [0].Value
```

### Return Version Tag

```bash
Tags[?Key==`Version`] | [0].Value
```

---

# Key AWS Services

* Amazon EC2
* Amazon VPC
* AWS CLI
* AWS SDK for PHP
* Resource Tagging

---

# Key Concepts Learned

* Resource tagging strategy
* AWS CLI filtering
* JMESPath queries
* Bulk tag updates
* Automated instance management
* Compliance automation
* Tag-based lifecycle control

---

## Result

Successfully:

* Located EC2 instances using tags.
* Updated Version tags programmatically.
* Stopped and restarted development environments.
* Implemented a tag-or-terminate compliance workflow.
* Used JMESPath queries to extract targeted AWS resource information.
