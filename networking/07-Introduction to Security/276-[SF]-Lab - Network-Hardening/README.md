# Using Amazon Inspector for Vulnerability Assessment and Remediation

## Lab Overview

In this lab, you will use Amazon Inspector to scan AWS resources for vulnerabilities, specifically AWS Lambda functions. You will learn how to activate Amazon Inspector, analyze vulnerability findings, and remediate detected issues.

The developers at AnyCompany are building an application using AWS Lambda and require an automated security solution capable of scanning vulnerable software packages and code. Amazon Inspector fulfills this requirement by continuously scanning Lambda functions, EC2 instances, and Amazon ECR repositories.

---

# Objectives

After completing this lab, you should be able to:

- Activate Amazon Inspector
- Analyze and interpret vulnerability findings
- Remediate vulnerabilities detected by Amazon Inspector

---

# Duration

This lab takes approximately **30 minutes** to complete.

---

# Lab Environment

The environment contains AWS Lambda functions with intentionally vulnerable packages. Amazon Inspector will scan these functions and report findings based on severity levels.

---

# AWS Services Used

- Amazon Inspector
- AWS Lambda
- Amazon EC2
- Amazon ECR
- National Vulnerability Database (NVD)

---

# Architecture Overview

The lab environment includes:

- Vulnerable AWS Lambda functions
- Amazon Inspector scanning enabled
- Automated vulnerability detection
- Vulnerability remediation workflow

---

# Accessing the AWS Management Console

## Step 1: Start the Lab

1. Choose **Start Lab**
2. Wait until the lab status turns green
3. Open the AWS Console

### Lab Status Indicators

| Status Color | Meaning |
|---|---|
| 🔴 Red | Lab not started |
| 🟡 Yellow | Lab starting |
| 🟢 Green | Lab ready |

---

# Task 1: Activate Amazon Inspector

In this task, you activate Amazon Inspector to continuously scan AWS Lambda functions.

---

## Step 1: Open Amazon Inspector

1. In the AWS Console search bar, search for:

```bash
Inspector
```

2. Open **Amazon Inspector**

---

## Step 2: Activate Amazon Inspector

1. In the left navigation pane, choose:

```text
Activate Inspector
```

2. Choose:

```text
Activate Inspector
```

---

## Step 3: Verify Activation

After activation, you should see:

```text
Welcome to Inspector. Your first scan is underway.
```

---

## Step 4: Wait for Scanning

Refresh the page periodically until:

```text
Dashboard > Summary > Environment coverage > Lambda functions = 100%
```

---

# Task 2: Review Inspected Resources

In this task, you review the vulnerabilities detected by Amazon Inspector.

---

# Task 2.1: Review Lambda Function Findings

## Step 1: Open Findings

1. In the left navigation pane, choose:

```text
Findings > All findings
```

You should see:

- 3 vulnerability findings
- Severity level: Medium
- Affected Lambda functions

---

## Step 2: Review Vulnerability Details

Select the finding:

```text
CVE-2023-32681 - requests
```

This opens the vulnerability details pane.

---

## Step 3: Open NVD Reference

Under **Vulnerability details**, choose the external link next to the Vulnerability ID.

This opens the National Vulnerability Database (NVD) webpage with detailed CVE information.

---

# Understanding the Vulnerability

## Vulnerable Package

The issue is caused by an outdated Python package:

```python
requests==2.20.0
```

This version contains known vulnerabilities.

---

## Amazon Inspector Recommendation

Amazon Inspector recommends upgrading the package to a newer version.

---

# Task 3: Remediate Vulnerability Findings

In this task, you update the Lambda function to remove the vulnerable package version.

---

# Task 3.1: Remediate Lambda Package Vulnerabilities

## Step 1: Open AWS Lambda

1. In the AWS Console search bar, search for:

```bash
Lambda
```

2. Open **AWS Lambda**

---

## Step 2: Open the Vulnerable Function

Choose the Lambda function:

```text
get-request
```

---

## Step 3: Edit requirements.txt

In the code editor:

1. Open:

```text
requirements.txt
```

2. Find this line:

```python
requests==2.20.0
```

3. Replace it with:

```python
requests
```

---

# Why This Fix Works

When no version number is specified:

```python
requests
```

AWS Lambda installs the latest available version of the package, which resolves the vulnerability.

---

## Step 4: Deploy the Function

Choose:

```text
Deploy
```

Expected output:

```text
Successfully updated the function get-request
```

---

# Task 4: Verify Remediation

After deployment, Amazon Inspector automatically rescans the Lambda function.

---

## Step 1: Return to Amazon Inspector

1. Search for:

```bash
Amazon Inspector
```

2. Open:

```text
Findings > All findings
```

---

## Step 2: View Closed Findings

Under finding status:

```text
Active → Closed
```

You should now see:

```text
CVE-2023-32681 - requests
```

listed as **Closed**.

This confirms successful remediation.

---

# Task 5: Confirm Updated Scan Timestamp

## Step 1: Open Lambda Coverage

In the left navigation pane:

```text
Resources coverage > Lambda functions
```

---

## Step 2: Verify Latest Scan

Check the:

```text
Last scanned
```

timestamp.

The updated timestamp confirms that Amazon Inspector rescanned the Lambda function after deployment.

---

# Important Concepts Learned

## Amazon Inspector

Amazon Inspector is an automated vulnerability management service that continuously scans AWS workloads for vulnerabilities.

---

## CVE

A Common Vulnerabilities and Exposures (CVE) entry identifies publicly known cybersecurity vulnerabilities.

Example:

```text
CVE-2023-32681
```

---

## Vulnerability Remediation

Remediation involves:

- Updating vulnerable packages
- Applying security patches
- Deploying fixed application versions

---

# Key AWS Security Benefits

Amazon Inspector provides:

- Continuous vulnerability scanning
- Automated security assessments
- Near real-time detection
- Integration with Lambda, EC2, and ECR
- Severity classification
- Remediation guidance

---

# Commands and Configurations Used

## Vulnerable Package

```python
requests==2.20.0
```

---

## Remediated Package

```python
requests
```

---

# Security Best Practices

- Always use updated package versions
- Continuously scan workloads
- Automate vulnerability management
- Review CVE reports regularly
- Patch vulnerabilities immediately
- Use least privilege access controls

---

# Expected Results

At the end of this lab:

✅ Amazon Inspector activated successfully  
✅ Lambda functions scanned successfully  
✅ Vulnerability findings analyzed  
✅ Vulnerable package remediated  
✅ Findings moved from Active to Closed  

---

# Conclusion

In this lab, you learned how to use Amazon Inspector to detect and remediate vulnerabilities in AWS Lambda functions. You activated Amazon Inspector, analyzed CVE findings, updated vulnerable dependencies, and confirmed remediation through automated rescanning.

Amazon Inspector helps organizations continuously improve cloud security by identifying vulnerabilities early in the development lifecycle.

---

# Author

AWS Security Lab Notes  
Prepared for GitHub Documentation and Study Reference
