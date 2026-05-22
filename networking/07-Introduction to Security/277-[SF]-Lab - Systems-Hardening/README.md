# Systems Hardening with Patch Manager via AWS Systems Manager

## Lab Overview

In organizations with hundreds or thousands of workstations, keeping operating systems and software updated is critical for security and compliance. Administrators must ensure systems meet a minimum approved software version and remain protected against vulnerabilities.

In this lab, you will use AWS Systems Manager Patch Manager to:

- Patch Linux EC2 instances using default patch baselines
- Create a custom patch baseline for Windows instances
- Use patch groups to manage patching
- Verify patch compliance across all managed nodes

The lab environment already includes:

- 3 Linux EC2 instances
- 3 Windows EC2 instances
- Preconfigured IAM roles and Systems Manager setup

---

# Objectives

After completing this lab, you should be able to:

- Patch Linux instances using default baselines
- Create custom patch baselines
- Use patch groups to patch Windows instances using custom baselines
- Verify patch compliance

---

# Duration

Approximately 60 minutes

---

# Lab Environment

The environment contains:

| Resource | Quantity |
|---|---|
| Linux EC2 Instances | 3 |
| Windows EC2 Instances | 3 |

Backend resources such as IAM roles and Systems Manager integrations are already configured.

---

# Accessing the AWS Management Console

1. Choose **Start Lab**
2. Wait until the lab status becomes **Ready**
3. Choose the green **AWS** button to open the AWS Management Console
4. Allow pop-ups if prompted
5. If prompted, switch to the new Console Home
6. Do not change the AWS Region unless instructed

---

# Task 1: Patch Linux Instances Using Default Baselines

## Step 1: Open AWS Systems Manager

1. In the AWS Console search bar, search for:
   ```text
   Systems Manager
   ```

2. Open **AWS Systems Manager**

---

## Step 2: Review Managed Nodes

1. In the left navigation pane:
   ```text
   Node Management → Fleet Manager
   ```

2. Observe:
   - 3 Linux instances
   - 3 Windows instances

3. Select:
   ```text
   Linux-1
   ```

4. Choose:
   ```text
   Node actions → View details
   ```

5. Review:
   - Platform type
   - Node type
   - OS name
   - IAM role

6. Return to:
   ```text
   AWS Systems Manager
   ```

---

## Step 3: Open Patch Manager

1. In the left navigation pane:
   ```text
   Node Management → Patch Manager
   ```

2. If prompted:
   ```text
   Choose "Start with an overview"
   ```

---

## Step 4: Patch Linux Instances

1. Choose:
   ```text
   Patch now
   ```

2. Configure:

| Setting | Value |
|---|---|
| Patching operation | Scan and install |
| Reboot option | Reboot if needed |
| Instances to patch | Patch only the target instances I specify |
| Target selection | Specify instance tags |
| Tag key | Patch Group |
| Tag value | LinuxProd |

3. Choose:
   ```text
   Add
   ```

4. Choose:
   ```text
   Patch now
   ```

---

## Step 5: Monitor Patch Progress

Observe:

- AWS-PatchNowAssociation panel
- Scan/Install operation summary

Wait until all 3 Linux instances complete successfully.

---

# Task 2: Create a Custom Patch Baseline for Windows

## Step 1: Open Patch Baselines

1. Return to:
   ```text
   Systems Manager → Patch Manager
   ```

2. Choose:
   ```text
   Patch baselines
   ```

3. Choose:
   ```text
   Create patch baseline
   ```

---

## Step 2: Configure Baseline Details

Configure:

| Setting | Value |
|---|---|
| Name | WindowsServerSecurityUpdates |
| Description | Windows security baseline patch |
| Operating system | Windows |
| Default patch baseline | Leave unchecked |

---

## Step 3: Configure First Approval Rule

### Rule 1

| Setting | Value |
|---|---|
| Products | WindowsServer2019 |
| Severity | Critical |
| Classification | SecurityUpdates |
| Auto-approval | 3 days |
| Compliance reporting | Critical |

---

## Step 4: Add Second Approval Rule

Choose:
```text
Add rule
```

### Rule 2

| Setting | Value |
|---|---|
| Products | WindowsServer2019 |
| Severity | Important |
| Classification | SecurityUpdates |
| Auto-approval | 3 days |
| Compliance reporting | High |

---

## Step 5: Create Baseline

Choose:
```text
Create patch baseline
```

---

# Task 3: Associate Patch Group with Baseline

## Step 1: Select Patch Baseline

1. Locate:
   ```text
   WindowsServerSecurityUpdates
   ```

2. Select the baseline

3. Choose:
   ```text
   Actions → Modify patch groups
   ```

---

## Step 2: Add Patch Group

Under Patch groups:

```text
WindowsProd
```

Choose:

```text
Add
```

Then choose:

```text
Close
```

---

# Task 4: Tag Windows Instances

## Step 1: Open EC2 Console

1. Search for:
   ```text
   EC2
   ```

2. Open:
   ```text
   Instances
   ```

---

## Step 2: Tag Windows-1

1. Select:
   ```text
   Windows-1
   ```

2. Open:
   ```text
   Tags tab
   ```

3. Choose:
   ```text
   Manage tags
   ```

4. Choose:
   ```text
   Add new tag
   ```

5. Configure:

| Key | Value |
|---|---|
| Patch Group | WindowsProd |

6. Choose:
   ```text
   Save
   ```

---

## Step 3: Repeat for Other Windows Instances

Repeat the same process for:

- Windows-2
- Windows-3

---

# Task 5: Patch Windows Instances

## Step 1: Return to Patch Manager

1. Open:
   ```text
   Systems Manager → Patch Manager
   ```

2. Choose:
   ```text
   Patch now
   ```

---

## Step 2: Configure Windows Patching

| Setting | Value |
|---|---|
| Patching operation | Scan and install |
| Reboot option | Reboot if needed |
| Instances to patch | Patch only the target instances I specify |
| Target selection | Specify instance tags |
| Tag key | Patch Group |
| Tag value | WindowsProd |

Choose:

```text
Add
```

Then choose:

```text
Patch now
```

---

## Step 3: Monitor Patch Execution

1. When available, choose the:
   ```text
   Execution ID
   ```

2. Open one instance with status:
   ```text
   InProgress
   ```

3. Choose:
   ```text
   Output
   ```

4. Expand the output panel

Observe:

- PatchBaselineOperations
- PatchGroup: WindowsProd

---

# Task 6: Verify Compliance

## Step 1: Open Dashboard

1. In Patch Manager, open:
   ```text
   Dashboard
   ```

2. Under Compliance summary verify:

```text
Compliant: 6
```

This confirms all Linux and Windows instances are compliant.

---

## Step 2: Review Compliance Reporting

1. Open:
   ```text
   Compliance reporting
   ```

2. Verify all six instances show:

```text
Compliant
```

---

## Step 3: Review Detailed Patch Information

Scroll right to view:

- Critical noncompliant count
- Security noncompliant count
- Other noncompliant count
- Last operation date
- Baseline ID

---

## Step 4: View Installed Patches

1. Choose the Node ID of a Windows instance
2. Open:
   ```text
   Patch tab
   ```

3. Review:
   - Installed patches
   - Installed time

---

# Key Concepts Learned

## AWS Systems Manager Patch Manager

Patch Manager automates:

- Patch scanning
- Patch installation
- Compliance reporting
- Patch scheduling

---

## Patch Baselines

Patch baselines define:

- Approved patches
- Rejected patches
- Auto-approval timing
- Severity classifications

---

## Patch Groups

Patch groups allow administrators to:

- Organize instances
- Apply different patch baselines
- Automate targeting

---

## Compliance Reporting

Compliance reporting provides:

- Patch status visibility
- Security auditing
- Noncompliant system tracking

---

# Final Outcome

By completing this lab, you successfully:

- Patched Linux instances using default baselines
- Created a custom Windows patch baseline
- Used patch groups for targeted patching
- Patched Windows instances
- Verified compliance for all managed nodes