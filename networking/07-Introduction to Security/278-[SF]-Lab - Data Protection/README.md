# Data Protection Using Encryption

## Lab Overview

Cryptography converts communicated information into secret code to keep data confidential and private. Encryption transforms readable plaintext into unreadable ciphertext, while decryption converts ciphertext back into readable plaintext.

In this lab, you will:

- Connect to a file server hosted on an Amazon EC2 instance
- Configure AWS Encryption CLI
- Create an AWS Key Management Service (AWS KMS) key
- Encrypt plaintext files
- View encrypted ciphertext
- Decrypt files back into plaintext

---

# Objectives

After completing this lab, you should be able to:

- Create an AWS KMS encryption key
- Install the AWS Encryption CLI
- Encrypt plaintext
- Decrypt ciphertext

---

# Duration

Approximately **45 minutes**

---

# Lab Environment

The environment includes:

- One preconfigured Amazon EC2 instance named **File Server**
- An IAM role attached for AWS Systems Manager Session Manager access
- Preconfigured backend AWS resources

---

# Task 1: Create an AWS KMS Key

## Step 1: Open AWS KMS

1. In AWS Console search for **KMS**
2. Select **Key Management Service**

---

## Step 2: Create a Key

1. Choose **Create a key**
2. Configure:

| Setting | Value |
|---|---|
| Key type | Symmetric |

3. Choose **Next**

---

## Step 3: Add Labels

Configure:

| Setting | Value |
|---|---|
| Alias | MyKMSKey |
| Description | Key used to encrypt and decrypt data files |

Choose **Next**

---

## Step 4: Define Administrative Permissions

1. Under **Key administrators**
2. Select:

- `voclabs`

Choose **Next**

---

## Step 5: Define Key Usage Permissions

1. Under **This account**
2. Select:

- `voclabs`

Choose **Next**

---

## Step 6: Finish Key Creation

1. Review configuration
2. Choose **Finish**

---

## Step 7: Copy the KMS Key ARN

1. Open the newly created key:
   - `MyKMSKey`
2. Copy the **ARN**
3. Save it in a text editor

You will use this ARN later.

---

# Summary of Task 1

You created:

- A symmetric AWS KMS key
- Administrative and usage permissions for the `voclabs` IAM role

---

# Task 2: Configure the File Server Instance

---

## Step 1: Open EC2

1. Search for **EC2**
2. Choose **Instances**
3. Select:
   - `File Server`
4. Choose:
   - **Connect**

---

## Step 2: Connect Using Session Manager

1. Open the **Session Manager** tab
2. Choose **Connect**

---

## Step 3: Configure AWS CLI Credentials

Run:

```bash
cd ~
aws configure
```

Enter:

| Prompt | Value |
|---|---|
| AWS Access Key ID | 1 |
| AWS Secret Access Key | 1 |
| Default region name | Your lab region |
| Default output format | Press Enter |

---

## Step 4: Copy Temporary Credentials

1. Return to Vocareum
2. Choose:
   - **AWS Details**
3. Under AWS CLI choose:
   - **Show**
4. Copy the entire credentials block

---

## Step 5: Edit Credentials File

Run:

```bash
vi ~/.aws/credentials
```

Inside `vi`:

1. Press:
   - `dd`
   multiple times to delete contents

2. Paste copied credentials

3. Save and exit:

```bash
:wq
```

---

## Step 6: Verify Credentials

Run:

```bash
cat ~/.aws/credentials
```

---

## Step 7: Install AWS Encryption CLI

Run:

```bash
pip3 install aws-encryption-sdk-cli
```

Export the path:

```bash
export PATH=$PATH:/home/ssm-user/.local/bin
```

---

# Summary of Task 2

You:

- Configured AWS credentials
- Installed AWS Encryption CLI
- Prepared the instance for encryption operations

---

# Task 3: Encrypt and Decrypt Data

---

## Step 1: Create Test Files

Run:

```bash
touch secret1.txt secret2.txt secret3.txt
```

Add content:

```bash
echo 'TOP SECRET 1!!!' > secret1.txt
```

View contents:

```bash
cat secret1.txt
```

---

## Step 2: Create Output Directory

Run:

```bash
mkdir output
```

---

## Step 3: Save the KMS ARN as a Variable

Replace `(KMS ARN)` with your copied ARN:

```bash
keyArn=(KMS ARN)
```

Example:

```bash
keyArn=arn:aws:kms:us-west-2:123456789:key/abc123
```

Run the command in the terminal.

---

# Encrypt the File

Run:

```bash
aws-encryption-cli --encrypt \
                     --input secret1.txt \
                     --wrapping-keys key=$keyArn \
                     --metadata-output ~/metadata \
                     --encryption-context purpose=test \
                     --commitment-policy require-encrypt-require-decrypt \
                     --output ~/output/.
```

---

## Verify Success

Run:

```bash
echo $?
```

Expected output:

```bash
0
```

---

## View Encrypted File

List files:

```bash
ls output
```

Expected:

```bash
secret1.txt.encrypted
```

Open encrypted file:

```bash
cd output
cat secret1.txt.encrypted
```

You will see unreadable ciphertext.

---

# Encryption Concept

Encryption transforms:

- Plaintext → Ciphertext

Using:

- Symmetric encryption
- AWS KMS key
- Encryption algorithms

Only authorized decryption restores readability.

---

# Decrypt the File

Run:

```bash
aws-encryption-cli --decrypt \
                     --input secret1.txt.encrypted \
                     --wrapping-keys key=$keyArn \
                     --commitment-policy require-encrypt-require-decrypt \
                     --encryption-context purpose=test \
                     --metadata-output ~/metadata \
                     --max-encrypted-data-keys 1 \
                     --buffer \
                     --output .
```

---

## View Decrypted File

List files:

```bash
ls
```

Expected:

```bash
secret1.txt.encrypted.decrypted
```

Open the decrypted file:

```bash
cat secret1.txt.encrypted.decrypted
```

Expected output:

```text
TOP SECRET 1!!!
```

---

# Decryption Concept

Decryption transforms:

- Ciphertext → Plaintext

Using:

- The same symmetric AWS KMS key
- Matching encryption context
- AWS Encryption CLI

---

# Summary of Task 3

You successfully:

- Created plaintext files
- Encrypted files using AWS KMS
- Viewed encrypted ciphertext
- Decrypted files back into readable plaintext

---

# Key Concepts Learned

| Concept | Description |
|---|---|
| Cryptography | Protecting information using mathematical techniques |
| Encryption | Converting plaintext into ciphertext |
| Decryption | Converting ciphertext back into plaintext |
| AWS KMS | AWS managed encryption key service |
| Symmetric Encryption | Same key used for encryption and decryption |
| AWS Encryption CLI | Command-line tool for encrypting/decrypting data |

---

# Commands Reference

## Configure AWS CLI

```bash
aws configure
```

## Install Encryption CLI

```bash
pip3 install aws-encryption-sdk-cli
```

## Encrypt File

```bash
aws-encryption-cli --encrypt
```

## Decrypt File

```bash
aws-encryption-cli --decrypt
```

## View File

```bash
cat filename
```

---

# Final Outcome

At the end of this lab you:

- Created an AWS KMS key
- Configured AWS credentials
- Installed AWS Encryption CLI
- Encrypted sensitive data
- Decrypted encrypted data successfully
- Understood symmetric encryption workflows in AWS