import logging

import app.logging_config  # noqa: F401

from app.vault_service import get_github_token
from app.vault_service import get_gemini_key

logger = logging.getLogger(__name__)

GITHUB_TOKEN = get_github_token()
GEMINI_API_KEY = get_gemini_key()

missing_secrets = []

if not GITHUB_TOKEN:
    missing_secrets.append("GITHUB_TOKEN")

if not GEMINI_API_KEY:
    missing_secrets.append("GEMINI_API_KEY")

if missing_secrets:
    logger.critical(
        "Failed to load required secrets from Vault: %s",
        ", ".join(missing_secrets),
    )
    raise RuntimeError(
        f"Failed to load required secrets from Vault: {', '.join(missing_secrets)}"
    )

logger.info("All secrets loaded successfully from Vault")
