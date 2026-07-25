# Install and Configure the AWS CLI

## Lab Overview

The AWS Command Line Interface (AWS CLI) is a command-line tool used to interact with Amazon Web Services (AWS) services directly from a terminal.

In this lab, you will:

- Install the AWS CLI on a Red Hat Linux EC2 instance
- Configure the AWS CLI using IAM credentials
- Connect the AWS CLI to an AWS account
- Use AWS CLI commands to interact with AWS Identity and Access Management (IAM)

---

# Objectives

After completing this lab, you should be able to:

- Install and configure the AWS CLI
- Connect the AWS CLI to an AWS account
- Access IAM using the AWS CLI

---

# Estimated Duration

**45 minutes**

---

# Architecture Overview

The lab environment contains:

- A Virtual Private Cloud (VPC)
- A Red Hat EC2 instance
- AWS CLI installed on the EC2 instance
- IAM configuration connected to the AWS account

You access the EC2 instance using SSH.

---

# Task 1 — Connect to the Red Hat EC2 Instance Using SSH

## Windows Users

### Step 1 — Download Credentials

1. Choose **Details**
2. Choose **Show**
3. Download:
   - `labsuser.ppk`
4. Copy the:
   - `PublicIP`

---

### Step 2 — Install PuTTY

Download and install:

- PuTTY

---

### Step 3 — Connect Using PuTTY

1. Open `putty.exe`
2. Configure the SSH session:
   - Host Name:
     ```bash
     ec2-user@<PublicIP>
     ```
3. Load:
   - `labsuser.ppk`
4. Connect

---

## macOS and Linux Users

### Step 1 — Download PEM File

1. Choose **Details**
2. Choose **Show**
3. Download:
   - `labsuser.pem`
4. Copy the:
   - `PublicIP`

---

### Step 2 — Open Terminal

Navigate to the download directory:

```bash
cd ~/Downloads
```

---

### Step 3 — Change Key Permissions

```bash
chmod 400 labsuser.pem
```

---

### Step 4 — Connect Using SSH

Replace `<ip-address>` with your EC2 public IP:

```bash
ssh -i labsuser.pem ec2-user@<ip-address>
```

When prompted, type:

```bash
yes
```

---

# Task 2 — Install the AWS CLI on Red Hat Linux

## Step 1 — Download AWS CLI Installer

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
```

---

## Step 2 — Extract the Installer

```bash
unzip -u awscliv2.zip
```

---

## Step 3 — Install AWS CLI

```bash
sudo ./aws/install
```

---

## Step 4 — Verify Installation

```bash
aws --version
```

### Example Output

```bash
aws-cli/2.7.24 Python/3.8.8 Linux/4.14.133-113.105.amzn2.x86_64 botocore/2.4.5
```

---

## Step 5 — Open AWS CLI Help

```bash
aws help
```

To exit help:

```bash
q
```

---

# Task 3 — Observe IAM Configuration in AWS Console

## Step 1 — Open IAM

1. In AWS Console search for:
   ```text
   IAM
   ```
2. Open IAM

---

## Step 2 — View IAM User

1. Choose:
   - **Users**
2. Select:
   - `awsstudent`

---

## Step 3 — View Policy

1. Open:
   - **Permissions**
2. Expand:
   - `lab_policy`
3. Choose:
   - `{}` JSON

You will see the IAM policy document in JSON format.

---

## Step 4 — View Access Keys

1. Open:
   - **Security credentials**
2. Locate:
   - Access Key ID

The secret key is available in:

- **Details → Show**

---

# Task 4 — Configure AWS CLI

Run:

```bash
aws configure
```

Provide the following information:

| Setting | Value |
|---|---|
| AWS Access Key ID | AccessKey from lab details |
| AWS Secret Access Key | SecretKey from lab details |
| Default region name | us-west-2 |
| Default output format | json |

---

# Task 5 — Test AWS CLI with IAM

Run:

```bash
aws iam list-users
```

---

## Expected Result

A JSON response listing IAM users in the account.

Example:

```json
{
  "Users": [
    {
      "UserName": "awsstudent"
    }
  ]
}
```

---

# Activity 1 Challenge

## Objective

Download the `lab_policy` IAM policy document using only the AWS CLI.

---

# Step 1 — List IAM Policies

Run:

```bash
aws iam list-policies --scope Local
```

---

# Step 2 — Locate the Policy ARN

Find:

- `Arn`
- `DefaultVersionId`

Example:

```text
arn:aws:iam::038946776283:policy/lab_policy
```

Version example:

```text
v1
```

---

# Step 3 — Download the Policy Document

Run:

```bash
aws iam get-policy-version --policy-arn arn:aws:iam::038946776283:policy/lab_policy --version-id v1 > lab_policy.json
```

---

# Step 4 — Verify the File

```bash
cat lab_policy.json
```

---

# Useful AWS CLI Commands

## Show AWS CLI Version

```bash
aws --version
```

---

## Configure AWS CLI

```bash
aws configure
```

---

## List IAM Users

```bash
aws iam list-users
```

---

## List IAM Policies

```bash
aws iam list-policies --scope Local
```

---

## Get IAM Policy Version

```bash
aws iam get-policy-version --policy-arn <policy-arn> --version-id <version>
```

---

# Key Concepts

| Concept | Description |
|---|---|
| AWS CLI | Command-line interface for AWS |
| IAM | AWS Identity and Access Management |
| Access Key ID | Public credential used for AWS authentication |
| Secret Access Key | Private credential paired with the access key |
| JSON | JavaScript Object Notation used for policies |
| SSH | Secure Shell remote connection protocol |

---

# Key Takeaways

- AWS CLI allows management of AWS services through the terminal
- AWS CLI requires:
  - Access Key ID
  - Secret Access Key
- IAM policies are stored in JSON format
- AWS CLI can fully manage IAM resources

---

# Lab Summary

You successfully:

- Installed the AWS CLI
- Configured the AWS CLI
- Connected AWS CLI to AWS
- Used AWS CLI with IAM
- Retrieved IAM policy documents using AWS CLI

---

# Cleanup

When finished:

1. Choose:
   - **End Lab**
2. Confirm:
   - **Yes**

Lab resources will terminate automatically.

---

# Additional Resources

## AWS CLI Documentation

```text
https://docs.aws.amazon.com/cli/
```

## IAM Documentation

```text
https://docs.aws.amazon.com/iam/
```

## AWS Training and Certification

```text
https://aws.amazon.com/training/
```