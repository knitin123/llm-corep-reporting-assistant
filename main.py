import os
from dotenv import load_dotenv
 
load_dotenv()

 
api_key = os.getenv("OPENAI_API_KEY")

 
if api_key:
    print(" Success! Your Python script found the API key.")
    print(f"Key starts with: {api_key[:8]}...") 
else:
    print("Script failed to find the key ")
