import pytest
from app import app as myapp


@pytest.fixture()
def app():
    app = myapp
    app.debug = True
    return app
