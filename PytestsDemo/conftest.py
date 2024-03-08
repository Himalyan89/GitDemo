import pytest


@pytest.fixture(scope = "class")
def Setup():
    print("I will execute first")
    yield
    print("I will be executing last")

@pytest.fixture()
def dataload():
    print("User profile data is being created")
    return("Abhi", "Himalyan", "abhishek.com")


@pytest.fixture(params=[("Chrome", "Abhi","shek","Himalyan"), ("Firefox", "Thakur"), "IE"])
def crossBrowser(request):
    return request.param
