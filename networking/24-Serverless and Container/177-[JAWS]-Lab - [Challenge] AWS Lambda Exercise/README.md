# AWS Lambda Exercise (Challenge)

## Lab Overview

In this challenge lab, you will create an AWS Lambda function that automatically counts the number of words in a text file uploaded to an Amazon S3 bucket. The result will be sent via email using Amazon Simple Notification Service (Amazon SNS).

The solution demonstrates event-driven serverless architecture by integrating Amazon S3, AWS Lambda, and Amazon SNS.

---

## Objectives

After completing this lab, you will be able to:

- Create a Lambda function to count the number of words in a text file
- Configure an Amazon S3 bucket to invoke a Lambda function when a text file is uploaded
- Create an Amazon SNS topic to send the word count via email
- Test event-driven automation using AWS services
- Monitor Lambda execution using Amazon CloudWatch Logs

---

## Duration

**Estimated Time:** 90 Minutes

---

# Architecture

```text
Upload Text File to Amazon S3
              │
              ▼
        S3 Event Trigger
              │
              ▼
         AWS Lambda
              │
              ├── Read Text File
              ├── Count Words
              └── Publish Result
                      │
                      ▼
                 Amazon SNS
                      │
                      ▼
                    Email
```

---

# Business Requirement

When a text file is uploaded to an S3 bucket:

1. Amazon S3 automatically triggers a Lambda function.
2. Lambda reads the file contents.
3. Lambda counts the words in the file.
4. Lambda publishes the result to an SNS topic.
5. SNS sends an email notification.

The email message must use the following format:

```text
The word count in the <textFileName> file is nnn.
```

The email subject must be:

```text
Word Count Result
```

---

# AWS Services Used

| Service | Purpose |
|----------|----------|
| AWS Lambda | Serverless compute service |
| Amazon S3 | Stores uploaded text files |
| Amazon SNS | Sends email notifications |
| Amazon CloudWatch | Logging and monitoring |
| AWS IAM | Permissions management |

---

# IAM Role

Use the pre-created IAM role:

```text
LambdaAccessRole
```

This role includes the following permissions:

### AWSLambdaBasicExecutionRole

Provides permissions to:

- Create CloudWatch log groups
- Create CloudWatch log streams
- Write log events

### AmazonSNSFullAccess

Provides:

- Full access to Amazon SNS

### AmazonS3FullAccess

Provides:

- Full access to Amazon S3 buckets

### CloudWatchFullAccess

Provides:

- Full access to Amazon CloudWatch

---

# Task 1: Create an Amazon SNS Topic

## Create Topic

Navigate to:

```text
Amazon SNS → Topics → Create Topic
```

Configure:

| Setting | Value |
|----------|----------|
| Type | Standard |
| Name | WordCountTopic |

Choose:

```text
Create Topic
```

---

## Create Subscription

Open the topic and choose:

```text
Create Subscription
```

Configure:

| Setting | Value |
|----------|----------|
| Protocol | Email |
| Endpoint | Your Email Address |

Choose:

```text
Create Subscription
```

---

## Confirm Subscription

1. Open your email inbox.
2. Locate the Amazon SNS confirmation email.
3. Choose **Confirm Subscription**.

The subscription status should change to:

```text
Confirmed
```

---

# Task 2: Create an Amazon S3 Bucket

Navigate to:

```text
Amazon S3 → Create Bucket
```

Example bucket name:

```text
word-count-bucket-yourname
```

Keep default settings and create the bucket.

---

# Task 3: Create the Lambda Function

Navigate to:

```text
AWS Lambda → Create Function
```

Configure:

| Setting | Value |
|----------|----------|
| Function Name | WordCountFunction |
| Runtime | Python 3.9 |
| Execution Role | Use Existing Role |
| Existing Role | LambdaAccessRole |

Choose:

```text
Create Function
```

---

# Task 4: Develop Lambda Code

Replace the default Lambda code with:

```python
import boto3
import urllib.parse

sns = boto3.client('sns')

TOPIC_ARN = "YOUR_SNS_TOPIC_ARN"

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(
        event['Records'][0]['s3']['object']['key']
    )

    s3 = boto3.client('s3')

    response = s3.get_object(
        Bucket=bucket,
        Key=key
    )

    text = response['Body'].read().decode('utf-8')

    word_count = len(text.split())

    message = (
        f"The word count in the {key} file "
        f"is {word_count}."
    )

    sns.publish(
        TopicArn=TOPIC_ARN,
        Subject="Word Count Result",
        Message=message
    )

    return {
        "statusCode": 200,
        "body": message
    }
```

---

# Task 5: Configure SNS Topic ARN

Copy the ARN of your SNS topic.

Example:

```text
arn:aws:sns:us-west-2:123456789012:WordCountTopic
```

Replace:

```python
TOPIC_ARN = "YOUR_SNS_TOPIC_ARN"
```

with the actual ARN.

---

# Task 6: Deploy the Function

Choose:

```text
Deploy
```

to save and publish the Lambda function.

---

# Task 7: Configure S3 Event Trigger

Inside the Lambda function:

```text
Add Trigger
```

Select:

```text
S3
```

Configure:

| Setting | Value |
|----------|----------|
| Bucket | Your S3 Bucket |
| Event Type | PUT |
| Suffix | .txt |

Enable recursive invocation acknowledgment and choose:

```text
Add
```

---

# Task 8: Test the Solution

Create a text file:

### sample1.txt

```text
AWS Lambda makes serverless computing easy.
```

Upload the file to the S3 bucket.

---

## Expected Result

Lambda executes automatically.

An email is sent with:

### Subject

```text
Word Count Result
```

### Message

```text
The word count in the sample1.txt file is 6.
```

---

# Additional Test Files

## sample2.txt

Contents:

```text
Hello World
```

Expected Result:

```text
The word count in the sample2.txt file is 2.
```

---

## sample3.txt

Contents:

```text
Amazon Web Services provides many cloud services.
```

Expected Result:

```text
The word count in the sample3.txt file is 7.
```

---

# Monitoring

Navigate to:

```text
CloudWatch → Log Groups
```

Locate:

```text
/aws/lambda/WordCountFunction
```

Review logs for:

- Successful executions
- Errors
- Invocation details

---

# Troubleshooting

## No Email Received

Verify:

- SNS subscription is confirmed
- Topic ARN is correct
- Lambda executed successfully

---

## Lambda Not Triggering

Verify:

- S3 trigger is configured
- File extension is `.txt`
- File uploaded to the correct bucket

---

## Access Denied Errors

Verify:

```text
LambdaAccessRole
```

is attached to the Lambda function.

---

# Validation Checklist

- [ ] SNS Topic Created
- [ ] Email Subscription Confirmed
- [ ] S3 Bucket Created
- [ ] Lambda Function Created
- [ ] LambdaAccessRole Assigned
- [ ] Lambda Code Deployed
- [ ] SNS ARN Configured
- [ ] S3 Trigger Added
- [ ] Text File Uploaded
- [ ] Email Notification Received
- [ ] Lambda Logs Verified

---

# Conclusion

In this challenge lab, you successfully:

- Created an AWS Lambda function to count words in text files
- Configured Amazon S3 to automatically invoke Lambda
- Created an Amazon SNS topic and email subscription
- Implemented event-driven serverless processing
- Used CloudWatch Logs for monitoring and troubleshooting

This solution demonstrates a practical serverless architecture using AWS Lambda, Amazon S3, and Amazon SNS.