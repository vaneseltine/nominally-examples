import pytest


@pytest.fixture(autouse=True)
def add_output_spacing():
    print("")
    yield
    print("")
