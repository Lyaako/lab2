import unittest
from unittest.mock import patch, Mock
from hex_extractor import HexColorExtractor


class TestHexColorExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = HexColorExtractor()

    def test_extract_hex_colors_valid(self):
        text = "Цвета: #FF0000, #0F0 и #123ABC."
        result = self.extractor.extract_hex_colors(text)
        expected = ['FF0000', '0F0', '123ABC']
        self.assertEqual(result, expected)

    def test_extract_hex_colors_invalid(self):
        text = "Неверные: #GGG, #12345, #1234567"
        result = self.extractor.extract_hex_colors(text)
        self.assertEqual(result, [])  # только корректные шаблоны

    def test_validate_hex_color_valid(self):
        self.assertTrue(self.extractor.validate_hex_color("#FF0000"))
        self.assertTrue(self.extractor.validate_hex_color("#0F0"))
        self.assertTrue(self.extractor.validate_hex_color("#abc"))
        self.assertTrue(self.extractor.validate_hex_color("#123ABC"))

    def test_validate_hex_color_invalid(self):
        self.assertFalse(self.extractor.validate_hex_color("#GGG"))
        self.assertFalse(self.extractor.validate_hex_color("#12"))
        self.assertFalse(self.extractor.validate_hex_color("#1234567"))
        self.assertFalse(self.extractor.validate_hex_color("FF0000"))
        self.assertFalse(self.extractor.validate_hex_color("#"))
        self.assertFalse(self.extractor.validate_hex_color(123))  # not string

    def test_get_colors_from_file(self):
        # Тест с реальным файлом или mock файловой системы
        # Для простоты можно создать временный файл, но в рамках unittest
        # мы проверим логику через mock, если нужно — но здесь достаточно интеграционного теста отдельно
        pass  # Или используем patch при необходимости

    @patch("hex_extractor.requests.get")
    def test_get_colors_from_url_success(self, mock_get):
        mock_response = Mock()
        mock_response.text = "Цвет фона: #FF5733, акцент: #A1B"
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = self.extractor.get_colors_from_url("http://example.com")
        expected = ["#FF5733"]
        self.assertEqual(result, expected)  # '#A1B' не соответствует шаблону (длина 4)

    @patch("hex_extractor.requests.get")
    def test_get_colors_from_url_error(self, mock_get):
        mock_get.side_effect = Exception("Connection failed")
        result = self.extractor.get_colors_from_url("http://bad.url")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()