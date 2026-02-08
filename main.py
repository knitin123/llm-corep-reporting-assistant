import os
from dotenv import load_dotenv

# 1. Load the variables from the .env file
load_dotenv()

# 2. Grab the key using os.getenv
# Make sure the name inside " " matches exactly what you wrote in .env
api_key = os.getenv("OPENAI_API_KEY")

# 3. Test it
if api_key:
    print("✅ Success! Your Python script found the API key.")
    print(f"Key starts with: {api_key[:8]}...") 
else:
    print("❌ Script failed to find the key. Check your .env file name and content.")