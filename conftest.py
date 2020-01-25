
import pytest
from fixture.application import Application

# 1 fixture for all session (scope="session")
@pytest.fixture (scope = "session")
def app(request):
    fixture = Application()
    fixture. app.session.login(user="admin", password="secret")
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
