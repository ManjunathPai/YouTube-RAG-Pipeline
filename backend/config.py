# stores config variables for the backend
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get configuration variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Embedding model for generating vector embeddings
EMBEDDING_MODEL = "text-embedding-3-small"

# LLM model for generating responses
LLM_MODEL = "gpt-3.5-turbo"