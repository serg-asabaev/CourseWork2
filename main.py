from src.api_adapter import APIAdapter
from src.json_saver import JSONSaver
from src.plane import Plane
from src.planes_info import PlanesInfo
from src.utils import get_time_greeting

api = APIAdapter()
json_saver = JSONSaver('data/planes_info.json')

def user_interaction():
    """Функция для взаимодействия с пользователем"""

    # Общая структура работы приложения
    # 1. Приветствие
    print(get_time_greeting())

    # 2. Запрашиваем страну и получаем список самолетов
    country = input('Введите название страны (на английском): ')

    planes = api.get_aeroplanes(country)
    planes_info = PlanesInfo(planes)
    planes = api.cast_to_object_list(planes)

    # 3. По ответу пользователя сохраняем данные в файл
    user_save_answer = input('Сохранить данные в файл?(да/нет) ')

    if user_save_answer.lower() == 'да':
        json_saver.save_list_to_file(planes)

    # 4. Получение топ N самолетов по высоте полета
    planes_count = int(input('Введите количество самолетов с наибольшей высотой полета: '))

    top_altitude_planes = planes_info.top_planes_by_altitude(planes_count, planes)

    # 5. Получение списка самолетов
    planes_country = input('Введите страну регистрации самолета (на английском): ')

    planes_by_country = planes_info.planes_by_country(planes_country, planes)

    # 6. Добавление самолета в список
    plane_is_add = input('Хотите добавить самолет в список?(да/нет) ')

    if plane_is_add.lower() == 'да':
        plane_id = input('Введите код самолета в системе ICAO24: ')
        plane_call_sign = input('Введите позывной рейса: ')
        plane_country = input('Введите страну регистрации самолета: ')
        plane_longitude = input('Введите координату долготы: ')
        plane_latitude = input('Введите координату широты: ')
        plane_baro_altitude = float(input('Введите высоту полета: '))
        plane_on_ground_str = input('Самолет на земле?(да/нет)')
        if plane_on_ground_str.lower() == 'да':
            plane_on_ground = True
        else:
            plane_on_ground = False
        plane_velocity = float(input('Введите горизонтальную скорость: '))
        plane_true_track = float(input('Введите курс самолета: '))
        plane_vertical_rate = float(input('Введите скорость подъема/снижения самолета: '))

        plane_1 = Plane(plane_id, plane_call_sign, plane_country, plane_longitude, plane_latitude, plane_baro_altitude,
                      plane_on_ground, plane_velocity, plane_true_track, plane_vertical_rate)

        json_saver.add_plane(plane_1)

    print('До свидания!')

if __name__ == '__main__':
    user_interaction()
