from src.api_adapter import APIAdapter
from src.json_saver import JSONSaver
from src.plane import Plane
from src.planes_info import PlanesInfo

api = APIAdapter()
json_saver = JSONSaver('data/planes_info.json')

def user_interaction():
    """Функция для взаимодействия с пользователем"""

    # Получение списка самолетов надо указанной страной
    country = input('Введите название страны (на английском): ')

    planes = api.get_aeroplanes(country)
    planes_info = PlanesInfo(planes)
    planes = api.cast_to_object_list(planes)

    # Получение топ N самолетов по высоте полета
    planes_count = int(input('Введите количество самолетов с наибольшей высотой полета: '))

    top_planes = planes_info.top_planes_by_altitude(planes_count, planes)

    # Получение самолетов по стране регистрации
    planes_country = input('Введите страну регистрации самолета (на английском): ')

    planes_by_country = planes_info.planes_by_country(planes_country, planes)


    # print(top_planes)
    #
    # json_saver.save_list_to_file(planes)
    #
    # plane1 = Plane('39de4f1', 'TVF3422', 'France', 6.7779, 48.0356, 10000
    #                , False, 854, 10.045, 0)
    #
    # plane2 = Plane('39de4f2', 'TVF3423', 'France', -15.15398, 155.0356, 8000
    #                , False, 852, 10.045, 0)
    #
    # json_saver.add_plane(plane1)
    #
    # json_saver.delete_plane('39de4f1')
    # print(plane1 < plane2)


if __name__ == '__main__':
    user_interaction()

    # plane1 = Plane('39de4f', 'TVF3422', 'France',  6.7779, 48.0356)

    # print(plane1)