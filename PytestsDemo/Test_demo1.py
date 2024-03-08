# Any pytest file should start with test_ or end with _test
# Any pytest method should start with test_
# Any code should be wrapped in method only
# Method Name should have sense(i.e test case name)
#-k stand for method names execution, -s for logs in outout, -v stand for more meta data
#You can run specific file with py.test<file name>
#You can mark (tag) tests (@pytest.mark.smoke) and then run with -m
#you can skip the test wit @pytest.mark.skip
#@pytest.mark.xfail -
#fixture are used to setup and teardown methods for test cases.
#conftest file is to generalize the fixture make it avilable for all the test cases.
#fixture also help to load the data for test case.


import pytest


def test_firstProgram():
    print("Hello")


@pytest.mark.xfail
def test_SecondCreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])