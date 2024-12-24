from typing import Any, Dict, List


class Vacancy:
    """ Класс для работы с вакансиями """
    __slots__ = ('__name', '__area', '__salary_from', '__salary_to', '__url')

    def __init__(self, name, area, salary_from, salary_to, url) -> None:
        """ Инициализация экземпляра вакансии """
        self.__name: str = self.__name_validation(name)
        self.__area: str = self.__area_validation(area)
        self.__salary_from: int = self.__salary_validation(salary_from)
        self.__salary_to: int = self.__salary_validation(salary_to)
        self.__url: str = self.__url_validation(url)

    @staticmethod
    def __name_validation(name: str) -> str:
        """ Валидация названия вакансии """
        if not name:
            return "Название вакансии не указано!"
        return name

    @staticmethod
    def __area_validation(area: str) -> str:
        """ Валидация указания города в вакансии """
        if not area:
            return "Город не указан."
        return area

    @staticmethod
    def __salary_validation(salary: int) -> int:
        """ Валидация указания зарплаты в вакансии """
        if salary is not None:
            return salary
        return 0

    @staticmethod
    def __url_validation(url: str) -> str:
        """ Валидация наличия ссылки на вакансию """
        if not url:
            return "Ссылка на вакансию отсутствует..."
        return url

    @classmethod
    def vacancy_from_dict(cls, vacancy_dict: Dict) -> 'Vacancy':
        """ Создает объект Vacancy из словаря """

        name = vacancy_dict.get('name')
        url = vacancy_dict.get('alternate_url')
        salary_from = vacancy_dict.get('salary').get('from') if vacancy_dict.get('salary') else None
        salary_to = vacancy_dict.get('salary').get('to') if vacancy_dict.get('salary') else None
        area = vacancy_dict.get('area').get('name')
        vacancy = cls(name, area, salary_from, salary_to, url)
        return vacancy

    @classmethod
    def vacancy_from_list(cls, vacancy_list: List[Dict]) -> List['Vacancy']:
        """ Получаем список объектов Vacancy из списка словарей """
        return [cls.vacancy_from_dict(vacancy) for vacancy in vacancy_list]

    @staticmethod
    def to_list(vacancies_list: List['Vacancy']):
        """ Преобразование списка объектов Vacancy в список словарей """
        return [vacancy.to_dict() for vacancy in vacancies_list]

    def to_dict(self) -> Dict:
        """ Преобразование объекта Vacancy в словарь"""
        return {
            'name': self.__name,
            'area': self.__area,
            'salary_from': self.__salary_from,
            'salary_to': self.__salary_to,
            'url': self.__url
        }

    def __ge__(self, other: 'Vacancy') -> Any:
        """ Сравнения уровня зарплат по принципу 'больше или равно' """
        return self.__salary_from > other.__salary_from

    def __le__(self, other: 'Vacancy') -> Any:
        """ Сравнения уровня зарплат по принципу 'меньше или равно' """
        return self.__salary_from <= other.__salary_from

    def __gt__(self, other: 'Vacancy') -> Any:
        """ Сравнения уровня зарплат по принципу 'больше' """
        return self.__salary_from > other.__salary_from

    def __lt__(self, other: 'Vacancy') -> Any:
        """ Сравнения уровня зарплат по принципу 'меньше' """
        return self.__salary_from < other.__salary_from

    def __str__(self) -> str:
        """ Строковое представление вакансий """
        return (f"Вакансия: {self.__name}. Город: {self.__area}.\n"
                f"Зарплата: {self.__salary_from} - {self.__salary_to}.\n"
                f"Ссылка на вакансию: {self.__url}")
