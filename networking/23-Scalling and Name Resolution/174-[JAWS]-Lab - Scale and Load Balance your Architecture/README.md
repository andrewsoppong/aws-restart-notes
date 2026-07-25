# Scaling and Load Balancing Your Architecture

## Overview

This lab demonstrates how to improve application availability, scalability, and fault tolerance using:

* Amazon EC2
* Amazon Machine Images (AMI)
* Application Load Balancer (ALB)
* EC2 Launch Templates
* EC2 Auto Scaling Groups
* Amazon CloudWatch Alarms

The lab begins with a single web server and ends with a highly available architecture that distributes traffic across multiple EC2 instances running in private subnets across multiple Availability Zones.

---

## Objectives

By completing this lab, I learned how to:

* Create an Amazon Machine Image (AMI)
* Create and configure an Application Load Balancer
* Create a Launch Template
* Create an Auto Scaling Group
* Deploy instances in private subnets
* Configure target tracking scaling policies
* Monitor scaling events using CloudWatch alarms
* Test automatic scaling based on CPU utilization

---

## Architecture

### Initial Architecture

* Single EC2 instance (Web Server 1)
* Public subnet
* Single Availability Zone

### Final Architecture

* Application Load Balancer
* Auto Scaling Group
* Multiple EC2 instances
* Private Subnet 1
* Private Subnet 2
* Multiple Availability Zones
* CloudWatch Alarms

---

## Task 1: Create an AMI

### Purpose

Create a reusable image from the existing Web Server 1 instance.

### Steps

1. Open EC2 Console.
2. Select **Web Server 1**.
3. Choose:

Actions → Image and templates → Create image

4. Configure:

* Image Name: Web Server AMI
* Description: Lab AMI for Web Server

5. Create the image.

### Result

A custom AMI was created and stored for future instance launches.

---

## Task 2: Create an Application Load Balancer

### Purpose

Distribute incoming HTTP requests across multiple EC2 instances.

### Steps

1. Open EC2 Console.
2. Navigate to:

Load Balancers → Create Load Balancer

3. Choose:

Application Load Balancer

4. Configure:

* Name: LabELB
* VPC: Lab VPC
* Availability Zones:

  * Public Subnet 1
  * Public Subnet 2

5. Attach:

* Web Security Group

---

### Create Target Group

1. Create a new target group.

Configuration:

* Target Type: Instances
* Name: lab-target-group

2. Create target group.

3. Return to load balancer setup.

4. Configure Listener:

HTTP → Forward to lab-target-group

5. Create load balancer.

### Result

Application Load Balancer successfully created.

---

## Task 3: Create Launch Template

### Purpose

Define how Auto Scaling launches EC2 instances.

### Configuration

| Setting        | Value                   |
| -------------- | ----------------------- |
| Template Name  | lab-app-launch-template |
| AMI            | Web Server AMI          |
| Instance Type  | t3.micro                |
| Key Pair       | None                    |
| Security Group | Web Security Group      |

### Result

Launch Template successfully created.

---

## Task 4: Create Auto Scaling Group

### Purpose

Automatically maintain and scale EC2 capacity.

### Configuration

#### General

| Setting         | Value                   |
| --------------- | ----------------------- |
| Name            | Lab Auto Scaling Group  |
| Launch Template | lab-app-launch-template |

#### Networking

| Setting | Value                              |
| ------- | ---------------------------------- |
| VPC     | Lab VPC                            |
| Subnets | Private Subnet 1, Private Subnet 2 |

#### Load Balancing

| Setting               | Value            |
| --------------------- | ---------------- |
| Existing Target Group | lab-target-group |
| Health Check Type     | ELB              |

#### Capacity

| Setting          | Value |
| ---------------- | ----- |
| Desired Capacity | 2     |
| Minimum Capacity | 2     |
| Maximum Capacity | 4     |

#### Scaling Policy

| Setting      | Value                   |
| ------------ | ----------------------- |
| Policy Type  | Target Tracking         |
| Metric       | Average CPU Utilization |
| Target Value | 50%                     |

#### Tags

| Key  | Value        |
| ---- | ------------ |
| Name | Lab Instance |

### Result

Auto Scaling Group launched two EC2 instances across private subnets.

---

## Task 5: Verify Load Balancing

### Steps

1. Open Target Groups.
2. Select:

lab-target-group

3. Verify:

Registered Targets → Healthy

4. Copy the DNS name of LabELB.
5. Open the DNS name in a browser.

### Result

The application successfully loaded through the Application Load Balancer.

---

## Task 6: Test Auto Scaling

### Purpose

Trigger Auto Scaling using increased CPU load.

### Steps

1. Open CloudWatch.
2. Navigate to:

Alarms → All Alarms

3. Locate:

* AlarmHigh
* AlarmLow

4. Open Load Test Application.
5. Click:

Load Test

6. Wait several minutes.

### Expected Result

* CPU utilization exceeds 50%.
* AlarmHigh enters "In Alarm" state.
* Auto Scaling launches additional EC2 instances.

### Verification

EC2 Console → Instances

Instance count increased beyond the original two instances.

---

## Task 7: Terminate Original Web Server

### Purpose

Remove the original source instance after creating the AMI.

### Steps

1. Select Web Server 1.
2. Choose:

Instance State → Terminate Instance

3. Confirm termination.

### Result

Web Server 1 terminated successfully.

---

## CloudWatch Monitoring

CloudWatch automatically created alarms to monitor:

* High CPU utilization
* Low CPU utilization

These alarms trigger Auto Scaling activities to maintain approximately 50% average CPU usage across all instances.

---

## Key AWS Services Used

* Amazon EC2
* Amazon Machine Images (AMI)
* Application Load Balancer (ALB)
* EC2 Auto Scaling
* Launch Templates
* Target Groups
* Amazon CloudWatch
* VPC
* Private Subnets
* Public Subnets

---

## Real-World SaaS Application

This architecture is suitable for:

* School Management Systems
* Student Portals
* Learning Management Systems
* E-Commerce Platforms
* Business Applications

For a School Management SaaS, the Application Load Balancer would distribute requests from students, teachers, and administrators across multiple application servers, while Auto Scaling would automatically add servers during peak periods such as registration, fee payment, and examination result releases.

---

## Skills Gained

* Creating reusable EC2 images
* Configuring Application Load Balancers
* Creating Launch Templates
* Deploying Auto Scaling Groups
* Monitoring infrastructure with CloudWatch
* Designing scalable and highly available architectures
* Implementing fault tolerance across multiple Availability Zones
