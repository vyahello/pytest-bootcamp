import os


def ping_host(host: str) -> int:
    return os.system(f"ping {host} -c 1")
