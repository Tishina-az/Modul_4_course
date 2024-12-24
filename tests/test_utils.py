from unittest.mock import mock_open, patch

from src.utils import JsonVacancy
from src.vacancies import Vacancy


def test_load_vacancies_file_not_found(vacancy_file: JsonVacancy) -> None:
    """Поведение метода при отсутствии файла"""
    with patch("builtins.open", side_effect=FileNotFoundError):
        vacancies = vacancy_file.load_vacancies()
        assert vacancies == []


def test_load_vacancies_empty_file(vacancy_file: JsonVacancy) -> None:
    """Чтение пустого файла"""
    with patch("builtins.open", new_callable=mock_open, read_data="[]"):
        vacancies = vacancy_file.load_vacancies()
        assert vacancies == []


def test_load_vacancies_with_data(
    vacancy_file: JsonVacancy, valid_vacancy_obj: Vacancy, valid_vacancy_obj_2: Vacancy
) -> None:
    """Чтение файла с данными"""
    with patch(
        "builtins.open", new_callable=mock_open, read_data='[{"name": "Программист", "url": "https://example.com"}]'
    ):
        vacancies = vacancy_file.load_vacancies()
        assert len(vacancies) == 1
        assert vacancies[0]["name"] == "Программист"


def test_add_vacancy_new(vacancy_file: JsonVacancy, valid_vacancy_obj_2: Vacancy) -> None:
    """Добавление новой вакансии в файл"""
    m_open = mock_open()
    with patch("builtins.open", m_open), patch("json.dump") as mock_dump:
        vacancy_file.add_vacancy(valid_vacancy_obj_2)

    m_open.assert_called_with(vacancy_file.path_to_file, "w", encoding="utf-8")
    mock_dump.assert_called_once()


def test_add_vacancy_duplicate(vacancy_file: JsonVacancy, valid_vacancy_obj: Vacancy) -> None:
    """Тестируем поведение, при попытке добавить дубликат вакансии"""
    with patch(
        "builtins.open",
        new_callable=mock_open,
        read_data='[{"name": "Аналитик данных", "url": "https://hh.ru/vacancy/112424253"}]',
    ):
        vacancy_file.add_vacancy(valid_vacancy_obj)

    with patch("builtins.open", mock_open()):
        vacancy_file.add_vacancy(valid_vacancy_obj)


def test_delete_vacancy_existing(vacancy_file: JsonVacancy, valid_vacancy_obj_2: Vacancy) -> None:
    """Удаление существующей вакансии"""
    with patch(
        "builtins.open",
        new_callable=mock_open,
        read_data='[{"name": "Аналитик данных", "url": "https://hh.ru/vacancy/11242425"}]',
    ):
        vacancy_file.delete_vacancy(valid_vacancy_obj_2)

    with patch("builtins.open", mock_open()) as m_open, patch("json.dump") as mock_dump:
        vacancy_file.delete_vacancy(valid_vacancy_obj_2)

    m_open.assert_called_with(vacancy_file.path_to_file, "w", encoding="utf-8")
    mock_dump.assert_called_once()
