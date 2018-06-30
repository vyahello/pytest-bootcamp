from chapter_three.checks import ping_host


def test_ping_host(host: str) -> None:
    assert ping_host(host) == 0
