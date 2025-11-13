import boto3
import os
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

def get_client(service_name):
    return boto3.client(service_name, region_name=AWS_REGION)

def log(message):
    print(f"[INFO] {message}")
