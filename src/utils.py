import json
import os.path
from abc import ABC, abstractmethod
from typing import List

from src.vacancies import Vacancy


class BaseVacancyFile(ABC):
    """ Базовый класс для работы с файлами вакансий """

    @abstractmethod
    def load_vacancies(self) -> List[Vacancy]:
        """ Получение списка объектов Vacancy из файла JSON """
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавление вакансии в файл."""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Удаление вакансии по идентификатору."""
        pass


class JsonVacancy(BaseVacancyFile):
    """ Класс для работы с вакансиями в формате JSON """

    def __init__(self, filename: str = 'vacancies.json'):
        """ Конструктор класса """
        self.__filename = filename
        self.path_to_file = os.path.join(os.path.dirname(__file__), '..', 'data', self.__filename)

    def load_vacancies(self) -> List[Vacancy]:
        """ Получение списка объектов Vacancy из файла JSON """
        try:
            with open(self.path_to_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return Vacancy.vacancy_from_list(data)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """ Добавление вакансии в файл JSON """
        vacancies = self.load_vacancies()
        if not any(vac.__name == vacancy.__name and vac.__url == vacancy.__url for vac in vacancies):
            with open(self.path_to_file, 'a', encoding='utf-8') as f:
                json.dump(vacancy.to_dict(), f, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """ Удаление вакансии из файла JSON """
        vacancies = self.load_vacancies()
        new_data = [vac for vac in vacancies if vac.__url != vacancy.__url]
        with open(self.path_to_file) as f:
            json.dump([data.to_dict() for data in new_data], f, ensure_ascii=False, indent=4)
