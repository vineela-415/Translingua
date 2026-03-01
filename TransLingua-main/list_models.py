import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# List available models
models = genai.list_models()

print("AVAILABLE MODELS FOR YOUR API KEY:\n")
for model in models:
    print(model.name, " | supports:", model.supported_generation_methods)
