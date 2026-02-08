from app.retriever import get_retriever

retriever = get_retriever()

query = "What qualifies as Common Equity Tier 1 capital?"

docs = retriever.invoke(query)

print("\n🔎 TOP MATCHES:\n")

for i, doc in enumerate(docs, 1):
    print(f"\nRESULT {i}")
    print("-" * 40)
    print(doc.page_content[:500])  # show first 500 chars
