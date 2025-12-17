import os


def get_env():
    return os.environ.get("ENVIRONMENT", "dev")
