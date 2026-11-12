# ☁️ Automated CSV Backup and Cloud Storage System

<p align="center">
  A simple Python + AWS project that automates CSV validation, local backup creation, and secure cloud storage using Amazon S3.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS-Amazon%20S3-orange?logo=amazonaws&logoColor=white" />
  <img src="https://img.shields.io/badge/Library-Boto3-yellow" />
  <img src="https://img.shields.io/badge/Status-Completed-success" />
</p>

---

## 📌 About the Project

The **Automated CSV Backup and Cloud Storage System** is a Python-based mini project designed to simplify and automate CSV data backup.

The application reads transaction records from a local CSV file, validates the data, generates a timestamped backup, and uploads the backup file to an Amazon S3 bucket.

It demonstrates how Python can interact with AWS cloud storage to create a simple and reliable backup workflow.

## ✨ Features

- 📄 **CSV Reading** – Reads transaction data from a local CSV file.
- 🔍 **Data Validation** – Checks required columns and empty values.
- 💰 **Amount Validation** – Ensures transaction amounts are numeric and non-negative.
- 🕒 **Timestamped Backups** – Creates uniquely named backup files.
- 💻 **Local Storage** – Keeps a copy of the generated backup locally.
- ☁️ **Cloud Upload** – Uploads backup files to Amazon S3.
- 🛡️ **Error Handling** – Handles file, validation, and AWS errors.
- 📋 **Status Messages** – Displays progress throughout the backup process.

## ⚙️ How It Works

```text
       ┌─────────────────────┐
       │   transactions.csv  │
       └──────────┬──────────┘
                  │
                  ▼
       ┌─────────────────────┐
       │   Read CSV Data     │
       └──────────┬──────────┘
                  │
                  ▼
       ┌─────────────────────┐
       │   Validate Records  │
       └──────────┬──────────┘
                  │
                  ▼
       ┌─────────────────────┐
       │ Create Local Backup │
       │   + Timestamp       │
       └──────────┬──────────┘
                  │
                  ▼
       ┌─────────────────────┐
       │   Upload to AWS S3  │
       └──────────┬──────────┘
                  │
                  ▼
       ┌─────────────────────┐
       │  Backup Completed   │
       └─────────────────────┘
```

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Boto3 | AWS SDK for Python |
| Amazon S3 | Cloud backup storage |
| CSV Module | Reading and writing CSV files |
| Datetime | Generating timestamps |
| OS Module | File and directory operations |

## 📂 Project Structure

```text
CSV-Cloud-Backup/
│
├── main.py
│   └── Main application logic
│
├── transactions.csv
│   └── Sample transaction data
│
├── backup_YYYY-MM-DD_HH-MM-SS.csv
│   └── Generated local backup
│
└── README.md
    └── Project documentation
```

## 🚀 Getting Started

### 1. Prerequisites

Make sure you have:

- Python 3.x
- An AWS account
- An Amazon S3 bucket
- AWS CLI installed and configured

### 2. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

```bash
cd CSV-Cloud-Backup
```

### 3. Install Dependencies

```bash
py -m pip install boto3
```

### 4. Configure AWS Credentials

Configure your AWS credentials using:

```bash
aws configure
```

Enter your AWS access key, secret key, default region, and output format when prompted.

**Security note:** Never upload AWS credentials, secret keys, or `.aws` configuration files to GitHub.

### 5. Configure Amazon S3

Update the following settings in `main.py`:

```python
BUCKET_NAME = "projectsm"
REGION = "ap-south-1"
```

Use your own bucket name and region if running the project with a different AWS account.

### 6. Run the Application

```bash
py main.py
```

## 📊 Sample Input

**transactions.csv**

```csv
Transaction_ID,Customer_Name,Amount,Status
T101,Arun,5000,Success
T102,Priya,2500,Success
T103,Rahul,7000,Pending
T104,Divya,1500,Success
T105,Karthik,3000,Failed
```

## 💻 Expected Output

```text
================================
     CSV CLOUD BACKUP SYSTEM
================================

Reading CSV file...
File successfully loaded.

Validating records...
All records are valid.

Creating backup file...
Backup file created successfully!

Connecting to Amazon S3...
Connection successful.

Uploading file...
Upload successful!

================================
       BACKUP COMPLETED
================================
```

## ☁️ AWS S3 Storage

The generated backup file is uploaded to the configured Amazon S3 bucket.

**AWS Configuration:**

- Bucket: `projectsm`
- Region: `ap-south-1` (Mumbai)
- Storage: Amazon Simple Storage Service (S3)

The bucket should remain private, with public access blocked and only the required IAM permissions granted.

## 🔐 Data Validation Rules

The application checks:

- Required columns: `Transaction_ID`, `Customer_Name`, `Amount`, `Status`
- Required fields must not be empty.
- Transaction amounts must be valid numeric values.
- Negative transaction amounts are rejected.

## 🔮 Future Improvements

- Duplicate transaction ID detection.
- Transaction status validation.
- More detailed validation reports.
- Improved backup recovery mechanisms.
- Automated scheduling using Windows Task Scheduler.
- Email notifications after successful uploads.
- Encryption and additional backup security.

## 🎯 Learning Outcomes

Through this project, I explored:

- Python file handling and CSV processing.
- Data validation and exception handling.
- Working with AWS services using Boto3.
- Uploading files to Amazon S3.
- Basic cloud storage and backup automation.
- AWS IAM permissions and credential configuration.

## 🏁 Conclusion

This project demonstrates a practical application of Python and AWS integration for automated data backup. By combining CSV validation, timestamped local backups, and Amazon S3 cloud storage, it provides a beginner-friendly introduction to cloud automation.

---

<p align="center">
  <b>Built with Python 🐍 and Amazon Web Services ☁️</b>
  <br/>
  <i>Learning Python, Exploring Cloud, Building Projects.</i>
</p>
