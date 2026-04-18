from src.planes_info import PlanesInfo


class Plane:
    baro_altitude = 0
    on_ground = True
    velocity = 0
    true_track = 0
    vertical_rate = 0

    def __init__(self, plane_id, call_sign, country, longitude, latitude):
        self.plane_id = plane_id
        self.call_sign = call_sign
        self.country = country
        self.latitude = latitude
        self.longitude = longitude


    def __eq__(self, other):

        if not other.isinstance(other, Plane):
            raise TypeError('Некорректный тип аргуманта!')

        if self.plane_id == other.plane_id:
            return True
        else:
            return False

    def __repr__(self):
        return (f'Самолет, бортовой номер: {self.plane_id}, позывной: {self.call_sign}, страна регистрации: {self.country}, '
                f'координаты: (долгота: {self.latitude}, широта: {self.longitude})')


    def plane_obj_info(self):
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
