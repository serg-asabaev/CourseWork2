from src.api_adapter import APIAdapter
from src.planes_info import PlaneInfo

if __name__ == '__main__':
    api = APIAdapter()
    api.get_aeroplanes('Russian Federation')

    planes_info = PlaneInfo(api.aeroplanes, '39de4f')

    res_time = planes_info.time
    res_states = planes_info.states


    print(planes_info.get_plane())