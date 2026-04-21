
class Plane:
    """Класс для работы с конкретным самолетом"""

    __slots__ = ('plane_id', 'call_sign', 'country', 'longitude', 'latitude',
                 'baro_altitude', 'on_ground', 'velocity', 'true_track', 'vertical_rate')

    def __init__(self, plane_id, call_sign, country, longitude, latitude, baro_altitude, on_ground, velocity, true_track, vertical_rate):
        self.plane_id = plane_id
        self.call_sign = call_sign
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.baro_altitude = baro_altitude
        self.on_ground = on_ground
        self.velocity = velocity
        self.true_track = true_track
        self.vertical_rate = vertical_rate


    def __eq__(self, other):
        """Сравнение двух самолетов по идентификатору на равенство"""

        if isinstance(other, Plane):
            raise TypeError('Некорректный тип аргуманта!')

        if self.plane_id == other.plane_id:
            return True
        else:
            return False

    def __lt__(self, other):
        """Сравнение двух самолетов по высоте полета на меньше"""

        if not isinstance(other, Plane):
            raise TypeError('Некорректный тип аргуманта!')

        if self.baro_altitude < other.baro_altitude:
            return True
        else:
            return False

    def __le__(self, other):
        """Сравнение двух самолетов по высоте полета на больше"""

        if not isinstance(other, Plane):
            raise TypeError('Некорректный тип аргуманта!')

        if self.baro_altitude > other.baro_altitude:
            return True
        else:
            return False

    def __repr__(self):
        """Представление самолета в строковом виде"""
        return (f'Самолет, бортовой номер: {self.plane_id}, позывной: {self.call_sign}, страна регистрации: {self.country}, '
                f'координаты: (долгота: {self.latitude}, широта: {self.longitude})')


    def plane_obj_info(self):
        """Представление самолета в виде объекта"""
        return{
            'plane_id': self.plane_id,
            'call_sign': self.call_sign,
            'plane_country': self.country,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'baro_altitude': self.baro_altitude,
            'on_ground': self.on_ground,
            'velocity': self.velocity,
            'true_track': self.true_track,
            'vertical_rate': self.vertical_rate
        }
