from utils import get_client, log
import pandas as pd

def list_monitors():
    client = get_client("ce")
    monitors = []
    paginator = client.get_paginator("list_anomaly_monitors")

    for page in paginator.paginate():
        monitors.extend(page["AnomalyMonitors"])

    df = pd.DataFrame(monitors)
    df.to_csv("monitor_audit.csv", index=False)
    log(f"{len(monitors)} monitors exported to monitor_audit.csv")

if __name__ == "__main__":
    list_monitors()
