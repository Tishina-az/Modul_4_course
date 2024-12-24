import unittest
from unittest.mock import MagicMock, patch

from requests.models import Response

from src.api_query import HeadHunterAPI


class TestHeadHunterAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.api = HeadHunterAPI()

    @patch("requests.get")
    def test_connect_to_api_success(self, mock_get: MagicMock) -> None:
        """Тестируем работу при успешном соединении"""
        mock_response = MagicMock(spec=Response)
        mock_response.status_code = 200
        mock_response.json.return_value = {"items": []}
        mock_get.return_value = mock_response

        response = self.api._connect_to_api()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"items": []})

    @patch("requests.get")
    def test_connect_to_api_failure(self, mock_get: MagicMock) -> None:
        """Тестируем работу при возникновении ошибки в ответе"""
        mock_response = MagicMock(spec=Response)
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        with self.assertRaises(ValueError) as context:
            self.api._connect_to_api()

        self.assertEqual(str(context.exception), "Ошибка 404, попробуйте ещё раз!")

    @patch("requests.get")
    def test_get_vacancies(self, mock_get: MagicMock) -> None:
        """Получение вакансий при успешном ответе от API"""
        mock_response = MagicMock(spec=Response)
        mock_response.status_code = 200
        mock_response.json.return_value = {"items": [{"id": 1, "name": "Vacancy 1"}, {"id": 2, "name": "Vacancy 2"}]}
        mock_get.return_value = mock_response

        self.api.get_vacancies("Python")
        self.assertEqual(self.api.vacancies[0]["name"], "Vacancy 1")
        self.assertEqual(self.api.vacancies[1]["name"], "Vacancy 2")
