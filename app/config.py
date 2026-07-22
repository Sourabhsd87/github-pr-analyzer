import logging
import os
from dotenv import load_dotenv

import app.logging_config  # noqa: F401

logger = logging.getLogger(__name__)

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

missing_secrets = []

if not GITHUB_TOKEN:
    missing_secrets.append("GITHUB_TOKEN")

if not GEMINI_API_KEY:
    missing_secrets.append("GEMINI_API_KEY")

if missing_secrets:
    logger.critical(
        "Failed to load required secrets from environment: %s",
        ", ".join(missing_secrets),
    )
    raise RuntimeError(
        f"Failed to load required secrets from environment: {', '.join(missing_secrets)}"
    )

logger.info("All secrets loaded successfully")
