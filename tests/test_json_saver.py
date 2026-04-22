from unittest.mock import patch, mock_open


from src.json_saver import JSONSaver
from src.plane import Plane


@patch('src.json_saver.open', new_callable=mock_open)
@patch('src.json_saver.json.load')
def test_read_from_file(mock_json_load, mock_file, planes_info_json):

    mock_json_load.return_value = planes_info_json

    json_saver = JSONSaver('data/planes_info.json')

    result = json_saver.read_from_file()

    assert result == planes_info_json
    mock_file.assert_called_once_with('data/planes_info.json', 'r', encoding='utf-8')
    mock_json_load.assert_called_once()


def test_save_list_to_file(planes_info_json):

    with patch('src.json_saver.open', mock_open()) as mock_file:
        with patch('src.json_saver.json.dump') as mock_json:
            writer = JSONSaver('data/planes_info.json')
            result = writer.save_list_to_file(planes_info_json)

            assert result is True
            mock_file.assert_called_once_with('data/planes_info.json', 'w', encoding='utf-8')
            mock_json.assert_called_once()

            call_args = mock_json.call_args
            assert call_args[0][0] == planes_info_json  # Первый аргумент - данные

@patch('src.json_saver.os.path.exists')
@patch('src.json_saver.open', new_callable=mock_open)
@patch('src.json_saver.json.load')
@patch('src.json_saver.json.dump')
def test_add_plane( mock_json_dump, mock_json_load, mock_file, mock_exists):
    mock_exists.return_value = True

    plane = Plane( "39de4w","TVF3031 ","France", -5.4862,37.8827,10957.56,
            False,243.89,25.75,0.33)
    existing_data = [
        {
            "plane_id": "39de4f1",
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
    mock_json_load.return_value = existing_data


    json_saver = JSONSaver('data/planes_info.json')
    result = json_saver.add_plane(plane)

    assert result is True
    mock_json_load.assert_called_once()
    mock_json_dump.assert_called_once()

    written_data = mock_json_dump.call_args[0][0]
    print(written_data)
    assert len(written_data) == 2
    assert written_data[1] == {
            "plane_id": "39de4w",
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


