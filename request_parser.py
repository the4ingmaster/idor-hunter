import requests


def parse_burp_request(file):

    with open(file) as f:
        lines = f.read().splitlines()

    method, path, _ = lines[0].split()

    headers = {}

    for line in lines[1:]:

        if ":" in line:
            k, v = line.split(":",1)
            headers[k.strip()] = v.strip()

    host = headers.get("Host")

    url = "https://" + host + path

    return method, url, headers