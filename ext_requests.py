import requests


def check_website(url):
    return requests.get(url).status_code