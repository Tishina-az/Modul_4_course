# Создание экземпляра класса для работы с API сайтов с вакансиями
from src.api_query import HeadHunterAPI
from src.utils import JsonVacancy
from src.vacancies import Vacancy

hh_api = HeadHunterAPI()

# Получение вакансий с hh.ru в формате JSON
hh_api.get_vacancies("Python")

# Преобразование набора данных из JSON в список объектов
vacancies_list = Vacancy.vacancy_from_list(hh_api.vacancies)

# Пример работы конструктора класса с одной вакансией
vacancy = Vacancy("Python Developer", "Москва", 100000, 150000, "https://hh.ru/vacancy/111348872")

# Сохранение информации о вакансиях в файл
json_saver = JsonVacancy()
json_saver.add_vacancy(vacancy)
print(json_saver.load_vacancies())
print(type(json_saver.load_vacancies()))
json_saver.delete_vacancy(vacancy)
#
# # Функция для взаимодействия с пользователем
# def user_interaction():
#     platforms = ["HeadHunter"]
#     search_query = input("Введите поисковый запрос: ")
#     top_n = int(input("Введите количество вакансий для вывода в топ N: "))
#     filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
#     salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000
#
#     filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
#
#     ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
#
#     sorted_vacancies = sort_vacancies(ranged_vacancies)
#     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
#     print_vacancies(top_vacancies)
#
#
# if __name__ == "__main__":
#     user_interaction()
