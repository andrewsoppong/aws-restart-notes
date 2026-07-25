# Working with AWS Lambda

## Lab Overview

In this lab, you deploy and configure an AWS Lambda serverless solution that generates a sales analysis report from a MySQL database and emails the results to an administrator.

The solution uses:

- AWS Lambda
- Amazon SNS
- AWS Systems Manager Parameter Store
- Amazon EC2 (LAMP Stack)
- Amazon CloudWatch
- AWS IAM

The database connection information is stored in Systems Manager Parameter Store, while the database itself runs on an EC2 LAMP instance.

---

## Architecture

### Workflow

1. A CloudWatch scheduled event triggers the `salesAnalysisReport` Lambda function.
2. `salesAnalysisReport` invokes the `salesAnalysisReportDataExtractor` Lambda function.
3. `salesAnalysisReportDataExtractor` queries the `cafe_db` database.
4. Query results are returned to `salesAnalysisReport`.
5. The report is formatted and published to an SNS topic.
6. Amazon SNS sends the report via email to the administrator.

---

## Objectives

After completing this lab, you will be able to:

- Recognize IAM permissions required for Lambda functions
- Create a Lambda Layer for external dependencies
- Create Lambda functions that extract data and generate reports
- Configure Lambda functions to invoke other Lambda functions
- Deploy and test scheduled serverless workloads
- Use CloudWatch Logs for troubleshooting
- Configure Amazon SNS notifications

---

## Duration

**Estimated Time:** 60 Minutes

---

# Task 1: Observe IAM Role Settings

## salesAnalysisReportRole

### Trusted Entity

- `lambda.amazonaws.com`

### Attached Policies

| Policy | Purpose |
|----------|----------|
| AmazonSNSFullAccess | Full access to SNS |
| AmazonSSMReadOnlyAccess | Read access to Parameter Store |
| AWSLambdaBasicRunRole | Write logs to CloudWatch |
| AWSLambdaRole | Invoke other Lambda functions |

---

## salesAnalysisReportDERole

### Trusted Entity

- `lambda.amazonaws.com`

### Attached Policies

| Policy | Purpose |
|----------|----------|
| AWSLambdaBasicRunRole | CloudWatch logging |
| AWSLambdaVPCAccessRunRole | VPC networking permissions |

---

# Task 2: Create a Lambda Layer and Data Extractor Function

## Download Required Files

- `pymysql-v3.zip`
- `salesAnalysisReportDataExtractor-v3.zip`

---

## Create Lambda Layer

### Configuration

| Setting | Value |
|-----------|---------|
| Name | pymysqlLibrary |
| Description | PyMySQL library modules |
| Runtime | Python 3.9 |
| Package | pymysql-v3.zip |

### Purpose

Provides the PyMySQL dependency without packaging it inside every Lambda deployment package.

---

## Create Lambda Function

### Function Details

| Setting | Value |
|-----------|---------|
| Function Name | salesAnalysisReportDataExtractor |
| Runtime | Python 3.9 |
| Execution Role | salesAnalysisReportDERole |

---

## Attach Lambda Layer

### Layer Configuration

| Setting | Value |
|-----------|---------|
| Layer Type | Custom Layer |
| Layer | pymysqlLibrary |
| Version | 1 |

---

## Upload Function Code

### Runtime Settings

| Setting | Value |
|-----------|---------|
| Handler | salesAnalysisReportDataExtractor.lambda_handler |

### Upload Package

- Upload `salesAnalysisReportDataExtractor-v3.zip`

---

## Configure Networking

### VPC Settings

| Setting | Value |
|-----------|---------|
| VPC | Cafe VPC |
| Subnet | Cafe Public Subnet 1 |
| Security Group | CafeSecurityGroup |

The Lambda function requires network access to the MySQL database running on the EC2 instance.

---

# Task 3: Test the Data Extractor Function

## Retrieve Database Parameters

From Systems Manager Parameter Store:

- `/cafe/dbUrl`
- `/cafe/dbName`
- `/cafe/dbUser`
- `/cafe/dbPassword`

---

## Create Test Event

```json
{
  "dbUrl": "<dbUrl>",
  "dbName": "<dbName>",
  "dbUser": "<dbUser>",
  "dbPassword": "<dbPassword>"
}
```

---

## Initial Test Result

Expected failure:

```json
{
  "errorMessage": "Task timed out after 3.00 seconds"
}
```

### Cause

The Lambda function cannot connect to the database.

---

## Troubleshooting

Verify that the database security group allows inbound access on:

```text
TCP 3306
```

MySQL uses port **3306** for client connections.

---

## Successful Test Result

```json
{
  "statusCode": 200,
  "body": []
}
```

The query executes successfully but returns no data because no orders exist.

---

## Populate Database

### Open Café Website

```text
http://<Public-IP>/cafe
```

Find the public IP from:

- EC2 Console → CafeInstance
- Lab Details → CafePublicIP

---

## Create Sample Orders

Place orders through the café application to generate sales data.

---

## Test Again

Expected output:

```json
{
  "statusCode": 200,
  "body": [
    {
      "product_group_number": 1,
      "product_group_name": "Pastries",
      "product_id": 1,
      "product_name": "Croissant",
      "quantity": 1
    },
    {
      "product_group_number": 2,
      "product_group_name": "Drinks",
      "product_id": 8,
      "product_name": "Hot Chocolate",
      "quantity": 2
    }
  ]
}
```

---

# Task 4: Configure Notifications

## Create SNS Topic

Navigate to:

```text
Amazon SNS → Topics → Create Topic
```

### Configuration

| Setting | Value |
|-----------|---------|
| Type | Standard |
| Topic Name | salesAnalysisReportTopic |

---

## Subscribe Email Address

1. Create an Email subscription.
2. Enter your email address.
3. Confirm the subscription from the confirmation email.

---

## Purpose

The Lambda reporting function publishes messages to this topic.

Amazon SNS then delivers the sales report to all subscribed recipients.

---

# Key AWS Services Used

| Service | Purpose |
|-----------|----------|
| AWS Lambda | Serverless compute |
| Amazon SNS | Email notifications |
| Systems Manager Parameter Store | Secure configuration storage |
| Amazon EC2 | Hosts MySQL database |
| CloudWatch | Scheduling and logging |
| IAM | Access control |
| Lambda Layers | Dependency management |

---

# Skills Demonstrated

- Serverless application deployment
- Lambda Layer creation
- IAM role analysis
- VPC-enabled Lambda configuration
- Database connectivity troubleshooting
- SNS notification setup
- CloudWatch logging and monitoring
- Lambda-to-Lambda invocation

---

# Lab Outcome

Successfully:

- Created a reusable Lambda Layer
- Deployed a database-integrated Lambda function
- Configured VPC networking for Lambda
- Troubleshot database connectivity issues
- Queried data from a MySQL database
- Created SNS email notifications
- Built a serverless reporting workflow using AWS Lambda