# AWS CloudTrail

## Overview
AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. CloudTrail records AWS API calls and account activity and delivers log files for monitoring and analysis.

This lesson introduces the value and core features of AWS CloudTrail and how it helps organizations improve visibility, monitoring, and security across AWS environments.

---

# What You Will Learn

## At the Core of the Lesson
You will learn how to:

- Describe the value of AWS CloudTrail
- Highlight the features of AWS CloudTrail

---

# Introduction to AWS CloudTrail

AWS CloudTrail helps organizations track and monitor activity within AWS accounts. It records actions taken through:

- AWS Management Console
- AWS Command Line Interface (CLI)
- AWS SDKs
- AWS APIs

CloudTrail provides a history of account activity, allowing organizations to:

- Detect unusual activity
- Investigate security incidents
- Monitor compliance
- Troubleshoot operational issues
- Improve governance and auditing

---

# Value of AWS CloudTrail

AWS CloudTrail provides several important security and operational benefits.

## Security Monitoring
CloudTrail records actions performed by users, roles, and AWS services, making it easier to identify unauthorized or suspicious activity.

## Operational Troubleshooting
Administrators can review logs to determine:

- Who made changes
- What changes were made
- When the changes occurred

## Compliance and Auditing
CloudTrail supports compliance requirements by maintaining detailed logs of account activity.

## Visibility Across AWS Services
CloudTrail integrates with many AWS services to provide centralized monitoring and event tracking.

---

# Features of AWS CloudTrail

## Event History
CloudTrail provides access to recent account activity and management events directly in the AWS Management Console.

## API Activity Logging
CloudTrail logs API requests made to AWS services, including:

- Identity of the requester
- Time of request
- Source IP address
- Request parameters
- Response elements

## Multi-Region Tracking
CloudTrail can track activity across multiple AWS Regions.

## Log File Delivery
Logs can be delivered to Amazon S3 for long-term storage and analysis.

## Integration with Amazon CloudWatch
CloudTrail integrates with Amazon CloudWatch to enable:

- Monitoring
- Alerting
- Automated responses

## Security Analysis
CloudTrail logs can be analyzed using services such as:

- Amazon Athena
- AWS Security Hub
- Amazon GuardDuty

---

# Common Use Cases

## Detect Unauthorized Access
Monitor failed login attempts or suspicious API calls.

## Track Configuration Changes
Identify who modified AWS resources and when.

## Support Incident Response
Use logs during forensic investigations and security reviews.

## Maintain Compliance
Retain audit logs for regulatory and governance requirements.

---

# Summary

In this lesson, you learned how AWS CloudTrail helps organizations monitor, record, and analyze AWS account activity.

You also explored:

- The value of CloudTrail for security and auditing
- Key CloudTrail features
- How CloudTrail supports monitoring, compliance, and incident response