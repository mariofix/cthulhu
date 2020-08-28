from dataclasses import dataclass
import os


@dataclass
class Config:
    SECRET_KEY: str = b"\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G.)\xaf"
    SERVER_NAME: str = "localhost:9000"
    SESSION_COOKIE_NAME: str = "cthulhu"
    EXPLAIN_TEMPLATE_LOADING: bool = False
    BASE_DIR: str = os.path.abspath(os.path.dirname(__file__))
    REGISTER_CORE = True

    @staticmethod
    def init_app(app):
        pass


@dataclass
class DevConfig(Config):
    URL: str = f"https://dev.mariofix.com"
    SESSION_COOKIE_SECURE: bool = False
    REMEMBER_COOKIE_SECURE: bool = False
    EXPLAIN_TEMPLATE_LOADING: bool = True


@dataclass
class TestConfig(Config):
    URL: str = f"https://dev.mariofix.com"
    SESSION_COOKIE_SECURE: bool = False
    REMEMBER_COOKIE_SECURE: bool = False
    EXPLAIN_TEMPLATE_LOADING: bool = True
    TESTING: bool = True
    SERVER_NAME: str = "localhost.localdomain:9000"


@dataclass
class ProdConfig(Config):
    URL: str = f"https://mariofix.com"
    SESSION_COOKIE_SECURE: bool = True
    REMEMBER_COOKIE_SECURE: bool = True
    EXPLAIN_TEMPLATE_LOADING: bool = False


config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig,
    'default': DevConfig
}
