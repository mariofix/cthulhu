from config import Config, DevConfig, ProdConfig


def test_base_config():
    c = Config()
    assert c.SECRET_KEY is not None
    assert c.SERVER_NAME is not None
    assert c.REGISTER_CORE


def test_dev_config():
    c = DevConfig()
    assert c.URL is not None
    assert c.SESSION_COOKIE_SECURE is False
    assert c.REMEMBER_COOKIE_SECURE is False


def test_prod_config():
    c = ProdConfig()
    assert c.URL is not None
    assert c.SESSION_COOKIE_SECURE is True
    assert c.REMEMBER_COOKIE_SECURE is True
