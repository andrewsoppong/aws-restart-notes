# 🤖 Lab 3.4 - Training a Machine Learning Model

## 📖 Lab Overview

In this lab, I used **Amazon SageMaker** to train a machine 
learning model on a biomechanical vertebral column dataset. 
I split the data into training, validation, and test sets, 
then trained an **XGBoost** classification model using 
SageMaker's built-in algorithm support.

---

## 🎯 Objectives

- [x] Split data into training, validation, and test datasets
- [x] Train an XGBoost model in Amazon SageMaker
- [x] Monitor training job progress and review results

---

## 🛠️ AWS Services Used

| Service | Purpose |
|---|---|
| Amazon SageMaker | Notebook instance and model training |
| Amazon S3 | Storage for training and validation data |
| JupyterLab | Interactive notebook environment |
| XGBoost Algorithm | Machine learning model training |

---

## 📋 Step-by-Step Summary

### Task 1: Open SageMaker Notebook
- Navigated to **Amazon SageMaker AI → Notebooks → 
Notebook instances**
- Opened **MyNotebook** in JupyterLab
- Selected **conda_python3** as the kernel

### Task 2: Open the Lab Notebook
- Opened `en_us/3_4-machinelearning.ipynb`
- Ran each cell sequentially using **Shift + Enter**

### Notebook Steps:

#### Step 1 — Load the Dataset
- Loaded the **biomechanical vertebral column dataset**
- Explored the features and target variable

#### Step 2 — Split the Data
- Split dataset into three parts:
  - **Training set** (~70%) — used to train the model
  - **Validation set** (~15%) — used during training 
  to tune performance
  - **Test set** (~15%) — used for final evaluation

#### Step 3 — Upload to S3
- Uploaded training and validation datasets to 
an **S3 bucket** for SageMaker access

#### Step 4 — Train XGBoost Model
- Configured the **XGBoost** built-in algorithm container
- Set training hyperparameters
- Launched and monitored the **SageMaker training job**
- Waited for training job to complete successfully ✅

#### Step 5 — Review Results
- Reviewed training and validation accuracy metrics
- Confirmed model trained without errors ✅

---

## 💡 Key Concepts Learned

- **Train/Validation/Test split** is essential to build 
models that generalize well to unseen data
- **Training set** teaches the model patterns
- **Validation set** helps tune the model during training 
and prevents overfitting
- **Test set** gives an unbiased evaluation of final 
model performance
- **XGBoost** (Extreme Gradient Boosting) is a powerful 
algorithm for classification and regression tasks
- **Amazon SageMaker** provides managed infrastructure 
for training ML models at scale
- **JupyterLab** is an interactive environment for 
running Python code and visualizing results
- Training jobs in SageMaker run on dedicated 
compute instances and store results in S3

---

## ✅ Lab Outcome

Successfully split the vertebral column dataset into training, 
validation, and test sets, uploaded them to S3, and trained 
an XGBoost classification model using Amazon SageMaker. 
The training job completed successfully with good accuracy 
on the validation set.

---

*Lab completed as part of the **AWS re/Start Program** — 
Cloud Practitioner track.*