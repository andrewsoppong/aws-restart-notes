# AWS Identity and Access Management (IAM)

## Overview
AWS Identity and Access Management (IAM) is a web service that helps securely control access to AWS resources. IAM allows administrators to manage users, groups, roles, and permissions to ensure that only authorized entities can access AWS services and resources.

This lesson explains the IAM service, the types of security credentials it supports, and how authentication and authorization are implemented in AWS.

---

# What You Will Learn

At the core of this lesson, you will learn how to:

- Describe the AWS Identity and Access Management (IAM) service
- List the different types of security credentials that IAM supports
- Describe how authentication and authorization are implemented in IAM

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Understand the purpose of AWS IAM
- Identify IAM components and features
- Describe IAM users, groups, and roles
- Recognize the types of AWS security credentials
- Explain authentication and authorization in AWS
- Understand IAM best practices

---

# What is AWS IAM?

AWS Identity and Access Management (IAM) is a service that enables you to securely manage access to AWS resources.

IAM helps organizations:

- Control who can access AWS resources
- Define permissions for users and services
- Implement least privilege access
- Enhance security with authentication methods

IAM is available globally and does not require additional cost.

---

# Core Components of IAM

## 1. IAM Users

An IAM user represents a person or application that needs access to AWS resources.

### Features

- Unique username
- Security credentials
- Assigned permissions

### Example

A developer may have an IAM user account that allows access to Amazon EC2 and Amazon S3.

---

## 2. IAM Groups

An IAM group is a collection of IAM users.

### Benefits

- Simplifies permission management
- Allows centralized access control

### Example

A Developers group may have permissions to deploy applications.

---

## 3. IAM Roles

An IAM role is an identity with permissions that can be assumed temporarily.

### Common Uses

- EC2 instance access
- Cross-account access
- AWS service permissions

### Features

- No permanent credentials
- Temporary security credentials
- Assumed when needed

---

## 4. IAM Policies

Policies define permissions using JSON documents.

Policies determine:

- What actions are allowed or denied
- Which resources can be accessed
- Under what conditions access is permitted

---

# Types of IAM Policies

## Managed Policies

Predefined policies created by AWS or administrators.

### Types

- AWS Managed Policies
- Customer Managed Policies

---

## Inline Policies

Policies directly attached to a single user, group, or role.

---

# Security Credentials Supported by IAM

IAM supports several types of credentials.

---

## 1. Username and Password

Used to access:

- AWS Management Console

### Example

A user signs in with:
- Username
- Password

---

## 2. Access Keys

Used for:

- AWS CLI
- SDKs
- API access

### Components

| Credential | Purpose |
|---|---|
| Access Key ID | Identifies the user |
| Secret Access Key | Authenticates requests |

---

## 3. Multi-Factor Authentication (MFA)

Adds an extra layer of security.

### MFA Methods

- Authenticator apps
- Hardware tokens
- Security keys

### Benefits

- Protects against stolen passwords
- Improves account security

---

## 4. Temporary Security Credentials

Provided through IAM roles or AWS STS (Security Token Service).

### Benefits

- Short-lived access
- Reduced credential exposure
- Enhanced security

---

# Authentication in IAM

Authentication verifies identity.

## Authentication Process

1. User submits credentials
2. AWS verifies credentials
3. Access is granted if credentials are valid

### Supported Authentication Methods

- Passwords
- Access keys
- MFA
- Temporary credentials

---

# Authorization in IAM

Authorization determines what actions an authenticated identity can perform.

IAM evaluates:

- Policies
- Permissions
- Resource access rules

---

# How Authorization Works

AWS evaluates requests in this order:

1. Authenticate the identity
2. Evaluate applicable policies
3. Determine whether access is allowed or denied

---

# IAM Policy Structure

IAM policies are written in JSON format.

## Example Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "*"
    }
  ]
}