import pandas as pd

def map_to_template(report_json):

    rows = []

    for field in report_json["fields"]:
        rows.append({
            "COREP Field": field["field_name"],
            "Reported Value": field["value"],
            "Treatment": field["treatment"]
        })

    df = pd.DataFrame(rows)

    return df
