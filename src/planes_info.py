
class PlanesInfo:

    def __init__(self, planes_info_response, icao24):
        self.time = planes_info_response['time']
        self.states = planes_info_response['states']
        self.plane_info = self.get_current_plane(icao24)


    def get_plane(self):
        return {
            'plane_id': self.plane_info[0],
            'call_sign': self.plane_info[1],
            'country': self.plane_info[2],
            'longitude': self.plane_info[5],
            'latitude': self.plane_info[6],
            'baro_altitude': self.plane_info[7],
            'on_ground': self.plane_info[8],
            'velocity': self.plane_info[9],
            'true_track': self.plane_info[10],
            'vertical_rate': self.plane_info[11]
        }

    def get_current_plane(self, icao24):

        res_plane = []

        for plane in self.states:
            if plane[0] == icao24:
                res_plane = plane

        return res_plane

    def is_equal_speed(self, other):
        if not isinstance(self, PlanesInfo) or not isinstance(other, PlanesInfo):
            raise TypeError('Некорректный тип аргуманта!')

        self_state = self.get_plane()
        other_state = other.get_plane()