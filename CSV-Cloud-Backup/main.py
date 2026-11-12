import boto3
import csv
import os
import sys
import math
from decimal import Decimal, InvalidOperation
from datetime import datetime
from botocore.exceptions import ClientError, BotoCoreError
BUCKET_NAME = "projectsm2507"
REGION = "ap-south-1"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(BASE_DIR, "transactions.csv")
ALLOWED_STATUSES = {"Success", "Pending", "Failed"}
def read_csv(filename):
    print("\nReading CSV file...")
    if not os.path.exists(filename):
        raise FileNotFoundError("CSV file not found!")
    with open(filename, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames:
            raise ValueError("CSV file has no header!")
        records = list(reader)
    print("File successfully loaded.")
    return records
def validate_records(records):
    print("\nValidating records...")
    if not records:
        print("Error: CSV file is empty!")
        return False
    required_fields = [
        "Transaction_ID",
        "Customer_Name",
        "Amount",
        "Status"
    ]
    errors = []
    for field in required_fields:
        if field not in records[0]:
            errors.append(f"Missing column: {field}")
    if errors:
        for error in errors:
            print(error)
        return False
    transaction_ids = set()
    for row_number, record in enumerate(records, start=2):
        for field in required_fields:
            value = record.get(field)
            if value is None or not value.strip():
                errors.append(
                    f"Row {row_number}: {field} is empty."
                )
        transaction_id = record["Transaction_ID"].strip()
        if transaction_id:
            if transaction_id in transaction_ids:
                errors.append(
                    f"Row {row_number}: Duplicate Transaction_ID "
                    f"'{transaction_id}'."
                )
            transaction_ids.add(transaction_id)
        try:
            amount = Decimal(record["Amount"].strip())
            if not amount.is_finite():
                errors.append(
                    f"Row {row_number}: Amount must be a finite number."
                )
            elif amount < 0:
                errors.append(
                    f"Row {row_number}: Negative amount is not allowed."
                )
        except (InvalidOperation, ValueError):
            errors.append(
                f"Row {row_number}: Invalid transaction amount."
            )
        status = record["Status"].strip()
        if status and status not in ALLOWED_STATUSES:
            errors.append(
                f"Row {row_number}: Invalid status '{status}'. "
                f"Allowed values: {', '.join(sorted(ALLOWED_STATUSES))}."
            )
    if errors:
        print("\nValidation failed!")
        for error in errors:
            print("-", error)
        return False
    print("All records are valid.")
    return True
def create_backup(records):
    print("\nCreating backup file...")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
    filename = f"backup_{timestamp}.csv"
    backup_path = os.path.join(BASE_DIR, filename)
    fieldnames = list(records[0].keys()) + ["Backup_Timestamp"]
    with open(backup_path, "x", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            row = record.copy()
            row["Backup_Timestamp"] = timestamp
            writer.writerow(row)
    print("Backup file created successfully!")
    print("Backup filename:", filename)
    return backup_path
def upload_to_s3(filename):
    print("\nConnecting to Amazon S3...")
    try:
        s3 = boto3.client(
            "s3",
            region_name=REGION
        )
        s3.head_bucket(Bucket=BUCKET_NAME)
        print("Connection successful.")
        print("\nUploading file...")
        s3_filename = os.path.basename(filename)
        s3.upload_file(
            filename,
            BUCKET_NAME,
            s3_filename
        )
        print("Upload successful!")
        print("S3 Bucket:", BUCKET_NAME)
        print("Uploaded File:", s3_filename)
        return True
    except ClientError as e:
        print("AWS S3 Error:", e)
        return False
    except BotoCoreError as e:
        print("AWS Connection Error:", e)
        return False
if __name__ == "__main__":
    try:
        records = read_csv(INPUT_FILE)
        print("Total records:", len(records))
        if not validate_records(records):
            sys.exit(1)
        backup_file = create_backup(records)
        print("\nBackup created:", backup_file)
        upload_success = upload_to_s3(backup_file)
        if upload_success:
            print("\nCloud backup completed successfully!")
        else:
            print("\nLocal backup created, but S3 upload failed.")
    except FileNotFoundError as e:
        print("Error:", e)
        sys.exit(1)
    except ValueError as e:
        print("CSV Error:", e)
        sys.exit(1)
    except (OSError, csv.Error) as e:
        print("File processing error:", e)
        sys.exit(1)