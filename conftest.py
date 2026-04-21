import pytest

from src.api_adapter import APIAdapter

@pytest.fixture
def result_api_adapter():
    api = APIAdapter()

    return api.get_aeroplanes('France')