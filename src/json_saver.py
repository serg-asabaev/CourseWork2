from abc import ABC, abstractmethod
import json

from src.plane import Plane


class FileSaver(ABC):

    @abstractmethod
    def save_list_to_file(self, info: list, file_name: str):
        pass

    @abstractmethod
    def read_from_file(self, file_name: str):
        pass

    @abstractmethod
    def add_plane(self, file_name, plane: Plane):
        pass

    @abstractmethod
    def delete_plane(self, file_name, plane_id: str):
        pass

class JSONSaver(FileSaver):


    def save_list_to_file(self, info: list, file_name: str):
        """ Сохранение в файл списка самолетов """

        if len(file_name) == 0:
            raise FileNotFoundError('Пустой путь до файла!')

        with open(file_name, 'w', encoding="utf-8") as f:
            json.dump(info, f, ensure_ascii=False, indent=2)

            print(f"✓ Данные сохранены в {file_name}")


    def read_from_file(self, file_name: str):
        if len(file_name) == 0:
            raise FileNotFoundError('Пустой путь до файла!')

        with open(file_name, 'r', encoding='utf-8') as f:
            planes_info = json.load(f)

        return planes_info

    def add_plane(self, file_name, plane: Plane):
        if len(file_name) == 0:
            raise FileNotFoundError('Пустой путь до файла!')

        planes = self.read_from_file(file_name)

        plane_obj = plane.plane_obj_info()
        planes.append(plane_obj)

        self.save_list_to_file(planes, file_name)

        print(f"✓ Данные сохранены в {file_name}")


    def delete_plane(self, file_name, plane_id: str):
        if len(file_name) == 0:
            raise FileNotFoundError('Пустой путь до файла!')

        planes = self.read_from_file(file_name)
        planes = [item for item in planes if item.get('plane_id') != plane_id]

        self.save_list_to_file(planes, file_name)

        print(f"Борт № {plane_id} удален из файла {file_name}")
