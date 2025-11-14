from utils import get_client, log
import os

def create_monitor(name, monitor_type="SERVICE", monitor_dimension="SERVICE"):
    client = get_client("ce")

    response = client.create_anomaly_monitor(
        AnomalyMonitorName=name,
        MonitorType=monitor_type,
        MonitorDimension=monitor_dimension
    )

    log(f"Monitor created: {response['AnomalyMonitorArn']}")
    return response

if __name__ == "__main__":
    prefix = os.getenv("MONITOR_PREFIX", "FinOps-Monitor")
    services = ["AmazonEC2", "AmazonS3", "AmazonCloudFront"]

    for service in services:
        monitor_name = f"{prefix}-{service}"
        create_monitor(monitor_name)
