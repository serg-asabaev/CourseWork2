class PlanesInfo:
    """Класс для работы со списком самолетов"""

    def __init__(self, planes_info_response):
        self.time = planes_info_response["time"]
        self.states = planes_info_response["states"]

    def get_current_plane(self, icao24):
        """Получение данных по самолету из списка самолетов"""

        if len(icao24) == 0:
            return []

        res_plane = []

        for plane in self.states:
            if plane[0] == icao24:
                res_plane = plane

        return res_plane

    @staticmethod
    def top_planes_by_altitude(count: int, planes_list: list[dict]) -> list[dict]:
        """Получение топ N самолетов по высоте"""

        result = []

        for plane in planes_list:
            if plane["baro_altitude"] is None:
                plane["baro_altitude"] = 0

        sorted_list = sorted(
            planes_list, key=lambda x: x["baro_altitude"], reverse=True
        )

        for plane in sorted_list[:count]:
            result.append(plane)
            print(
                f'Борт № {plane["plane_id"]}, высота {plane["baro_altitude"]} метров.'
            )

        return result

    @staticmethod
    def planes_by_country(country: str, planes: list[dict]) -> list[dict]:
        """Получение самолетов по стране регистрации"""

        if len(planes) == 0:
            return []

        result = []

        for plane in planes:
            if plane["plane_country"] == country:
                result.append(plane)
                print(f'Борт № {plane["plane_id"]}.')

        return result
