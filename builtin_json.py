import json


def parse_j(s):
    return json.loads(s or "{}")