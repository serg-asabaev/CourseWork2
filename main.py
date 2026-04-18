from src.api_adapter import APIAdapter
from src.json_saver import JSONSaver
from src.plane import Plane
from src.planes_info import PlanesInfo

api = APIAdapter()
json_saver = JSONSaver()

def user_interaction():
    country = input('Введите название страны: ')

    planes_info = api.get_aeroplanes(country)
    planes_info = api.cast_to_object_list(planes_info)

    json_saver.save_list_to_file(planes_info, 'data/planes_info.json')

    plane1 = Plane('39de4f1', 'TVF3422', 'France', 6.7779, 48.0356)

    plane1.on_ground = False
    plane1.baro_altitude = 10000
    plane1.true_track = 10.045
    plane1.velocity = 854
    plane1.vertical_rate = 0

    json_saver.add_plane('data/planes_info.json', plane1)

    json_saver.delete_plane('data/planes_info.json', '39de4f1')


if __name__ == '__main__':
    user_interaction()

    # plane1 = Plane('39de4f', 'TVF3422', 'France',  6.7779, 48.0356)

    # print(plane1)