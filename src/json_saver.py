from abc import ABC, abstractmethod
import json

from src.plane import Plane


class FileSaver(ABC):

    @abstractmethod
    def save_list_to_file(self, info: list):
        pass

    @abstractmethod
    def read_from_file(self):
        pass

    @abstractmethod
    def add_plane(self, plane: Plane):
        pass

    @abstractmethod
    def delete_plane(self, plane_id: str):
        pass


class JSONSaver(FileSaver):
    """Класс для работы с файлом JSON"""

    __file_name = 'data/planes_info.json'

    def __init__(self, __file_name):
        self.__file_name = __file_name

    def save_list_to_file(self, info: list):
        """ Сохранение в файл JSON списка самолетов """

        if len(self.__file_name) == 0:
            raise FileNotFoundError('Пустой путь до файла!')

        with open(self.__file_name, 'w', encoding="utf-8") as f:
            json.dump(info, f, ensure_ascii=False, indent=2)

            print(f"✓ Данные сохранены в {self.__file_name}")


    def read_from_file(self):
        """Чтение списка обьектов из фаула JSON"""

        if len(self.__file_name) == 0:
            raise FileNotFoundError('Пустой путь до файла!')

        with open(self.__file_name, 'r', encoding='utf-8') as f:
            planes_info = json.load(f)

        return planes_info

    def add_plane(self, inp_plane: Plane):
        """Добавление самолета в файл JSON"""

        if len(self.__file_name) == 0:
            raise FileNotFoundError('Пустой путь до файла!')

        planes = self.read_from_file()
        plane_obj = inp_plane.plane_obj_info()

        eq_flag = False

        for plane in planes:
            if plane == plane_obj:
                eq_flag = True

        if not eq_flag:
            planes.append(plane_obj)
            self.save_list_to_file(planes)
            print(f"✓ Данные сохранены в {self.__file_name}")
        else:
            print(f"В файле {self.__file_name} уже есть добавляемый объект")


    def delete_plane(self, plane_id: str):
        """Удаление самолета из файла JSON по идентификатору борта"""

        if len(self.__file_name) == 0:
            raise FileNotFoundError('Пустой путь до файла!')

        planes = self.read_from_file()
        planes = [item for item in planes if item.get('plane_id') != plane_id]

        self.save_list_to_file(planes)

        print(f"Борт № {plane_id} удален из файла {self.__file_name}")
