import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.reporting_assistant import generate_corep_report

st.title(" LLM-Assisted PRA COREP Reporting Assistant")

st.write("""
Prototype demonstrating retrieval-augmented regulatory reporting
for COREP Own Funds (C01.00).
""")

question = st.text_area(
    "Enter Regulatory Question / Scenario:",
    "Does Additional Tier 1 qualify as own funds?"
)

if st.button("Generate COREP Report"):

    with st.spinner("Analyzing regulatory text..."):

        report_json, template_df, validation_alerts, audit_log = generate_corep_report(question)

        st.subheader(" Structured JSON Output")
        st.json(report_json)

        st.subheader("Template ")
        st.dataframe(template_df)

        st.subheader(" Validation Alerts")
        if validation_alerts:
            for alert in validation_alerts:
                st.warning(alert)
        else:
            st.success("No validation issues detected.")

        st.subheader(" Audit Trail")
        st.write(audit_log)
