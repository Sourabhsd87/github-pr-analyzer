import logging

import hvac

logger = logging.getLogger(__name__)

VAULT_URL = "http://127.0.0.1:8200"

client = hvac.Client(
    url=VAULT_URL,
    token="root",
)

logger.debug("Vault client initialized (url=%s)", VAULT_URL)


def get_github_token():
    logger.debug("Reading GitHub token from Vault (path=github)")
    secret = client.secrets.kv.v2.read_secret_version(
        path="github",
        mount_point="secret",
    )
    token = secret["data"]["data"]["token"]
    logger.info("GitHub token loaded from Vault")
    return token


def get_gemini_key():
    logger.debug("Reading Gemini API key from Vault (path=gemini)")
    secret = client.secrets.kv.v2.read_secret_version(
        path="gemini",
        mount_point="secret",
    )
    api_key = secret["data"]["data"]["api_key"]
    logger.info("Gemini API key loaded from Vault")
    return api_key
