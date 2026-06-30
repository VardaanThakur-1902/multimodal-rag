from pathlib import Path

from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

OLLAMA_URL = os.getenv("OLLAMA_URL")

CHAT_MODEL = os.getenv("CHAT_MODEL")

EMBED_MODEL = os.getenv("EMBED_MODEL")

DATABASE_URL = os.getenv("DATABASE_URL")

UPLOAD_DIR = BASE_DIR / os.getenv("UPLOAD_DIR", "uploads")

MAX_FILE_SIZE = int(
    os.getenv("MAX_FILE_SIZE", 52428800)
)