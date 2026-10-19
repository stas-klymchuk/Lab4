from builtin_math import calculate_sqrt
from builtin_random import generate_random_number
from ext_colorama import show_colored_text
from ext_requests import check_website

def main() -> None:

    print("=== Запуск лабораторної роботи ===")
    calculate_sqrt(25)
    generate_random_number(1, 10)
    show_colored_text("Кольоровий текст працює!")
    check_website("https://www.google.com")


if __name__ == "__main__":
    main()