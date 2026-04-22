import pytest

from src.api_adapter import APIAdapter

@pytest.fixture
def result_api_adapter():
    api = APIAdapter()

    return api.get_aeroplanes('France')


@pytest.fixture
def planes_info_json():
    return [
        {
            "plane_id": "39de4f",
            "call_sign": "TVF3031 ",
            "plane_country": "France",
            "longitude": -5.4862,
            "latitude": 37.8827,
            "baro_altitude": 10957.56,
            "on_ground": False,
            "velocity": 243.89,
            "true_track": 25.75,
            "vertical_rate": 0.33
        },
    ]


@pytest.fixture
def plane_info_json():
    return {
            "plane_id": "39de4f",
            "call_sign": "TVF3031 ",
            "plane_country": "France",
            "longitude": -5.4862,
            "latitude": 37.8827,
            "baro_altitude": 10957.56,
            "on_ground": False,
            "velocity": 243.89,
            "true_track": 25.75,
            "vertical_rate": 0.33
        }