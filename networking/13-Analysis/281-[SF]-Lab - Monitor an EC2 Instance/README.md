# Monitor an EC2 Instance

## Lab Overview

Logging and monitoring are techniques implemented to achieve a common goal. They work together to help ensure that a system's performance baselines and security guidelines are always met.

### Logging
Logging refers to recording and storing data events as log files. Logs contain low-level details that can give visibility into how applications or systems perform under certain circumstances. From a security standpoint, logging helps administrators identify suspicious activity and security threats.

### Monitoring
Monitoring is the process of analyzing and collecting data to help ensure optimal system performance and security. Monitoring helps detect unauthorized access and ensures services comply with organizational security requirements.

In this lab, you create an Amazon CloudWatch alarm that activates when an Amazon Elastic Compute Cloud (Amazon EC2) instance exceeds a specific CPU utilization threshold. You also configure Amazon Simple Notification Service (Amazon SNS) to send an email notification when the alarm is triggered.

You then log into the EC2 instance and run a stress test that simulates a malicious actor causing CPU utilization to spike to 100%.

---

# Objectives

After completing this lab, you should be able to:

- Create an Amazon SNS notification
- Configure a CloudWatch alarm
- Stress test an EC2 instance
- Confirm that an Amazon SNS email was sent
- Create a CloudWatch dashboard

---

# Duration

This lab requires approximately **60 minutes** to complete.

---

# Lab Environment

The lab environment includes:

- One preconfigured EC2 instance named **Stress Test**
- An attached IAM role
- AWS Systems Manager Session Manager access

Backend components such as Amazon EC2, IAM roles, and AWS services are already configured.

---

# Accessing the AWS Management Console

1. Choose **Start Lab**
2. Wait for the lab status indicator to turn green
3. Choose the green AWS icon to open the AWS Management Console
4. If prompted, switch to the new console experience
5. Arrange the instructions and console side-by-side

> Do not change the AWS Region unless instructed.

---

# Task 1: Configure Amazon SNS

## Overview

Amazon SNS is a fully managed messaging service for application-to-application (A2A) and application-to-person (A2P) communication.

In this task, you create:

- An SNS topic
- An email subscription

---

## Create an SNS Topic

1. Open the AWS Management Console
2. Search for **SNS**
3. Choose **Simple Notification Service**
4. In the left navigation pane, choose **Topics**
5. Choose **Create topic**

### Configure Topic

| Setting | Value |
|---|---|
| Type | Standard |
| Name | MyCwAlarm |

6. Choose **Create topic**

---

## Create an SNS Subscription

1. Open the **Subscriptions** tab
2. Choose **Create subscription**

### Configure Subscription

| Setting | Value |
|---|---|
| Topic ARN | Default |
| Protocol | Email |
| Endpoint | Your email address |

3. Choose **Create subscription**

---

## Confirm the Subscription

1. Open the confirmation email from AWS Notifications
2. Choose **Confirm subscription**
3. Return to the AWS Console
4. Verify the subscription status shows **Confirmed**

---

# Task 1 Summary

In this task, you:

- Created an SNS topic
- Created an email subscription
- Confirmed the subscription

The SNS topic can now send notifications to your email address.

---

# Task 2: Create a CloudWatch Alarm

## Overview

Amazon CloudWatch is a monitoring and observability service that provides metrics, logs, and alarms for AWS resources.

In this task, you:

- View EC2 metrics
- Create a CloudWatch alarm
- Configure SNS notifications

---

## View EC2 Metrics

1. Search for **CloudWatch**
2. Open **CloudWatch**
3. In the left navigation pane, choose:

```text
Metrics → All metrics
```

4. Choose:

```text
EC2 → Per-Instance Metrics
```

5. Select the metric:

```text
CPUUtilization
```

for the **Stress Test** instance.

---

## Create a CloudWatch Alarm

1. In the left navigation pane, choose:

```text
Alarms → All alarms
```

2. Choose **Create alarm**
3. Choose **Select metric**
4. Navigate to:

```text
EC2 → Per-Instance Metrics
```

5. Select:

```text
CPUUtilization
```

for the Stress Test instance.

6. Choose **Select metric**

---

## Configure Alarm Conditions

### Metric Settings

| Setting | Value |
|---|---|
| Metric name | CPUUtilization |
| Statistic | Average |
| Period | 1 minute |

### Conditions

| Setting | Value |
|---|---|
| Threshold type | Static |
| Condition | Greater than |
| Threshold value | 60 |

7. Choose **Next**

---

## Configure SNS Notifications

### Notification Settings

| Setting | Value |
|---|---|
| Alarm state trigger | In alarm |
| SNS topic | MyCwAlarm |

8. Choose **Next**

---

## Configure Alarm Details

| Setting | Value |
|---|---|
| Alarm name | LabCPUUtilizationAlarm |
| Description | CloudWatch alarm for Stress Test EC2 instance CPUUtilization |

9. Choose **Next**
10. Review the settings
11. Choose **Create alarm**

---

# Task 2 Summary

In this task, you:

- Viewed EC2 metrics in CloudWatch
- Created a CloudWatch alarm
- Configured SNS notifications
- Set a CPU threshold of 60%

---

# Task 3: Test the CloudWatch Alarm

## Overview

In this task, you:

- Connect to the EC2 instance
- Run a CPU stress test
- Trigger the CloudWatch alarm
- Confirm SNS email delivery

---

## Connect to the EC2 Instance

1. Open the Vocareum console
2. Choose **AWS Details**
3. Copy the URL next to:

```text
EC2InstanceURL
```

4. Open the link in a new browser tab

---

## Run the Stress Test

Execute the following command:

```bash
sudo stress --cpu 10 -v --timeout 400s
```

### What This Command Does

- Loads CPU utilization to 100%
- Runs for 400 seconds
- Simulates abnormal resource usage

---

## Monitor CPU Usage

Open a second Session Manager terminal and run:

```bash
top
```

This displays live CPU usage.

---

## Monitor the CloudWatch Alarm

1. Return to CloudWatch
2. Open:

```text
LabCPUUtilizationAlarm
```

3. Refresh the graph every minute
4. Wait for the alarm state to change to:

```text
In alarm
```

---

## Verify Email Notification

Check your email inbox for an AWS Notifications message confirming the alarm activation.

---

# Task 3 Summary

In this task, you:

- Stress tested the EC2 instance
- Increased CPU utilization to 100%
- Triggered the CloudWatch alarm
- Received an SNS email notification

---

# Task 4: Create a CloudWatch Dashboard

## Overview

CloudWatch dashboards provide customizable views of metrics and alarms across AWS resources.

---

## Create a Dashboard

1. In CloudWatch, choose:

```text
Dashboards
```

2. Choose **Create dashboard**

### Dashboard Configuration

| Setting | Value |
|---|---|
| Dashboard name | LabEC2Dashboard |

3. Choose **Create dashboard**

---

## Add a Widget

1. Choose:

```text
Line
```

2. Choose:

```text
Metrics
```

3. Navigate to:

```text
EC2 → Per-Instance Metrics
```

4. Select:

```text
Stress Test → CPUUtilization
```

5. Choose **Create widget**
6. Choose **Save dashboard**

---

# Task 4 Summary

In this task, you:

- Created a CloudWatch dashboard
- Added a CPUUtilization metric widget
- Created a quick monitoring view for the EC2 instance

---

# Lab Summary

In this lab, you:

- Created an Amazon SNS notification
- Configured a CloudWatch alarm
- Stress tested an EC2 instance
- Confirmed SNS email delivery
- Created a CloudWatch dashboard

This lab demonstrated how monitoring and alerting help detect unusual resource activity such as CPU spikes, which may indicate malware or malicious activity.

---

# AWS Services Used

## Amazon CloudWatch

Used for:
- Metrics
- Monitoring
- Dashboards
- Alarms

## Amazon SNS

Used for:
- Notifications
- Email alerts

## Amazon EC2

Used for:
- Hosting the Stress Test instance

## AWS Systems Manager Session Manager

Used for:
- Secure shell access without SSH keys

---

# Key Concepts

## Logging

Captures and stores events and activity records.

## Monitoring

Analyzes metrics and operational data to detect problems.

## CloudWatch Alarm

Triggers actions when a metric crosses a threshold.

## SNS Notification

Sends alerts through email or other messaging protocols.

## CPU Utilization

Measures the percentage of CPU resources being used.

---

# Conclusion

Congratulations! You successfully:

- Created an Amazon SNS notification
- Configured a CloudWatch alarm
- Stress tested an EC2 instance
- Confirmed SNS email delivery
- Created a CloudWatch dashboard

You now understand how AWS monitoring and alerting services can help detect abnormal activity and improve operational security.