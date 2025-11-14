import os
import requests
from utils import log

TEAMS_WEBHOOK_URL = os.getenv("TEAMS_WEBHOOK_URL")

def send_teams_alert(service, cost, change_percent):
    message = {
        "@type": "MessageCard",
        "@context": "https://schema.org/extensions",
        "summary": "AWS Cost Anomaly Detected",
        "themeColor": "EA4300",
        "sections": [{
            "activityTitle": f"🚨 AWS Cost Anomaly Detected: {service}",
            "facts": [
                {"name": "Cost", "value": f"${cost}"},
                {"name": "Change", "value": f"{change_percent}%"},
            ],
        }]
    }
    response = requests.post(TEAMS_WEBHOOK_URL, json=message)
    log(f"Teams alert sent: {response.status_code}")

if __name__ == "__main__":
    send_teams_alert("AmazonS3", 312.42, 25.6)
