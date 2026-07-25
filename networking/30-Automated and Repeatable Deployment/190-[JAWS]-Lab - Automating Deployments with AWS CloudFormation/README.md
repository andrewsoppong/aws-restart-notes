# AWS CloudFormation Automation Lab

## Overview

This lab demonstrates how to use AWS CloudFormation to automate infrastructure deployment in AWS. CloudFormation allows infrastructure to be defined as code using YAML or JSON templates, ensuring consistent, repeatable, and reliable deployments.

## Objectives

By completing this lab, you will learn how to:

* Deploy an AWS CloudFormation stack.
* Create a Virtual Private Cloud (VPC).
* Create networking resources using Infrastructure as Code (IaC).
* Add Amazon S3 resources to an existing stack.
* Add Amazon EC2 resources to an existing stack.
* Update CloudFormation stacks.
* Delete CloudFormation stacks and associated resources.

---

# Task 1: Deploy a CloudFormation Stack

## Step 1: Download the Template

Download the provided CloudFormation template:

```bash
task1.yaml
```

Review the template contents.

### Parameters Section

Used to collect user inputs.

Example:

```yaml
Parameters:
  VPCCIDR:
    Type: String
```

### Resources Section

Defines AWS resources to create.

Example:

```yaml
Resources:
  VPC:
    Type: AWS::EC2::VPC
```

### Outputs Section

Displays useful information after deployment.

Example:

```yaml
Outputs:
  DefaultSecurityGroup:
    Value: !Ref AppSecurityGroup
```

---

## Step 2: Create the Stack

1. Open AWS Management Console.
2. Navigate to CloudFormation.
3. Choose **Create Stack**.
4. Select **Upload a Template File**.
5. Upload `task1.yaml`.
6. Click **Next**.

### Stack Configuration

| Setting    | Value |
| ---------- | ----- |
| Stack Name | Lab   |

Leave default parameter values unchanged.

Continue:

```text
Next → Next → Create Stack
```

---

## Verify Deployment

Monitor deployment status:

```text
CREATE_IN_PROGRESS
```

Wait until:

```text
CREATE_COMPLETE
```

Review:

* Events Tab
* Resources Tab

Expected resources:

* VPC
* Subnet
* Route Table
* Security Group

---

# Task 2: Add an Amazon S3 Bucket

## Modify the Template

Add the following resource under the `Resources:` section.

```yaml
S3Bucket:
  Type: AWS::S3::Bucket
```

---

## Update the Stack

1. Open CloudFormation.
2. Select the Lab stack.
3. Choose **Update**.
4. Upload the modified template.
5. Click Next through all screens.
6. Verify Preview Changes shows:

```text
Add AWS::S3::Bucket
```

7. Choose **Update Stack**.

---

## Verify

Wait for:

```text
UPDATE_COMPLETE
```

Check Resources tab.

Expected new resource:

```text
S3Bucket
```

---

# Task 3: Add an Amazon EC2 Instance

## Add Parameter for Latest Amazon Linux AMI

Under the Parameters section add:

```yaml
AmazonLinuxAMIID:
  Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
  Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
```

This automatically retrieves the latest Amazon Linux 2 AMI.

---

## Add EC2 Instance Resource

Under the Resources section add:

```yaml
AppServer:
  Type: AWS::EC2::Instance
  Properties:
    ImageId: !Ref AmazonLinuxAMIID
    InstanceType: t3.micro
    SecurityGroupIds:
      - !Ref AppSecurityGroup
    SubnetId: !Ref PublicSubnet
    Tags:
      - Key: Name
        Value: App Server
```

---

## Resource Explanation

### ImageId

Uses the latest Amazon Linux AMI:

```yaml
ImageId: !Ref AmazonLinuxAMIID
```

### Instance Type

```yaml
InstanceType: t3.micro
```

### Security Group

```yaml
SecurityGroupIds:
  - !Ref AppSecurityGroup
```

### Subnet

```yaml
SubnetId: !Ref PublicSubnet
```

### Name Tag

```yaml
Tags:
  - Key: Name
    Value: App Server
```

---

## Update the Stack

Upload the modified template.

Expected preview:

```text
Add AWS::EC2::Instance
```

Choose:

```text
Update Stack
```

---

## Verify Deployment

Wait for:

```text
UPDATE_COMPLETE
```

Check Resources tab.

Expected resources:

* VPC
* Public Subnet
* Security Group
* S3 Bucket
* EC2 Instance

---

# Example Final Template Structure

```yaml
AWSTemplateFormatVersion: '2010-09-09'

Parameters:

  VPCCIDR:
    Type: String

  PublicSubnetCIDR:
    Type: String

  AmazonLinuxAMIID:
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2

Resources:

  VPC:
    Type: AWS::EC2::VPC

  PublicSubnet:
    Type: AWS::EC2::Subnet

  AppSecurityGroup:
    Type: AWS::EC2::SecurityGroup

  S3Bucket:
    Type: AWS::S3::Bucket

  AppServer:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: !Ref AmazonLinuxAMIID
      InstanceType: t3.micro
      SecurityGroupIds:
        - !Ref AppSecurityGroup
      SubnetId: !Ref PublicSubnet
      Tags:
        - Key: Name
          Value: App Server
```

---

# Troubleshooting

## Template Format Error

Incorrect indentation.

Correct:

```yaml
Resources:
  AppServer:
    Type: AWS::EC2::Instance
```

Incorrect:

```yaml
Resources:
AppServer:
Type: AWS::EC2::Instance
```

---

## Unresolved Resource Dependency

Verify resource names:

```yaml
!Ref PublicSubnet
!Ref AppSecurityGroup
!Ref AmazonLinuxAMIID
```

---

## CREATE_FAILED or UPDATE_FAILED

Navigate to:

```text
CloudFormation → Stack → Events
```

Review the failure message.

---

# Task 4: Delete the Stack

## Delete Resources

1. Open CloudFormation.
2. Select the Lab stack.
3. Choose **Delete**.
4. Confirm deletion.

CloudFormation automatically removes:

* VPC
* Subnet
* Security Groups
* EC2 Instance
* S3 Bucket
* Route Tables

Status:

```text
DELETE_IN_PROGRESS
```

Wait until the stack disappears.

---

# Lab Summary

In this lab you successfully:

* Created a CloudFormation stack.
* Created a VPC using Infrastructure as Code.
* Added an Amazon S3 bucket to an existing stack.
* Added an EC2 instance to an existing stack.
* Updated CloudFormation stacks.
* Deleted CloudFormation stacks and resources.
* Learned how to use YAML-based Infrastructure as Code on AWS.

---

# Key AWS Services Used

* AWS CloudFormation
* Amazon VPC
* Amazon EC2
* Amazon S3
* AWS Systems Manager Parameter Store
* AWS Security Groups

---

## Author

AWS CloudFormation Automation Lab Documentation

Infrastructure as Code (IaC) using AWS CloudFormation.
