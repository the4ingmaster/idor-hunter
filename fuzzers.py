import requests
from urllib.parse import urlencode
from utils import is_numeric, generate_numeric_variants, is_uuid, generate_uuid_variants


def fuzz_get(base_url, params, target_param):

    original_value = params[target_param]

    mutations = []

    if is_numeric(original_value):

        for v in generate_numeric_variants(original_value):

            mutated = params.copy()
            mutated[target_param] = str(v)
            mutations.append(mutated)

    elif is_uuid(original_value):

        for v in generate_uuid_variants():

            mutated = params.copy()
            mutated[target_param] = v
            mutations.append(mutated)

    return mutations



def fuzz_post(url, data, target_param):

    original = data[target_param]

    mutations = []

    if is_numeric(original):

        for v in generate_numeric_variants(original):

            mutated = data.copy()
            mutated[target_param] = str(v)
            mutations.append(mutated)

    elif is_uuid(original):

        for v in generate_uuid_variants():

            mutated = data.copy()
            mutated[target_param] = v
            mutations.append(mutated)

    return mutations