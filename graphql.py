import requests


def fuzz_graphql(endpoint, query, variable_name, value):

    mutations = []

    try:
        base = int(value)

        mutations = [
            base + 1,
            base + 5,
            base + 10
        ]

    except:
        return []

    results = []

    for m in mutations:

        payload = {
            "query": query,
            "variables": {
                variable_name: m
            }
        }

        r = requests.post(endpoint, json=payload)

        results.append((m, r.status_code, len(r.text)))

    return results