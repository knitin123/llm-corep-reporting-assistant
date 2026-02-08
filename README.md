LLM-Assisted PRA COREP Reporting Assistant
Overview

This project demonstrates an end-to-end Retrieval-Augmented Generation (RAG) prototype designed to support regulatory reporting workflows under the PRA Rulebook.

The assistant retrieves relevant COREP regulatory instructions, generates structured reporting outputs aligned with the Own Funds (C01.00) template, validates required fields, and provides an audit trail for explainability.

Key Features

- Retrieval grounded in regulatory text
- Locally hosted LLM (Phi-3 via Ollama,no sufficient funds for open api)
- Structured JSON reporting output
- COREP template mapping
- Validation engine
- Audit trail for regulatory transparency
- Streamlit-based user interface

Architecture:
User Query → FAISS Retriever → Local LLM → Structured Output → Template Mapping → Validation → Audit Log

Installation
git clone <repo>
cd repo
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt


Install Ollama and pull model:
ollama run phi3:mini


Rebuild vector DB:
python app/ingest.py


Run application:
python -m streamlit run ui/streamlit_app.py
 
