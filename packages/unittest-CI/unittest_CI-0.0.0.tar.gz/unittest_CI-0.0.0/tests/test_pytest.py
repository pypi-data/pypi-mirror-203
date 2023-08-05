import pytest


def test_pass():
    assert True

@pytest.mark.skip(reason="This test is expected to fail")
def test_failure():
    assert False
