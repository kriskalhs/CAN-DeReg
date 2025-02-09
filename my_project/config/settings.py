import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Web crawling settings
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
MAX_DEPTH = 2  # Max depth for crawling

# LLM settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Data storage
RAW_DATA_PATH = "data/raw/"
PROCESSED_DATA_PATH = "data/processed/"
