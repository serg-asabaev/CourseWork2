from abc import ABC, abstractmethod
from requests import get


class APIAdapterBase(ABC):

    @abstractmethod
    def get_aeroplanes(self, country: str):
        pass

    @abstractmethod
    def cast_to_object_list(self, aeroplanes):
        pass


class APIAdapter(APIAdapterBase):

    def __init__(self) -> None:
        self.openstreetmap_url = 'https://nominatim.openstreetmap.org/search'
        self.opensky_url = 'https://opensky-network.org/api/states/all?'
        self.aeroplanes = None

    def get_aeroplanes(self, country: str) -> None:
        #Headers с user-agent - обязательный параметр при запросе к nominatim.openstreetmap.
        #Вы можете использовать любое название вместо test-app/1.0, например просто test-app.
        headers_nominatim = {
            'User-Agent': 'test-app/1.0',
        }

        #Указываем параметры: в каком формате возвращать данные и максимальную длину списка стран в ответе.
        params_nominatim = {
            'country': country,
            'format': 'json',
            'limit': 1,
        }

        response = get(url=self.openstreetmap_url, params=params_nominatim, headers=headers_nominatim)

        data = response.json()

        #Пример ответа от nominatim.openstreetmap можно посмотреть в задании курсовой.
        geo_coordinates = data[0].get('boundingbox')

        #Параметры для фильтрации самолетов по их географическим координатам.
        params = {
            'lamin': geo_coordinates[0],
            'lamax': geo_coordinates[1],
            'lomin': geo_coordinates[2],
            'lomax': geo_coordinates[3],
        }

        response = get(url=self.opensky_url, params=params)

        #Пример ответа от opensky-network можно посмотреть в задании курсовой.
        self.aeroplanes = response.json()

        return response.json()

    def cast_to_object_list(self, aeroplanes):
        planes_object_list = []

        for plane in aeroplanes['states']:
            plane_info = {
                'plane_id': plane[0],
                'call_sign': plane[1],
                'plane_country': plane[2],
                'longitude': plane[5],
                'latitude': plane[6],
                'baro_altitude': plane[7],
                'on_ground': plane[8],
                'velocity': plane[9],
                'true_track': plane[10],
                'vertical_rate': plane[11]
            }
            planes_object_list.append(plane_info)

        return planes_object_list

# api = APIAdapter()
# api.get_aeroplanes('Azerbaijan')