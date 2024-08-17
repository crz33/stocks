import os


def get(key):
    v = os.environ.get(key)
    if v is None:
        raise RuntimeError(f"環境変数に {key} が定義されていない")
    return v


EDINET_KEY = get("EDINET_KEY")
