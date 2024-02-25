from enum import Enum

__all__ = ['Style', 'Fore', 'Back', 'style', 'test', 'RESET']

BEGIN_STYLE = "\x1b["
"""Начало escape sequence для стилей"""

END_STYLE = "m"
"""Конец escape sequence для стилей"""

RESET = f"{BEGIN_STYLE}0{END_STYLE}"
"""escape sequence Для сброса всех установленных стилей"""


class Style(Enum):
    """Некоторые стили"""
    BOLD = 1
    ITALIC = 3
    UNDERLINE = 4
    INVERT = 7
    CROSSED = 9
    DOUBLE_UNDERLINE = 21
    FRAMED = 51


class Fore(Enum):
    """Цвет текста"""
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    LIGHT_GRAY = 37
    DEFAULT = 39
    GRAY = 90
    LIGHT_RED = 91
    LIGHT_GREEN = 92
    LIGHT_YELLOW = 93
    LIGHT_BLUE = 94
    LIGHT_MAGENTA = 95
    LIGHT_CYAN = 96
    WHITE = 97


class Back(Enum):
    """Цвет фона"""
    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    MAGENTA = 45
    CYAN = 46
    LIGHT_GRAY = 47
    DEFAULT = 49
    GRAY = 100
    LIGHT_RED = 101
    LIGHT_GREEN = 102
    LIGHT_YELLOW = 103
    LIGHT_BLUE = 104
    LIGHT_MAGENTA = 105
    LIGHT_CYAN = 106
    WHITE = 107


def style(string, *args):
    """ Добавляет стили в начало строки string и RESET в конец строки"""
    styles_map = map(lambda a: a.value if isinstance(a, Enum) else a, args)
    styles_str = map(str, styles_map)
    styles = ';'.join(styles_str)
    return f"{BEGIN_STYLE}{styles}{END_STYLE}{string}{RESET}"


def test(console=False, colors=False, styles=False, all=None):
    """Выводит различные стили в консоль для проверки"""
    if all is None:
        all = not (console or colors or styles)

    if all or console:
        print('Console test: ')
        draw_test_console()
    if all or colors:
        print('Colors: ')
        draw_colors_table()
    if all or styles:
        print('Styles: ')
        draw_styles_table()


def draw_styles_table():
    width = 20
    separator = ' '
    for index, curr in enumerate(Style):
        s = curr.name.center(width)
        print(style(s, curr.value, Back.BLACK, Fore.WHITE), end=separator)
        if index % 4 == 3:
            print()
            print()
    print()


def draw_colors_table():
    width = 20
    separator = ' '
    for fore, back, index in zip(Fore, Back, range(len(Back))):
        s = f"Fore.{fore.name}".center(width)
        print(style(s, fore, Back.WHITE), end=separator)
        print(style(s, fore, Back.BLACK), end=separator)

        s = f"Back.{back.name}".center(width)
        print(style(s, back, Fore.WHITE), end=separator)
        print(style(s, back, Fore.BLACK), end=separator)
        print()
    print()


def draw_test_console(to=108):
    for i in range(to):
        print(style(str(i).center(8), i), end=' ')
        if i % 12 == 11:
            print()
    print()
