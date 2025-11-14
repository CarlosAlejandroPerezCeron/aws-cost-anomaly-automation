# AWS Cost Anomaly Detection Automation – Flow

1. Create Monitors
   - Each AWS service or linked account gets a dedicated anomaly monitor.
2. Adjust Thresholds
   - Python script calculates historical deviation and adjusts sensitivity.
3. Audit Monitors
   - Exports CSV audit log for transparency and FinOps governance.
4. Notify Slack/Teams
   - Sends structured messages to FinOps channels for triage.
5. Visualize in QuickSight
   - Dashboards for long-term trend and anomaly validation.


