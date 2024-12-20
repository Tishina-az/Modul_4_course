from abc import ABC, abstractmethod
from typing import Any, Dict, List

import requests
from requests import Response


class BaseHH(ABC):
    """ Абстрактный класс для работы с API HeadHunter """

    @abstractmethod
    def __connect_to_api(self) -> Response:
        """ Метод подключения к API """
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str) -> None:
        """ Метод получения списка вакансий по ключевому слову """
        pass


class HeadHunterAPI(BaseHH, ABC):
    """ Класс для работы с API HeadHunter """

    def __init__(self) -> None:
        """ Инициализатор класса, задающий атрибуты для подключения к API """
        self.__url: str = 'https://api.hh.ru/vacancies'
        self.__headers: Dict[str, str] = {'User-Agent': 'HH-User-Agent'}
        self.__params: Dict[str, Any] = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies: List[Dict[str, Any]] = []

    @property
    def vacancies(self) -> List[Dict[str, Any]]:
        """ Метод, возвращающий список вакансий """
        return self.__vacancies

    def _BaseHH__connect_to_api(self) -> Response:
        """ Метод подключения к API """
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        status_code = response.status_code
        if status_code != 200:
            raise ValueError(f"Ошибка {status_code}, попробуйте ещё раз!")
        else:
            return response

    def get_vacancies(self, keyword: str) -> None:
        """ Метод получения списка вакансий по ключевому слову """
        self.__params['text'] = keyword
        while self.__params.get('page') != 20:
            answer = self._BaseHH__connect_to_api()
            vacancies = answer.json().get('items', [])
            self.__vacancies.extend(vacancies)
            self.__params['page'] += 1
