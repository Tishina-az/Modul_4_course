from src.api_query import HeadHunterAPI
from src.filters import filtering_by_currency, filtering_by_salary, get_top_vacancies, sorted_by_salary
from src.utils import JsonVacancy
from src.vacancies import Vacancy


# Функция для взаимодействия с пользователем
def user_interaction() -> None:
    print("Здравствуйте!")
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    currency = input("Выберете валюту для фильтрации вакансий (RUR, EUR, USD): ")
    while currency.upper() not in ['RUR', 'EUR', 'USD']:
        print("Введите корректный ответ!")
        currency = input("Выберете валюту для фильтрации вакансий (RUR, EUR, USD): ")

    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000
    min_salary, max_salary = map(int, salary_range.split(" - "))

    hh_api = HeadHunterAPI()
    hh_api.get_vacancies(search_query)

    vacancies_list = hh_api.vacancies

    vacancies_by_currency = filtering_by_currency(vacancies_list, currency.upper())
    vacancies_by_salary = filtering_by_salary(vacancies_by_currency, min_salary, max_salary)
    vacancies_top = get_top_vacancies(sorted_by_salary(vacancies_by_salary), top_n)

    list_objects = Vacancy.vacancy_from_list(vacancies_top)

    json_saver = JsonVacancy()

    for vacancy in list_objects:
        json_saver.add_vacancy(vacancy)
        print(vacancy)


if __name__ == "__main__":
    user_interaction()
