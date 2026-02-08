import json
from app.llm_engine import ask_regulatory_question
from app.template_mapper import map_to_template
from app.validator import validate_report
from app.audit_logger import generate_audit_log


def generate_corep_report(question):

     
    response = ask_regulatory_question(question)

    print("\n===== RAW LLM RESPONSE =====\n")
    print(response)

 
    try:
        report_json = json.loads(response)

    except json.JSONDecodeError:

        print(" Model returned invalid JSON. Attempting auto-fix...")

        start = response.find("{")
        end = response.rfind("}") + 1

        if start == -1 or end == -1:
            raise ValueError("LLM did not return JSON  .")

        cleaned = response[start:end]

        report_json = json.loads(cleaned)

 
    template_df = map_to_template(report_json)

    validation_alerts = validate_report(report_json)

    audit_log = generate_audit_log(report_json)

    return report_json, template_df, validation_alerts, audit_log
