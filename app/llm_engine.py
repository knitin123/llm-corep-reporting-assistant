from langchain_ollama import ChatOllama
from app.retriever import get_retriever


# Load Local Model
llm = ChatOllama(
    model="phi3:mini",
    temperature=0,
    num_ctx=2048
)


retriever = get_retriever()


def ask_regulatory_question(question):

    docs = retriever.invoke(question)

    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
You are a regulatory reporting assistant.

You MUST return ONLY valid JSON.

DO NOT write explanations.
DO NOT write markdown.
DO NOT write text before or after JSON.

Return STRICT JSON ONLY.
Your entire response must begin with {{ and end with }}.


Example format:

{{
 "template": "C01.00 Own Funds",
 "fields":[
   {{
     "field_name":"Common Equity Tier 1",
     "value":"Eligible",
     "treatment":"Included in Tier 1",
     "regulatory_source":"Article 50 CRR",
     "confidence":"High"
   }}
 ]
}}

You are generating machine-readable output for an automated regulatory system. 

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content
