from src.filters import filtering_by_currency, filtering_by_salary, get_top_vacancies, sorted_by_salary


def test_filtering_by_salary(vacancies_list: list[dict], vacancy_2: dict, vacancy_3: dict) -> None:
    """Тестируем фильтрацию по заработной плате"""
    assert filtering_by_salary(vacancies_list, 150000, 300000) == [vacancy_2, vacancy_3]


def test_filtering_by_currency(vacancies_list: list[dict], vacancy_3: dict) -> None:
    """Тестируем фильтрацию по валюте плате"""
    assert filtering_by_currency(vacancies_list, "USD") == [vacancy_3]


def test_sorted_by_salary(vacancies_list: list[dict], vacancy_1: dict, vacancy_2: dict, vacancy_3: dict) -> None:
    """Тестируем сортировку вакансий по убыванию зарплаты"""
    assert sorted_by_salary(vacancies_list) == [vacancy_2, vacancy_1, vacancy_3]


def test_get_top_vacancies(vacancies_list: list[dict], vacancy_1: dict) -> None:
    """Тестируем возвращение списка топ вакансий"""
    assert get_top_vacancies(vacancies_list, 1) == [vacancy_1]
