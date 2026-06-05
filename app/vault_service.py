import hvac

client = hvac.Client(
    url="http://127.0.0.1:8200",
    token="root"
)


def get_github_token():
    secret = client.secrets.kv.v2.read_secret_version(
        path="github",
        mount_point="secret"
    )

    return secret["data"]["data"]["token"]


def get_gemini_key():
    secret = client.secrets.kv.v2.read_secret_version(
        path="gemini",
        mount_point="secret"
    )

    return secret["data"]["data"]["api_key"]