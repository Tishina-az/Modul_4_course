from typing import Dict, List


def filtering_by_salary(vacancies_list: List[Dict], salary_from: int, salary_to: int) -> List[Dict]:
    """ Фильтрация вакансий в заданном диапазоне заработной платы """
    filtered_vacancy = []
    for vacancy in vacancies_list:
        salary = vacancy.get('salary').get('from') if vacancy.get('salary') else 0
        if salary is None:
            salary = 0
        if salary_from <= salary <= salary_to:
            filtered_vacancy.append(vacancy)
        elif salary == 0:
            filtered_vacancy.append(vacancy)
    return filtered_vacancy


def filtering_by_currency(vacancies_list: List[Dict], currency: str = 'RUR') -> List[Dict]:
    """ Фильтрация вакансий по заданной валюте """
    filtered_vacancy = []
    for vacancy in vacancies_list:
        if vacancy.get('salary') is None:
            filtered_vacancy.append(vacancy)
        else:
            if currency == vacancy.get('salary').get('currency'):
                filtered_vacancy.append(vacancy)
    return filtered_vacancy


def sorted_by_salary(vacancies_list: List[Dict]) -> List[Dict]:
    """ Сортировка вакансий по убыванию зарплаты """
    filtered_vacancy = sorted(
        vacancies_list,
        key=lambda x: (x.get('salary').get('from') if x.get('salary') else 0) or 0,
        reverse=True
    )
    return filtered_vacancy


def get_top_vacancies(vacancies_list: List[Dict], top_n: int) -> List[Dict]:
    """ Получение топ N вакансий """
    filtered_vacancy = vacancies_list[:top_n]
    return filtered_vacancy
