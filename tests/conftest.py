import pytest
from flask_skeleton import create_app
from config import config


@pytest.fixture(scope='module')
def TestClient():
    test_app = create_app(config['testing'])
    test_client = test_app.test_client()
    ctx = test_app.app_context()
    ctx.push()
    yield test_client
    ctx.pop()
