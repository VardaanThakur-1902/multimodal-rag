from dotenv import load_dotenv
import os

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL")
CHAT_MODEL = os.getenv("CHAT_MODEL")
