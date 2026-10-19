from colorama import Fore, init


def show_colored_text(text):
    init(autoreset=True)
    print(Fore.GREEN + text)