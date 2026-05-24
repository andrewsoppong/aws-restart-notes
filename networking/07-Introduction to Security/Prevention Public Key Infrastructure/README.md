# Public Key Infrastructure (PKI) and Certificates

## Overview
This lesson introduces Public Key Infrastructure (PKI), digital certificates, and certification authorities (CAs). PKI is a framework used to secure communications, authenticate identities, and protect sensitive information through encryption.

---

# What You Will Learn

At the core of this lesson, you will learn how to:

- Explain how the Public Key Infrastructure (PKI) works and describe its major components
- Explain how certificates work and how they can be used to secure information
- Describe certification authorities (CAs) and their common configurations

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Understand the purpose of PKI
- Identify the components of PKI
- Explain how public and private keys work
- Describe how digital certificates are used
- Understand the role of certification authorities
- Explain certificate trust chains and validation

---

# What is PKI?

Public Key Infrastructure (PKI) is a system that manages:

- Encryption keys
- Digital certificates
- Authentication processes
- Secure communication methods

PKI helps ensure:

- Confidentiality
- Integrity
- Authentication
- Nonrepudiation

---

# Public Key Cryptography

PKI uses asymmetric encryption, which involves two keys:

| Key Type | Purpose |
|---|---|
| Public Key | Encrypts data and verifies signatures |
| Private Key | Decrypts data and creates signatures |

## How It Works

1. A sender encrypts data using the recipient’s public key.
2. Only the recipient’s private key can decrypt the data.
3. This ensures secure communication.

---

# Major Components of PKI

## 1. Certificate Authority (CA)

A CA is a trusted organization that:

- Issues certificates
- Validates identities
- Maintains trust relationships

### Responsibilities

- Verify certificate requests
- Sign digital certificates
- Revoke compromised certificates

---

## 2. Registration Authority (RA)

The Registration Authority validates identities before certificates are issued.

### Functions

- Identity verification
- Approving certificate requests
- Assisting the CA

---

## 3. Digital Certificates

A digital certificate is an electronic document that proves ownership of a public key.

Certificates contain:

- Owner information
- Public key
- Expiration date
- Issuing CA
- Digital signature

---

## 4. Public and Private Keys

PKI relies on key pairs:

### Public Key
- Shared publicly
- Used for encryption

### Private Key
- Kept secret
- Used for decryption

---

## 5. Certificate Revocation List (CRL)

A CRL contains certificates that are no longer trusted.

Reasons for revocation include:

- Compromised keys
- Expired certificates
- Unauthorized access

---

# How Certificates Work

## Certificate Process

1. Generate a public/private key pair
2. Create a Certificate Signing Request (CSR)
3. Submit the CSR to a CA
4. The CA validates identity
5. The CA issues and signs the certificate
6. Systems trust the certificate if they trust the CA

---

# Certificate Chain of Trust

Certificates are organized in a trust hierarchy.

```text
Root CA
   ↓
Intermediate CA
   ↓
Server/User Certificate