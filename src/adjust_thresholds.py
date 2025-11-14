from utils import get_client, log
import os
import pandas as pd

def adjust_threshold(monitor_arn, new_threshold):
    client = get_client("ce")

    response = client.update_anomaly_subscription(
        SubscriptionArn=monitor_arn,
        Threshold=new_threshold
    )

    log(f"Threshold updated to {new_threshold}% for {monitor_arn}")
    return response

if __name__ == "__main__":
    # Simulación de ajuste basado en promedio histórico
    history = pd.Series([120, 130, 125, 200])
    variation = ((history.max() - history.mean()) / history.mean()) * 100

    if variation > 20:
        new_threshold = 25
    else:
        new_threshold = 15

    # Placeholder ARN de ejemplo
    adjust_threshold("arn:aws:ce::123456789012:AnomalySubscription/abc123", new_threshold)
