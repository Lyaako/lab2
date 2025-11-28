from hex_extractor import HexColorExtractor

if __name__ == "__main__":
    extractor = HexColorExtractor()

    # =-=- Поиск HEX-цветов по URL -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    url = "https://htmlcolorcodes.com/"
    print(f"\nПоиск по странице: {url}\n")
    colors_from_url = extractor.get_colors_from_url(url)
    if colors_from_url:
        for i, color in enumerate(colors_from_url, 1):
            print(f"{i:2d}. {color}")
    else:
        print("Цвета не найдены")

    # =-=- Поиск HEX-цветов по пользовательскому тексту -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    print("\nПоиск по тексту:\n")
    test_text = """
    Вот несколько цветов:
    Основной: #FF5733
    Акцент: #A1
    Фон: #000
    Неверный: #GGG
    Другой: #12AB45
    """
    found_colors = extractor.extract_hex_colors(test_text)
    for color_code in found_colors:
        full_color = '#' + color_code
        is_valid = extractor.validate_hex_color(full_color)
        status = "VALID" if is_valid else "INVALID"
        print(f"{full_color} - {status}")

    # =-=- Поиск HEX-цветов по файлу -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    print("\nПоиск по файлу 'colors.txt':\n")
    colors_from_file = extractor.get_colors_from_file("colors.txt")
    if colors_from_file:
        for color in colors_from_file:
            print(color)
    else:
        print("Файл не найден или цвета отсутствуют")