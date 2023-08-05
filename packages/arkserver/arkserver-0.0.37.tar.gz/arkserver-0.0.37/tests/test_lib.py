from lib import get_host, get_port, get_root


def test_root():
    root = get_root()
    assert root is not None
    assert root.name == 'src'


def test_get_host():
    assert get_host() is not None


def test_get_port():
    assert get_port() is not None

