# Challenge Lab: Python Scripting Exercise

## Duration

This lab takes approximately **40 minutes** to complete.

---

# Lab Overview

In this challenge lab, you will connect to a Linux EC2 instance and create a Python script that generates all prime numbers between 1 and 250. The script will save the results into a text file for verification.

This lab demonstrates:

- Python scripting
- Functions
- Loops
- Conditional statements
- File handling
- Linux command-line usage
- SSH connectivity

---

# Lab Objectives

You will:

- Launch the AWS lab environment
- Connect to a Linux EC2 instance using SSH
- Write a Python script
- Generate prime numbers between 1 and 250
- Save the results to a text file
- Verify the generated output
- Identify the absolute path of the script

---

# Launch Your Lab Environment

## Step 1: Start the Lab

1. Click **Start Lab** at the top of the lab page.
2. Wait until the following message appears:

```text
Lab status: ready
```

3. Close the status window by clicking the **X**.

---

# Lab Environment

The lab launches an Amazon EC2 instance named:

```text
Linux Host
```

You will use this server to develop and run Python scripts.

---

# Save Lab Details

## Step 1: Open the Details Panel

1. Click the **Details** drop-down menu.
2. Select **Show**.

---

## Step 2: Copy the Public IP Address

Locate:

```text
ips -- public
```

Copy the IP address.

---

## Step 3: Save the Information

Create a text file named:

```text
Lab Details.txt
```

Paste the public IP address into the file.

Recommended text editors:

- Visual Studio Code
- Sublime Text
- Atom
- Notepad++

This information will be referred to later as **Lab Details**.

---

# Using SSH to Connect to the Linux Host

---

# Windows Users

## Step 1: Download the PPK File

1. Open the **Details** panel.
2. Click **Download PPK**.
3. Save the file:

```text
labsuser.ppk
```

4. Record the Public IP address.
5. Close the Details panel.

---

## Step 2: Install PuTTY

Download and install PuTTY:

```text
https://www.putty.org/
```

---

## Step 3: Open PuTTY

Launch:

```text
putty.exe
```

---

## Step 4: Configure the SSH Session

Configure:

- Host Name = Public IP Address
- SSH Authentication Key = `labsuser.ppk`

Use the AWS instructions for connecting with PuTTY.

---

## Step 5: Connect to the Linux Host

Click **Open** to connect.

Accept the security warning if prompted.

---

# macOS and Linux Users

## Step 1: Download the PEM File

1. Open the **Details** panel.
2. Click **Download PEM**.
3. Save:

```text
labsuser.pem
```

4. Close the panel.

---

## Step 2: Open Terminal

Navigate to the directory containing the PEM file.

Example:

```bash
cd ~/Downloads
```

---

## Step 3: Change Permissions

Run:

```bash
chmod 400 labsuser.pem
```

---

## Step 4: Connect Using SSH

Replace `<public-ip>` with the public IP address saved earlier.

```bash
ssh -i labsuser.pem ec2-user@<public-ip>
```

---

## Step 5: Confirm the Connection

Type:

```text
yes
```

when prompted.

You are now connected to the Linux Host.

---

# Your Challenge

Write a Python script that:

1. Displays all prime numbers between 1 and 250
2. Stores the results in a file named `results.txt`
3. Tests the script
4. Verifies the generated output
5. Saves the script location for future reference

---

# Recommended Python Version

Both Python 2 and Python 3 are installed.

Use Python 3.

Run scripts using:

```bash
python3 file.py
```

---

# Step 1: Create the Python Script

Create a file named:

```text
prime_numbers.py
```

Example using nano:

```bash
nano prime_numbers.py
```

---

# Step 2: Add the Python Code

Paste the following code into the file:

```python
def is_prime(number):

    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):

        if number % i == 0:
            return False

    return True


prime_numbers = []

for num in range(1, 251):

    if is_prime(num):
        prime_numbers.append(str(num))


with open("results.txt", "w") as file:

    for prime in prime_numbers:
        file.write(prime + "\n")


print("Prime numbers saved to results.txt")
```

---

# Step 3: Save the Script

If using nano:

- Press `CTRL + O`
- Press `Enter`
- Press `CTRL + X`

---

# Step 4: Run the Script

Execute:

```bash
python3 prime_numbers.py
```

Expected output:

```text
Prime numbers saved to results.txt
```

---

# Step 5: Verify the Output File

Display the file contents:

```bash
cat results.txt
```

Expected output begins with:

```text
2
3
5
7
11
13
17
19
23
29
```

The file should contain all prime numbers between 1 and 250.

---

# Expected Prime Numbers

Prime numbers include:

```text
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47...
```

There should be:

```text
53 prime numbers
```

between 1 and 250.

---

# Step 6: Find the Absolute Path

Run:

```bash
pwd
```

Example output:

```text
/home/ec2-user
```

Example absolute path:

```text
/home/ec2-user/prime_numbers.py
```

Save this path for future reference.

---

# Understanding the Script

---

## Prime Number Function

```python
def is_prime(number):
```

Checks whether a number is prime.

---

## Loop Through Numbers

```python
for num in range(1, 251):
```

Loops through numbers 1 to 250.

---

## Store Prime Numbers

```python
prime_numbers.append(str(num))
```

Adds prime numbers to a list.

---

## Write Results to File

```python
with open("results.txt", "w") as file:
```

Creates and writes data to the file.

---

# Testing the Script

Verify that:

- The script runs without errors
- `results.txt` is created
- Prime numbers appear correctly
- The total number of primes is correct

---

# Troubleshooting

---

## Python Not Found

Check Python version:

```bash
python3 --version
```

---

## Permission Problems

Make the script executable:

```bash
chmod +x prime_numbers.py
```

---

## File Not Found

Check current files:

```bash
pwd
ls
```

---

# Linux Commands Used

| Command | Purpose |
|---|---|
| ssh | Connect to remote server |
| cd | Change directory |
| pwd | Display current directory |
| ls | List files |
| nano | Text editor |
| cat | Display file contents |
| chmod | Change file permissions |

---

# Key Python Concepts

| Concept | Description |
|---|---|
| Function | Reusable block of code |
| Loop | Repeats actions |
| Condition | Makes decisions |
| File Handling | Reading/writing files |
| List | Stores multiple values |

---

# Key Terms

| Term | Meaning |
|------|---------|
| Prime Number | Number divisible only by 1 and itself |
| SSH | Secure Shell remote connection |
| EC2 | Amazon Elastic Compute Cloud |
| Absolute Path | Full file location |
| Script | File containing executable code |

---

# Lab Review Questions

1. What is a prime number?
2. Why are functions useful in Python?
3. What is the purpose of file handling?
4. Why should Python 3 be used?
5. What is the purpose of SSH?

---

# Lab Complete

When finished:

1. Click **End Lab**
2. Click **Yes** to confirm
3. Close the lab status panel

---

# Additional Resources

AWS Training and Certification:

```text
https://aws.amazon.com/training/
```

---

# Summary

In this challenge lab, you launched an AWS lab environment, connected to a Linux EC2 instance, created a Python script to generate prime numbers between 1 and 250, stored the results in a text file, verified the output, and learned about Python scripting, Linux commands, functions, loops, and file handling.