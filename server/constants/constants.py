import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV", "dev")

if ENV == "prod":
    LLAMA_URL = os.getenv("LLAMA_URL", "http://ollama:11434/api/generate")
else:
    LLAMA_URL = os.getenv("LLAMA_URL", "http://localhost:11434/api/generate")
