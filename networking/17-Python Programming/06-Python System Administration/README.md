# Python for System Administration

## At the Core of the Lesson

You will learn how to:

- Define system administration
- Use Python functions to manage users
- Handle packages in Python code
- Use `os.system()` and `subprocess.run()` to run bash commands in Python

---

# What You Will Learn

In this module, you will learn how to:

- Define system administration
- Recognize how to manage users
- Recognize how to handle packages
- Recognize how to use `os.system()` and `subprocess.run()` to make complex decisions

---

# Introduction to System Administration

System administration involves managing and maintaining computer systems, servers, software, and users.

System administrators are responsible for:

- Managing user accounts
- Installing and updating software
- Monitoring systems
- Automating tasks
- Managing files and permissions
- Troubleshooting system problems

Python is widely used in system administration because it can automate repetitive tasks efficiently.

---

# Using Python Functions to Manage Users

Python functions can help automate user-management tasks.

Example:

```python id="tx0j5x"
def create_user(username):
    print(f"Creating user: {username}")

create_user("andrews")