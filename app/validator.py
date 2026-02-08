def validate_report(report):

    alerts = []

    for field in report["fields"]:
        if field["value"] == "MISSING":
            alerts.append(f"{field['field_name']} is missing.")

    return alerts
