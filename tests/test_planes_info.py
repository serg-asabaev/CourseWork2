import pytest

from src.api_adapter import APIAdapter
from src.planes_info import PlanesInfo

@pytest.fixture
def planes_info_response():
    return {'time': 1776881711,
        'states': [
            ['e94c86', 'BOV709  ', 'Bolivia', 1776881450, 1776881522, -59.3583, -32.7539, 10363.2, False, 190.37, 344.16, 0,
             None, 10774.68, '0351', False, 0],
            ['aa7823', 'CAP847  ', 'United States', 1776881635, 1776881639, -81.7581, 27.5575, 845.82, False, 58.44, 189.63,
             -2.28, None, 891.54, '7014', False, 0],
            ['c00734', 'WJA2046 ', 'Canada', 1776881640, 1776881641, -92.4338, 42.0005, 10668, False, 243.77, 138.34, -0.33,
             None, 10919.46, '3320', False, 0]
        ]
    }


def test_init(planes_info_response):

    planes_info = PlanesInfo(planes_info_response)

    assert planes_info.time == 1776881711
    assert planes_info.states == [
            ['e94c86', 'BOV709  ', 'Bolivia', 1776881450, 1776881522, -59.3583, -32.7539, 10363.2, False, 190.37, 344.16, 0,
             None, 10774.68, '0351', False, 0],
            ['aa7823', 'CAP847  ', 'United States', 1776881635, 1776881639, -81.7581, 27.5575, 845.82, False, 58.44, 189.63,
             -2.28, None, 891.54, '7014', False, 0],
            ['c00734', 'WJA2046 ', 'Canada', 1776881640, 1776881641, -92.4338, 42.0005, 10668, False, 243.77, 138.34, -0.33,
             None, 10919.46, '3320', False, 0]
        ]


def test_get_current_plane(planes_info_response):
    planes_info = PlanesInfo(planes_info_response)

    assert planes_info.get_current_plane('e94c86') == ['e94c86', 'BOV709  ', 'Bolivia', 1776881450, 1776881522,
                                                        -59.3583, -32.7539, 10363.2, False, 190.37, 344.16, 0,
                                                         None, 10774.68, '0351', False, 0]


def test_get_current_plane_empty(planes_info_response):

    planes_info = PlanesInfo(planes_info_response)

    assert planes_info.get_current_plane('') == []


def test_top_planes_by_altitude(planes_info_response):

    api = APIAdapter()

    planes_info = PlanesInfo(planes_info_response)
    planes = api.cast_to_object_list(planes_info_response)

    count = 1

    assert planes_info.top_planes_by_altitude(count, planes) == [{
                                                                    'plane_id': 'c00734',
                                                                    'call_sign': 'WJA2046 ',
                                                                    'plane_country': 'Canada',
                                                                    'longitude': -92.4338,
                                                                    'latitude': 42.0005,
                                                                    'baro_altitude': 10668,
                                                                    'on_ground': False,
                                                                    'velocity': 243.77,
                                                                    'true_track': 138.34,
                                                                    'vertical_rate': -0.33
                                                                }]

def test_planes_by_country(planes_info_response):

    api = APIAdapter()

    planes_info = PlanesInfo(planes_info_response)
    planes = api.cast_to_object_list(planes_info_response)

    planes_by_country = [
        {
            'plane_id': 'c00734',
            'call_sign': 'WJA2046 ',
            'plane_country': 'Canada',
            'longitude': -92.4338,
            'latitude': 42.0005,
            'baro_altitude': 10668,
            'on_ground': False,
            'velocity': 243.77,
            'true_track': 138.34,
            'vertical_rate': -0.33
        }
    ]

    assert planes_info.planes_by_country('Canada', planes) == planes_by_country
