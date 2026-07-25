# 💻 Amazon EC2 Instances (Challenge)

## 📖 Lab Overview

In this challenge lab, I configured a complete virtual network 
from scratch and launched an **Amazon Linux EC2 instance** running 
a web server. I then deployed a simple **HTML webpage** and 
accessed it publicly through a browser.

---

## 🏗️ Architecture Built

- **VPC** (`Challenge-VPC`) with CIDR `10.0.0.0/16`
- **Public Subnet** (`Challenge-Public-Subnet`) with 
CIDR `10.0.1.0/24`
- **Internet Gateway** (`Challenge-IGW`) attached to the VPC
- **Route Table** with `0.0.0.0/0` route to Internet Gateway
- **EC2 Instance** (`Challenge-Web-Server`) with Apache 
web server installed via user data script
- **Security Group** allowing SSH (port 22) and HTTP (port 80)

---

## 🎯 Objectives

- [x] Configure a virtual private network (VPC)
- [x] Launch an Amazon Linux EC2 instance in the VPC
- [x] Install and start a web server using user data
- [x] Deploy an HTML webpage to the web server
- [x] Access the webpage publicly via the instance's IP

---

## 🛠️ AWS Services Used

| Service | Purpose |
|---|---|
| Amazon VPC | Virtual network for the EC2 instance |
| Amazon EC2 | Web server instance |
| Internet Gateway | Public internet access for the VPC |
| Route Tables | Traffic routing in the VPC |
| Security Groups | SSH and HTTP firewall rules |
| EC2 Instance Connect | Browser-based SSH connection |

---

## 📋 Step-by-Step Summary

### Step 1: Create VPC
- Created **Challenge-VPC** with CIDR `10.0.0.0/16`
- Enabled DNS hostnames

### Step 2: Create Public Subnet
- Created **Challenge-Public-Subnet** with CIDR `10.0.1.0/24`
- Enabled auto-assign public IPv4 address

### Step 3: Create Internet Gateway
- Created **Challenge-IGW** and attached to **Challenge-VPC**

### Step 4: Configure Route Table
- Renamed route table to **Challenge-Route-Table**
- Added route `0.0.0.0/0 → Challenge-IGW`
- Associated **Challenge-Public-Subnet** with the route table

### Step 5: Launch EC2 Instance
- **Name:** Challenge-Web-Server
- **AMI:** Amazon Linux 2
- **Instance type:** t3.micro
- **Storage:** 8 GiB gp2
- **Security group:** SSH (port 22) + HTTP (port 80) from anywhere
- **User data script:**

```bash
#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
chmod 777 /var/www/html
```

### Step 6: Verify System Log
- Checked system log via Actions → Get system log
- Confirmed httpd was successfully installed ✅

### Step 7: Deploy Webpage
- Connected via EC2 Instance Connect
- Created `projects.html` with custom HTML content
- Copied file to `/var/www/html/`

```bash
cat > /tmp/projects.html << 'EOF'
<!DOCTYPE html>
<html>
<body>
<h1>Andrews's re/Start Project Work</h1>
<p>EC2 Instance Challenge Lab</p>
</body>
</html>
EOF
sudo cp /tmp/projects.html /var/www/html/projects.html
```

### Step 8: Test Webpage
- Accessed `http://<Public-IPv4>/projects.html` in browser
- Webpage displayed successfully ✅

---

## 💡 Key Concepts Learned

- A **VPC** must have an **Internet Gateway** and a properly 
configured **route table** before instances can access 
the internet
- **User data scripts** run automatically at instance launch 
and can install software like Apache
- **Security groups** must allow both **SSH (22)** and 
**HTTP (80)** for web server access
- **EC2 Instance Connect** allows SSH access without 
a key pair file
- The `/var/www/html/` directory is Apache's document root — 
files placed here are served as web pages
- `sudo` is required to write files to protected directories
- **Auto-assign public IP** must be enabled on the subnet 
for instances to get a public address

---

## ✅ Lab Outcome

Successfully built a complete VPC network, launched an EC2 
instance with Apache installed via user data, deployed a custom 
HTML webpage, and confirmed public access via the browser.

---

*Lab completed as part of the **AWS re/Start Program** — 
Cloud Practitioner track.*