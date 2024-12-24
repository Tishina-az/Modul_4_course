import json
import os.path
from abc import ABC, abstractmethod
from typing import Any

from src.vacancies import Vacancy


class BaseVacancyFile(ABC):
    """Базовый класс для работы с файлами вакансий"""

    @abstractmethod
    def load_vacancies(self) -> Any:
        """Получение списка объектов Vacancy из файла JSON"""
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
    """Класс для работы с вакансиями в формате JSON"""

    def __init__(self, filename: str = "vacancies.json") -> None:
        """Конструктор класса"""
        self.__filename = filename
        self.path_to_file = os.path.join(os.path.dirname(__file__), "..", "data", self.__filename)

    def load_vacancies(self) -> list[dict]:
        """Получение списка объектов Vacancy из файла JSON"""
        try:
            with open(self.path_to_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавление вакансии в файл JSON"""
        vacancies = self.load_vacancies()
        vacancy = vacancy.to_dict()
        if not any(
            vac.get("name") == vacancy.get("name") and vac.get("url") == vacancy.get("url") for vac in vacancies
        ):
            vacancies.append(vacancy)
            with open(self.path_to_file, "w", encoding="utf-8") as f:
                json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Удаление вакансии из файла JSON"""
        vacancies = self.load_vacancies()
        vacancy = vacancy.to_dict()
        new_data = [
            vac for vac in vacancies if vac.get("name") != vacancy.get("name") and vac.get("url") != vacancy.get("url")
        ]
        with open(self.path_to_file, "w", encoding="utf-8") as f:
            json.dump(new_data, f, ensure_ascii=False, indent=4)
