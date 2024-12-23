import pytest

from src.utils import JsonVacancy
from src.vacancies import Vacancy


@pytest.fixture
def vacancy_1() -> dict:
    return {
        "name": "Программист в стартап-проект",
        "area": {"name": "Ташкент"},
        "salary": {"from": 110000, "to": 150000, "currency": "RUR"},
        "alternate_url": "https://hh.ru/vacancy/113067633",
    }


@pytest.fixture
def vacancy_2() -> dict:
    return {
        "name": "Инженер-робототехник",
        "area": {"name": "Москва"},
        "salary": {"from": 200000, "to": None, "currency": "RUR"},
        "alternate_url": "https://hh.ru/vacancy/112175780",
    }


@pytest.fixture
def vacancy_3() -> dict:
    return {
        "name": "Программист",
        "area": {"name": "Санкт-Петербург"},
        "salary": {"from": None, "to": 2000, "currency": "USD"},
        "alternate_url": "https://hh.ru/vacancy/112175793",
    }


@pytest.fixture
def vacancies_list(vacancy_1, vacancy_2, vacancy_3) -> list:
    return [vacancy_1, vacancy_2, vacancy_3]


@pytest.fixture
def valid_vacancy_obj() -> Vacancy:
    return Vacancy("Аналитик данных", "Москва", 200000, 350000, "https://hh.ru/vacancy/112424253")


@pytest.fixture
def invalid_vacancy_obj() -> Vacancy:
    return Vacancy(None, None, None, None, None)


@pytest.fixture
def valid_vacancy_obj_2() -> Vacancy:
    return Vacancy("Аналитик данных", "Москва", 80000, 150000, "https://hh.ru/vacancy/112424253")


@pytest.fixture
def vacancy_file() -> JsonVacancy:
    return JsonVacancy("example.json")
