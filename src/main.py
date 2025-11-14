from create_monitors import create_monitor
from audit_monitors import list_monitors
from notify_slack import send_slack_alert
from utils import log

def main():
    log("=== AWS Cost Anomaly Automation ===")

    # 1. Crear monitores base
    services = ["AmazonEC2", "AmazonS3"]
    for s in services:
        create_monitor(f"FinOpsMonitor-{s}")

    # 2. Auditar monitores existentes
    list_monitors()

    # 3. Notificación de prueba
    send_slack_alert("AmazonCloudFront", 2300, 70.2)

if __name__ == "__main__":
    main()
