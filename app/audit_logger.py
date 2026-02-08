def generate_audit_log(report):

    logs = []

    for field in report["fields"]:
        logs.append({
            "field": field["field_name"],
            "source": field["regulatory_source"]
        })

    return logs
