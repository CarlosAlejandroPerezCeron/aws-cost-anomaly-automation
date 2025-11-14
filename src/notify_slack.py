import os
import requests
from utils import log

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_slack_alert(service, cost, change_percent):
    message = {
        "text": f":warning: *AWS Cost Anomaly Detected!*\nService: `{service}`\nCost: `${cost}`\nChange: `{change_percent}%`"
    }

    response = requests.post(SLACK_WEBHOOK_URL, json=message)
    log(f"Slack alert sent: {response.status_code}")

if __name__ == "__main__":
    send_slack_alert("AmazonCloudFront", 2431.18, 80.5)
