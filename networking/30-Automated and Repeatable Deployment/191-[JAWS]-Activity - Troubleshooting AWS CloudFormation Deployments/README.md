# Activity: Troubleshoot CloudFormation

## Overview

This activity provides hands-on experience troubleshooting AWS CloudFormation deployments using the AWS Command Line Interface (AWS CLI), JMESPath queries, drift detection, and stack deletion troubleshooting.

You will:

* Practice querying JSON data using JMESPath.
* Troubleshoot CloudFormation deployment failures.
* Analyze EC2 log files to identify root causes.
* Detect CloudFormation stack drift.
* Resolve stack deletion failures.
* Learn how to preserve resources while deleting CloudFormation stacks.

---

# Architecture

The activity deploys:

* Amazon VPC
* Public Subnet
* EC2 Web Server
* Security Group
* Amazon S3 Bucket
* CloudFormation WaitCondition and WaitHandle

The stack is deployed and managed through AWS CloudFormation.

---

# Learning Objectives

After completing this activity, you will be able to:

* Use JMESPath expressions to query JSON documents.
* Deploy CloudFormation stacks using AWS CLI.
* Troubleshoot CloudFormation stack failures.
* Analyze EC2 cloud-init logs.
* Detect configuration drift.
* Resolve CloudFormation stack deletion issues.
* Preserve resources during stack deletion.

---

# Duration

**75 Minutes**

---

# Task 1: Practice Querying JSON Using JMESPath

## Sample JSON

```json
{
  "desserts": [
    {
      "name": "Chocolate cake",
      "price": "20.00"
    },
    {
      "name": "Ice cream",
      "price": "15.00"
    },
    {
      "name": "Carrot cake",
      "price": "22.00"
    }
  ]
}
```

## Query Examples

### Return Entire Array

```jmespath
desserts
```

### Return Second Element

```jmespath
desserts[1]
```

### Return Name of First Dessert

```jmespath
desserts[0].name
```

### Return Name and Price

```jmespath
desserts[0].[name,price]
```

### Return All Dessert Names

```jmespath
desserts[].name
```

### Filter by Name

```jmespath
desserts[?name=='Carrot cake']
```

---

## CloudFormation Example

JSON:

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

Query:

```jmespath
StackResources[?ResourceType=='AWS::EC2::Instance'].LogicalResourceId
```

Output:

```text
CliHostInstance
```

---

# Task 2: Troubleshoot CloudFormation Stacks

## Connect to CLI Host

### Linux/macOS

Navigate to the directory containing the PEM key:

```bash
cd ~/Downloads
```

Set permissions:

```bash
chmod 400 labsuser.pem
```

Connect:

```bash
ssh -i labsuser.pem ec2-user@<PUBLIC-IP>
```

---

## Configure AWS CLI

Determine Region:

```bash
curl http://169.254.169.254/latest/dynamic/instance-identity/document | grep region
```

Configure AWS CLI:

```bash
aws configure
```

Provide:

```text
Access Key ID
Secret Access Key
Region
json
```

---

## View CloudFormation Template

```bash
less template1.yaml
```

Exit:

```bash
q
```

---

## Create Stack

```bash
aws cloudformation create-stack \
--stack-name myStack \
--template-body file://template1.yaml \
--capabilities CAPABILITY_NAMED_IAM \
--parameters ParameterKey=KeyName,ParameterValue=vockey
```

---

## Monitor Resource Creation

```bash
watch -n 5 -d \
aws cloudformation describe-stack-resources \
--stack-name myStack \
--query 'StackResources[*].[ResourceType,ResourceStatus]' \
--output table
```

---

## Monitor Stack Status

```bash
watch -n 5 -d \
aws cloudformation describe-stacks \
--stack-name myStack \
--output table
```

---

## Investigate Failure

Display failed events:

```bash
aws cloudformation describe-stack-events \
--stack-name myStack \
--query "StackEvents[?ResourceStatus=='CREATE_FAILED']"
```

Expected result:

```text
WaitCondition timed out
```

---

## Delete Failed Stack

```bash
aws cloudformation delete-stack \
--stack-name myStack
```

---

# Task 2.4: Disable Rollback

Create stack again:

```bash
aws cloudformation create-stack \
--stack-name myStack \
--template-body file://template1.yaml \
--capabilities CAPABILITY_NAMED_IAM \
--on-failure DO_NOTHING \
--parameters ParameterKey=KeyName,ParameterValue=vockey
```

This preserves resources after failure.

---

## Find Web Server IP

```bash
aws ec2 describe-instances \
--filters "Name=tag:Name,Values='Web Server'" \
--query 'Reservations[].Instances[].[State.Name,PublicIpAddress]'
```

---

## Analyze Cloud-Init Logs

SSH into the instance and run:

```bash
tail -50 /var/log/cloud-init-output.log
```

Error observed:

```text
No package http available
```

---

## Inspect User Data Script

```bash
sudo cat /var/lib/cloud/instance/scripts/part-001
```

Problem:

```bash
yum install -y http
```

Correct package:

```bash
yum install -y httpd
```

---

# Task 2.5: Fix the Template

Edit file:

```bash
vim template1.yaml
```

Locate:

```bash
yum install -y http
```

Replace with:

```bash
yum install -y httpd
```

Save:

```bash
:wq
```

Verify:

```bash
cat template1.yaml | grep httpd
```

---

## Delete Failed Stack

```bash
aws cloudformation delete-stack \
--stack-name myStack
```

Wait until deleted.

---

## Recreate Stack

```bash
aws cloudformation create-stack \
--stack-name myStack \
--template-body file://template1.yaml \
--capabilities CAPABILITY_NAMED_IAM \
--on-failure DO_NOTHING \
--parameters ParameterKey=KeyName,ParameterValue=vockey
```

Monitor:

```bash
watch -n 5 -d \
aws cloudformation describe-stack-resources \
--stack-name myStack \
--query 'StackResources[*].[ResourceType,ResourceStatus]' \
--output table
```

Expected status:

```text
CREATE_COMPLETE
```

---

## Test Web Server

Retrieve output:

```bash
aws cloudformation describe-stacks \
--stack-name myStack \
--output table
```

Open:

```text
http://<PUBLIC-IP>
```

Expected:

```text
Hello from your web server!
```

---

# Task 3: Detect Drift

## Modify Security Group

Navigate:

```text
EC2 → Instances → Web Server
```

Open:

```text
Security Tab → WebServerSG
```

Edit inbound rule:

```text
SSH Source:
0.0.0.0/0
```

Change to:

```text
My IP
```

Save.

---

## Add File to Bucket

Retrieve bucket name:

```bash
bucketName=$(aws cloudformation describe-stacks \
--stack-name myStack \
--query "Stacks[*].Outputs[?OutputKey=='BucketName'].[OutputValue]" \
--output text)

echo $bucketName
```

Create file:

```bash
touch myfile
```

Upload:

```bash
aws s3 cp myfile s3://$bucketName/
```

Verify:

```bash
aws s3 ls s3://$bucketName/
```

---

## Start Drift Detection

```bash
aws cloudformation detect-stack-drift \
--stack-name myStack
```

Copy:

```text
StackDriftDetectionId
```

---

## Check Drift Status

```bash
aws cloudformation describe-stack-drift-detection-status \
--stack-drift-detection-id <DRIFT-ID>
```

Expected:

```text
DRIFTED
```

---

## View Drift Summary

```bash
aws cloudformation describe-stack-resources \
--stack-name myStack \
--query 'StackResources[*].[ResourceType,ResourceStatus,DriftInformation.StackResourceDriftStatus]' \
--output table
```

Expected:

```text
MODIFIED
```

for the security group.

---

## Detailed Drift Information

```bash
aws cloudformation describe-stack-resource-drifts \
--stack-name myStack \
--stack-resource-drift-status-filters MODIFIED
```

Review:

```text
PropertyDifferences
```

---

# Task 4: Delete Stack

Delete:

```bash
aws cloudformation delete-stack \
--stack-name myStack
```

Monitor:

```bash
watch -n 5 -d \
aws cloudformation describe-stack-resources \
--stack-name myStack \
--query 'StackResources[*].[ResourceType,ResourceStatus]' \
--output table
```

Result:

```text
DELETE_FAILED
```

Reason:

```text
S3 Bucket contains objects
```

CloudFormation cannot delete non-empty buckets.

---

# Challenge Solution: Keep Bucket and Delete Stack

## Step 1: Find Logical Resource ID

```bash
aws cloudformation describe-stack-resources \
--stack-name myStack
```

Find:

```text
MyBucket
```

Optional query:

```bash
aws cloudformation describe-stack-resources \
--stack-name myStack \
--query "StackResources[?ResourceType=='AWS::S3::Bucket'].LogicalResourceId"
```

---

## Step 2: Delete Stack but Retain Bucket

```bash
aws cloudformation delete-stack \
--stack-name myStack \
--retain-resources MyBucket
```

CloudFormation will:

* Delete all other resources.
* Keep the S3 bucket.
* Keep all files in the bucket.

---

## Verify

Check stack:

```bash
aws cloudformation describe-stacks \
--stack-name myStack
```

Eventually:

```text
Stack does not exist
```

The bucket remains available.

---

# Key Commands Reference

## Create Stack

```bash
aws cloudformation create-stack
```

## Update Stack

```bash
aws cloudformation update-stack
```

## Delete Stack

```bash
aws cloudformation delete-stack
```

## Detect Drift

```bash
aws cloudformation detect-stack-drift
```

## Describe Drift

```bash
aws cloudformation describe-stack-resource-drifts
```

## Describe Resources

```bash
aws cloudformation describe-stack-resources
```

## Describe Events

```bash
aws cloudformation describe-stack-events
```

---

# Conclusion

In this activity, you:

* Practiced JMESPath queries.
* Troubleshot CloudFormation deployment failures.
* Investigated EC2 cloud-init logs.
* Corrected CloudFormation templates.
* Successfully deployed infrastructure.
* Detected and analyzed stack drift.
* Resolved stack deletion failures.
* Learned how to retain resources during stack deletion.

These skills are essential for managing Infrastructure as Code (IaC) environments using AWS CloudFormation.
