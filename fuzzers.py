import requests
from utils import is_numeric, generate_numeric_variants


def fuzz_parameters(url, params, headers):

    results = []

    for key,value in params.items():

        if is_numeric(value):

            variants = generate_numeric_variants(value)

            for v in variants:

                new_params = params.copy()
                new_params[key] = str(v)

                r = requests.get(url, params=new_params, headers=headers)

                results.append((key,v,r.status_code,len(r.text)))

    return results
