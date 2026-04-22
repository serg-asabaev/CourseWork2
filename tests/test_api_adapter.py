import pytest
import responses
from src.api_adapter import APIAdapter  # ← замените на ваш модуль


# ========== ТЕСТ 1: Успешный ответ ==========
@responses.activate
def test_get_geo_coords_success():

    mock_data = [{
        "place_id": 287456789,
        "boundingbox": ["47.27", "55.09", "5.86", "15.04"],
        "lat": "51.16",
        "lon": "10.45",
        "display_name": "Deutschland"
    }]

    # Мокаем запрос к nominatim
    responses.add(
        responses.GET,
        'https://nominatim.openstreetmap.org/search',
        json=mock_data,
        status=200,
        headers={'Content-Type': 'application/json'}
    )

    # Вызов метода
    adapter = APIAdapter()
    result = adapter.get_geo_coords('Germany')

    # Проверки
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]['display_name'] == 'Deutschland'
    assert result[0]['boundingbox'] == ["47.27", "55.09", "5.86", "15.04"]

    # Проверка запроса
    assert len(responses.calls) == 1
    assert 'country=Germany' in responses.calls[0].request.url
    assert responses.calls[0].request.headers['User-Agent'] == 'test-app/1.0'

@responses.activate
def test_get_geo_coords_connection_error():

    responses.add(
        responses.GET,
        'https://nominatim.openstreetmap.org/search',
        status=503,
        body='Service Unavailable'
    )

    adapter = APIAdapter()

    with pytest.raises(ConnectionError, match='Ответ не получен!'):
        adapter.get_geo_coords('InvalidCountry')


@responses.activate
def test_get_geo_coords_empty():
    """Тест: обработка пустого списка в ответе"""

    responses.add(
        responses.GET,
        'https://nominatim.openstreetmap.org/search',
        json=[],
        status=200
    )

    adapter = APIAdapter()
    result = adapter.get_geo_coords('NowhereLand')

    assert result == []
    assert isinstance(result, list)


@responses.activate
def test_get_geo_coords_request_params():
    """Тест: проверка параметров и заголовков запроса"""

    responses.add(
        responses.GET,
        'https://nominatim.openstreetmap.org/search',
        json=[{'boundingbox': ['0', '1', '0', '1']}],
        status=200
    )

    adapter = APIAdapter()
    adapter.get_geo_coords('France')

    call = responses.calls[0]

    # Проверка параметров
    assert 'country=France' in call.request.url
    assert 'format=json' in call.request.url
    assert 'limit=1' in call.request.url

    # Проверка заголовка
    assert call.request.headers['User-Agent'] == 'test-app/1.0'