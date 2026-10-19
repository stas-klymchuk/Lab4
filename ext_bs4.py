from bs4 import BeautifulSoup


def parse_html(h):
    return BeautifulSoup(h, "html.parser")