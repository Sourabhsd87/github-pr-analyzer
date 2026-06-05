# from dotenv import load_dotenv
# import os

# load_dotenv()

# GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
# # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

from app.vault_service import get_github_token
from app.vault_service import get_gemini_key

GITHUB_TOKEN = get_github_token()
GEMINI_API_KEY = get_gemini_key()


missing_secrets = []

if not GITHUB_TOKEN:
    missing_secrets.append("GITHUB_TOKEN")

if not GEMINI_API_KEY:
    missing_secrets.append("GEMINI_API_KEY")

if missing_secrets:
    raise RuntimeError(
        f"Failed to load required secrets from Vault: {', '.join(missing_secrets)}"
    )

print("✓ All secrets loaded successfully from Vault")
    