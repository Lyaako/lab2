"""
Модуль для извлечения и валидации HEX-цветов из текста, URL или файла.

HEX-цвета должны соответствовать одному из форматов:
- #RGB (3 символа)
- #RRGGBB (6 символов)
Регистр букв не важен.
"""

import re
import requests
from typing import List


class HexColorExtractor:
    """Класс для извлечения и проверки синтаксически корректных HEX-цветов."""

    def __init__(self):
        # Регулярное выражение для поиска HEX-цветов (#RGB и #RRGGBB)
        self.hex_pattern = re.compile(r'#([0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})\b')

    def extract_hex_colors(self, text: str) -> List[str]:
        """
        Извлекает все HEX-цвета из переданного текста.

        Args:
            text (str): Текст для поиска.

        Returns:
            List[str]: Список найденных HEX-цветов (в исходном регистре и длине).
        """
        return self.hex_pattern.findall(text)

    def validate_hex_color(self, color: str) -> bool:
        """
        Проверяет, является ли строка синтаксически корректным HEX-цветом.

        Args:
            color (str): Строка, которую нужно проверить.

        Returns:
            bool: True, если корректный HEX-цвет, иначе False.
        """
        if not isinstance(color, str):
            return False
        return bool(self.hex_pattern.fullmatch(color))

    def get_colors_from_url(self, url: str) -> List[str]:
        """
        Извлекает HEX-цвета с указанной веб-страницы.

        Args:
            url (str): URL веб-страницы.

        Returns:
            List[str]: Список найденных HEX-цветов.
        """
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            # Используем .text, чтобы получить HTML как строку
            matches = self.hex_pattern.findall(response.text)
            # Восстанавливаем решётку, так как findall возвращает только группу
            return ['#' + match for match in matches]
        except Exception as e:
            print(f"Ошибка при загрузке страницы {url}: {e}")
            return []

    def get_colors_from_file(self, filepath: str) -> List[str]:
        """
        Извлекает HEX-цвета из текстового файла.

        Args:
            filepath (str): Путь к файлу.

        Returns:
            List[str]: Список найденных HEX-цветов.
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                matches = self.hex_pattern.findall(content)
                return ['#' + match for match in matches]
        except Exception as e:
            print(f"Ошибка при чтении файла {filepath}: {e}")
            return []