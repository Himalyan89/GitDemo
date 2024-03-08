import pytest


@pytest.mark.usefixtures("dataload")

class  TestExample:
    def test_editProfile(self, dataload):
        print(dataload[0])
        print(dataload[1])
        print(dataload[2])
