# AWS re/Start Challenge Lab – Using AWS CloudFormation to Create a VPC and Amazon EC2 Instance

## Lab Overview

This challenge lab focuses on creating AWS infrastructure using AWS CloudFormation.

The goal is to build a CloudFormation template that automatically deploys:

- Amazon Virtual Private Cloud (VPC)
- Internet Gateway attached to the VPC
- Security Group allowing SSH access from anywhere
- Private Subnet inside the VPC
- Amazon EC2 t3.micro instance inside the private subnet

> **Note:** The EC2 instance does not need to be accessible via SSH for a successful solution. The requirement is that it launches successfully within the private subnet.

---

## Objectives

By completing this lab, you will learn how to:

- Create infrastructure as code using AWS CloudFormation
- Define AWS resources in YAML format
- Deploy a VPC and networking resources
- Create Security Groups
- Launch an EC2 instance through CloudFormation
- Validate CloudFormation stack deployments
- Troubleshoot CloudFormation stack failures

---

## Architecture

```text
+--------------------------------------------------+
|                    Lab VPC                       |
|                 10.0.0.0/16                      |
|                                                  |
|  +--------------------------------------------+  |
|  | Private Subnet                             |  |
|  | 10.0.1.0/24                                |  |
|  |                                            |  |
|  |   EC2 Instance (t3.micro)                  |  |
|  |                                            |  |
|  +--------------------------------------------+  |
|                                                  |
|     Security Group (SSH from 0.0.0.0/0)         |
|                                                  |
+----------------------+---------------------------+
                       |
                       |
                Internet Gateway
```

---

# CloudFormation Template

Create a file named:

```bash
challenge-template.yaml
```

Paste the following template into the file:

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: AWS re/Start Challenge - VPC and EC2 Instance

Resources:

  LabVPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: true
      EnableDnsHostnames: true
      Tags:
        - Key: Name
          Value: LabVPC

  InternetGateway:
    Type: AWS::EC2::InternetGateway
    Properties:
      Tags:
        - Key: Name
          Value: LabIGW

  AttachGateway:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId: !Ref LabVPC
      InternetGatewayId: !Ref InternetGateway

  PrivateSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref LabVPC
      CidrBlock: 10.0.1.0/24
      MapPublicIpOnLaunch: false
      Tags:
        - Key: Name
          Value: PrivateSubnet

  InstanceSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Allow SSH Access
      VpcId: !Ref LabVPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: 0.0.0.0/0
      Tags:
        - Key: Name
          Value: SSH-SG

  EC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t3.micro
      ImageId: !Sub "{{resolve:ssm:/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2}}"
      SubnetId: !Ref PrivateSubnet
      SecurityGroupIds:
        - !Ref InstanceSecurityGroup
      Tags:
        - Key: Name
          Value: PrivateEC2

Outputs:

  VPCId:
    Description: VPC ID
    Value: !Ref LabVPC

  SubnetId:
    Description: Private Subnet ID
    Value: !Ref PrivateSubnet

  InstanceId:
    Description: EC2 Instance ID
    Value: !Ref EC2Instance
```

---

# Deploy the Stack

Run:

```bash
aws cloudformation create-stack \
--stack-name RestartChallenge \
--template-body file://challenge-template.yaml
```

---

# Monitor Deployment

Check stack status:

```bash
aws cloudformation describe-stacks \
--stack-name RestartChallenge
```

View stack events:

```bash
aws cloudformation describe-stack-events \
--stack-name RestartChallenge
```

---

# Verify Resources

## Verify VPC

```bash
aws ec2 describe-vpcs \
--filters Name=tag:Name,Values=LabVPC
```

---

## Verify Subnet

```bash
aws ec2 describe-subnets \
--filters Name=tag:Name,Values=PrivateSubnet
```

---

## Verify Security Group

```bash
aws ec2 describe-security-groups \
--filters Name=group-name,Values=SSH-SG
```

---

## Verify EC2 Instance

```bash
aws ec2 describe-instances \
--filters Name=tag:Name,Values=PrivateEC2
```

---

# Expected Resources

| Resource Name | Resource Type |
|--------------|---------------|
| LabVPC | AWS::EC2::VPC |
| InternetGateway | AWS::EC2::InternetGateway |
| AttachGateway | AWS::EC2::VPCGatewayAttachment |
| PrivateSubnet | AWS::EC2::Subnet |
| InstanceSecurityGroup | AWS::EC2::SecurityGroup |
| EC2Instance | AWS::EC2::Instance |

---

# Troubleshooting

## View Stack Errors

```bash
aws cloudformation describe-stack-events \
--stack-name RestartChallenge
```

Look for:

```text
CREATE_FAILED
```

Review the `ResourceStatusReason` field for details.

---

## Check Latest Amazon Linux AMI

```bash
aws ssm get-parameters \
--names /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
```

---

## Check Available Instance Types

```bash
aws ec2 describe-instance-type-offerings \
--location-type region
```

---

## Validate Template Before Deployment

```bash
aws cloudformation validate-template \
--template-body file://challenge-template.yaml
```

Expected output:

```json
{
  "Description": "AWS re/Start Challenge - VPC and EC2 Instance"
}
```

---

# Common CloudFormation Commands

## List Stacks

```bash
aws cloudformation list-stacks
```

## Describe a Stack

```bash
aws cloudformation describe-stacks \
--stack-name RestartChallenge
```

## View Resources in a Stack

```bash
aws cloudformation describe-stack-resources \
--stack-name RestartChallenge
```

## Delete a Stack

```bash
aws cloudformation delete-stack \
--stack-name RestartChallenge
```

---

# JMESPath Queries

## Get Only EC2 LogicalResourceId

Example JSON:

```json
{
  "StackResources": [
    {
      "LogicalResourceId": "VPC",
      "ResourceType": "AWS::EC2::VPC"
    },
    {
      "LogicalResourceId": "PublicSubnet1",
      "ResourceType": "AWS::EC2::Subnet"
    },
    {
      "LogicalResourceId": "CliHostInstance",
      "ResourceType": "AWS::EC2::Instance"
    }
  ]
}
```

JMESPath Query:

```text
StackResources[?ResourceType=='AWS::EC2::Instance'].LogicalResourceId
```

Output:

```json
[
  "CliHostInstance"
]
```

---

# CloudFormation Challenge Solution (Keep S3 Bucket While Deleting Stack)

## Step 1 – Find the Bucket Logical ID

```bash
aws cloudformation describe-stack-resources \
--stack-name myStack
```

JMESPath version:

```bash
aws cloudformation describe-stack-resources \
--stack-name myStack \
--query "StackResources[?ResourceType=='AWS::S3::Bucket'].LogicalResourceId"
```

Output:

```json
[
  "MyBucket"
]
```

---

## Step 2 – Delete Stack but Retain Bucket

```bash
aws cloudformation delete-stack \
--stack-name myStack \
--retain-resources MyBucket
```

This:

- Deletes the stack
- Deletes all other resources
- Keeps the S3 bucket
- Keeps all objects stored in the bucket

---

## Step 3 – Verify Stack Deletion

```bash
aws cloudformation describe-stacks \
--stack-name myStack
```

Expected result:

```text
Stack with id myStack does not exist
```

---

## Step 4 – Verify Bucket Still Exists

```bash
aws s3 ls
```

Verify bucket contents:

```bash
aws s3 ls s3://YOUR-BUCKET-NAME
```

The uploaded file should still be present.

---

# Success Criteria

The challenge is successfully completed when:

- ✅ CloudFormation template validates successfully
- ✅ VPC is created
- ✅ Internet Gateway is attached
- ✅ Security Group allows SSH
- ✅ Private Subnet is created
- ✅ EC2 t3.micro launches successfully
- ✅ CloudFormation Stack reaches `CREATE_COMPLETE`
- ✅ Resources can be viewed in AWS Console
- ✅ Stack can be deleted successfully
- ✅ S3 Bucket can be retained during stack deletion when required

---

# Key AWS Services Used

- AWS CloudFormation
- Amazon VPC
- Amazon EC2
- Amazon S3
- AWS Systems Manager Parameter Store
- Security Groups
- Internet Gateway
- AWS CLI
- JMESPath

---

# Author

AWS re/Start CloudFormation Challenge Lab Documentation