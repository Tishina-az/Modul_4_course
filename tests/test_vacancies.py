from src.vacancies import Vacancy


class TestVacancy:

    def test_vacancy_initialization(self, valid_vacancy_obj: Vacancy) -> None:
        """Тестируем конструктор класса"""
        assert valid_vacancy_obj.to_dict()["name"] == "Аналитик данных"
        assert valid_vacancy_obj.to_dict()["area"] == "Москва"
        assert valid_vacancy_obj.to_dict()["salary_from"] == 200000
        assert valid_vacancy_obj.to_dict()["salary_to"] == 350000
        assert valid_vacancy_obj.to_dict()["url"] == "https://hh.ru/vacancy/112424253"

    def test_name_validation_empty(self, invalid_vacancy_obj: Vacancy) -> None:
        """Проверяем отсутствие названия вакансии"""
        assert invalid_vacancy_obj.to_dict()["name"] == "Название вакансии не указано!"

    def test_area_validation_empty(self, invalid_vacancy_obj: Vacancy) -> None:
        """Проверяем отсутствие названия города в вакансии"""
        assert invalid_vacancy_obj.to_dict()["area"] == "Город не указан."

    def test_salary_validation_none(self, invalid_vacancy_obj: Vacancy) -> None:
        """Проверяем отсутствие зарплаты в вакансии"""
        assert invalid_vacancy_obj.to_dict()["salary_from"] == 0
        assert invalid_vacancy_obj.to_dict()["salary_to"] == 0

    def test_url_validation_empty(self, invalid_vacancy_obj: Vacancy) -> None:
        """Проверяем отсутствие ссылки на вакансию"""
        assert invalid_vacancy_obj.to_dict()["url"] == "Ссылка на вакансию отсутствует..."

    def test_vacancy_from_dict(self, vacancy_1: dict) -> None:
        """Тестируем получение объекта Vacancy из словаря"""
        vacancy = Vacancy.vacancy_from_dict(vacancy_1)
        assert vacancy.to_dict()["name"] == vacancy_1["name"]
        assert vacancy.to_dict()["area"] == vacancy_1["area"]["name"]
        assert vacancy.to_dict()["salary_from"] == vacancy_1["salary"]["from"]
        assert vacancy.to_dict()["salary_to"] == vacancy_1["salary"]["to"]
        assert vacancy.to_dict()["url"] == vacancy_1["alternate_url"]

    def test_vacancy_comparisons(self, valid_vacancy_obj_2: Vacancy, valid_vacancy_obj: Vacancy) -> None:
        """Проверка сравнения объектов вакансий по зарплате"""
        assert valid_vacancy_obj_2 < valid_vacancy_obj
        assert valid_vacancy_obj > valid_vacancy_obj_2
        assert valid_vacancy_obj_2 <= valid_vacancy_obj
        assert valid_vacancy_obj >= valid_vacancy_obj_2
