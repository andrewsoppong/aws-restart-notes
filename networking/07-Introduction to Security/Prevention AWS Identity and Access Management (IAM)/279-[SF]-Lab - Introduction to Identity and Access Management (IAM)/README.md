# Introduction to AWS Identity and Access Management (IAM)

## Overview

In this lab, you explore users, user groups, and policies in AWS Identity and Access Management (IAM). You learn how IAM controls authentication and authorization across AWS resources using users, groups, and policies.

---

# Objectives

By the end of this lab, you will be able to:

- Create and apply an IAM password policy
- Explore pre-created IAM users and user groups
- Inspect IAM policies attached to user groups
- Add users to groups with specific permissions
- Locate and use the IAM sign-in URL
- Test IAM permissions across AWS services

---

# Lab Environment

The environment contains:

## IAM Users

- `user-1`
- `user-2`
- `user-3`

## IAM Groups

- `EC2-Admin`
- `EC2-Support`
- `S3-Support`

---

# Duration

Approximately **60 minutes**

---

# Task 1: Create an Account Password Policy

## Steps

1. Open the AWS Management Console
2. Search for **IAM**
3. Choose **Account settings**
4. Choose **Change password policy**

## Configure the Following

- Minimum password length: `10`
- Enable:
  - Require uppercase letters
  - Require lowercase letters
  - Require numbers
  - Require non-alphanumeric characters
  - Allow users to change their own password
  - Enable password expiration
  - Prevent password reuse
- Password expiration: `90 days`
- Password reuse prevention: `5 passwords`

5. Choose **Save changes**

---

# Task 2: Explore Users and User Groups

## Explore IAM Users

1. Open **IAM**
2. Choose **Users**

### Existing Users

- `user-1`
- `user-2`
- `user-3`

### Review user-1

Inspect:

- Permissions tab
- Groups tab
- Security credentials tab

---

## Explore IAM Groups

Choose **User groups**

### Existing Groups

- `EC2-Admin`
- `EC2-Support`
- `S3-Support`

---

## EC2-Support Group

### Attached Policy

`AmazonEC2ReadOnlyAccess`

### Permissions

- View EC2 resources
- View ELB resources
- View CloudWatch resources
- View Auto Scaling resources

---

## S3-Support Group

### Attached Policy

`AmazonS3ReadOnlyAccess`

### Permissions

- List S3 buckets
- View S3 objects

---

## EC2-Admin Group

### Attached Policy

`EC2-Admin-Policy`

### Permissions

- Describe EC2 instances
- Start EC2 instances
- Stop EC2 instances

---

# Business Scenario

| User | Group | Permissions |
|---|---|---|
| user-1 | S3-Support | Read-only access to Amazon S3 |
| user-2 | EC2-Support | Read-only access to Amazon EC2 |
| user-3 | EC2-Admin | View, start, and stop EC2 instances |

---

# Task 3: Add Users to User Groups

## Add user-1 to S3-Support

1. Open **User groups**
2. Choose `S3-Support`
3. Open the **Users** tab
4. Choose **Add users**
5. Select `user-1`
6. Choose **Add Users**

---

## Add user-2 to EC2-Support

Repeat the process and add:

- `user-2` → `EC2-Support`

---

## Add user-3 to EC2-Admin

Repeat the process and add:

- `user-3` → `EC2-Admin`

---

# Task 4: Sign In and Test Permissions

## Locate IAM Sign-In URL

1. Open **IAM Dashboard**
2. Copy the **IAM Sign-in URL**

Example:

```text
https://123456789012.signin.aws.amazon.com/console
```

3. Open a private/incognito browser window
4. Paste the URL

---

# Test user-1 Permissions

## Sign In

- Username: `user-1`
- Password: `Lab-Password1`

## Verify Access

### Amazon S3

- Can view buckets
- Can browse bucket contents

### Amazon EC2

- Cannot access EC2 resources
- Receives authorization error

---

# Test user-2 Permissions

## Sign In

- Username: `user-2`
- Password: `Lab-Password2`

## Verify Access

### Amazon EC2

- Can view instances
- Cannot stop instances

### Amazon S3

- Cannot list buckets

---

# Test user-3 Permissions

## Sign In

- Username: `user-3`
- Password: `Lab-Password3`

## Verify Access

### Amazon EC2

- Can view instances
- Can stop instances

---

# Key IAM Concepts

## IAM Users

Identities created for people or applications.

## IAM Groups

Collections of users with shared permissions.

## Managed Policies

Reusable AWS-managed permission policies.

## Inline Policies

Policies attached directly to a single user or group.

## Authentication

Verifies user identity.

## Authorization

Determines allowed actions and resources.

---

# Conclusion

In this lab, you learned how to:

- Configure IAM password policies
- Explore IAM users and groups
- Understand IAM managed and inline policies
- Assign permissions using groups
- Test access permissions across AWS services
- Verify authentication and authorization behavior in AWS IAM