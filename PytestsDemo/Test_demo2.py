import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstprogram(Setup):
    msg = "Hello"
    assert msg == "Hell", "Test failed because does not match"



def test_SecondCreditCard():
    a = 4
    b = 6
    assert a+2 ==6, "Addition does not match"





